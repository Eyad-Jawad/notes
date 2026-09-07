## **The source:** https://beej.us/guide/bgnet/pdf/bgnet_usl_c_1.pdf

Sockets are UNIX file descriptors, descriptors are numbers attached to files, so sockets are files, there are many types of sockets, one type is Raw Sockets, but that doesn't matter for now, anohter two types are:

- Datagram Sockets: Or `SOCK_DGRAM`, which are connectionless sockets, means you can skip `connect()`
- Stream Sockets: Or `SOCK_STREAM`, which are two way sockets, and things sent are recived in order and error free, used in `ssh`, `telnet`, and `HTTP`.

the stream sockets above achive that using the "Transmision Control Protocol", or known as "TCP", the datagram sockets are not as reliable as the former, the data may arrive, but if it does it'll error free, it uses what's known as the "User Datagram Protocol", as known as "UDP"

They are connectionless because you don't have to maintain a connection in it as you'd have to do with the stream sockets

One might use a UDP over TCP for speed when that's the priority

![[Pasted image 20260606175123.png]]


### Internet Protocol version 4, and 6
I'm sure you know but verision 4 is the older 32 bit IPs, and version 6 is the newer 128 bit IPs:
```bash
192.0.2.111 # IPv4
2001:0db8:c9d2:aee5:73e3:934a:a5ae:9551 # IPv6
```
you can also use the colons to compress the zeros or ignore the leading zeros as well, there's also a way to use IPv4 in IPv6, which is using this pattern in a compatibility mode:
```bash
::ffff:IPv4 Address
```

there's something called a netmask, that you run on your IP in a bitwise-and address to get your host's IP address, which is just a bunch of ones followed by zeros, that's why it was changed later to just  a slash followed by the number of ones:

	(E.g. with that netmask, if your IP is 192.0.2.12, then your network is
	192.0.2.12	 AND 255.255.255.0 which gives 192.0.2.0.
	the new one:  192.0.2.12/30	

there's also the port which is a 16 bit number representing the use of this specific route, the os might give privliges to some ports depending on their use

you know about the endians and bit order, the big is the normal one, the little is the reverse one, in 8 bits form, and appearantly there's something called Network Byte Order as well, at that you'd always run a function to order things:

![[Pasted image 20260614120610.png]]

short being 2 bytes, and long being 4 bytess, host is the local endian, and network is the more universal one per se, Basically, you’ll want to convert the numbers to Network Byte Order before they go out on the wire, and convert them to Host Byte Order as they come in off the wire

### structs
a socket descriptor is `int`
then we have a socket named `addrinfo` which has to do with host name lookups, service name lookups, and other things, and it is genarally the first socket you'd call when making a connection:

```C
struct addrinfo {
	int              ai_flags;     // AI_PASSIVE, AI_CANONNAME, etc.
	int              ai_family;    // AF_INET, AF_INET6, AF_UNSPEC
	int              ai_socktype;  // SOCK_STREAM, SOCK_DGRAM
	int              ai_protocol;  // use 0 for "any"
	size_t           ai_addrlen;   // size of ai_addr in bytes
	struct sockaddr *ai_addr;      // struct sockaddr_in or _in6
	char            *ai_canonname; // full canonical hostname
	
	struct addrinfo *ai_next;      // linked list, next node
}; // I think ai means addrinfo?
```

```C
struct sockaddr {
	unsigned short sa_family;   // address family, AF_xxx
	char           sa_data[14]; // 14 bytes of protocol address
};
```

`AF_INET` is IPv4, and `AF_INET6` is IPv6, `sa_data` stores the destinationa address and port

```C
// (IPv4 only--see struct sockaddr_in6 for IPv6)
struct sockaddr_in {
	short int          sin_family;      // Address family, AF_INET
	unsigned short int sin_port;        // Port number
	struct             in_addrsin_addr; // Internet address
	unsigned char      sin_zero[8];     // Same size as struct sockaddr
};

// Internet address (a structure for historical reasons)
struct in_addr {
	uint32_t s_addr; // that's a 32-bit int (4 bytes)
};
```
that last variable is for padding it, it'll be just zeros idk why, and `sin_port` must be in Network Byte Order

```C
// (IPv6 only--see struct sockaddr_in and struct in_addr for IPv4)
struct sockaddr_in6 {
	u_int16_t       sin6_family;   // address family, AF_INET6
	u_int16_t       sin6_port;     // port, Network Byte Order
	u_int32_t       sin6_flowinfo; // IPv6 flow information
	struct in6_addr sin6_addr;     // IPv6 address
	u_int32_t       sin6_scope_id; // Scope ID
};

struct in6_addr {
	unsigned char   s6_addr[16];   // IPv6 address
};
```

then we have a storage unit large enough to fit both IPs, and then cast then IP into it's respective struct:
```C
struct sockaddr_storage {
	sa_family_t ss_family; // address family
	
	// all this is padding, implementation specific, ignore it:
	char    __ss_pad1[_SS_PAD1SIZE];
	int64_t __ss_align;
	char    __ss_pad2[_SS_PAD2SIZE];
};
```

and in the end you can use a function `in_pton()` (pton stands for presentation network, or printable network) to convert  `sockaddr_in` to `in_addr`, or `sockaddr_in6` to `in6_addr`:

```C
inet_pton(AF_INET, "10.12.110.57", &(sa.sin_addr));
inet_pton(AF_INET6, "2001:db8:63b3:1::3490", &(sa6.sin6_addr));
```

 and this function will return `-1` on error and `0` if the address is not messed up, and `1` for good, this function transforms number addresses to binary presentation, if you want it the other way around there's a function called `inet_ntop()` for that:
 ```C
// IPv4:

char ip4[INET_ADDRSTRLEN];// space to hold the IPv4 string
struct sockaddr_in sa;    // pretend this is loaded with something
inet_ntop(AF_INET, &(sa.sin_addr), ip4, INET_ADDRSTRLEN);
printf("The IPv4 address is: %s\n", ip4);


// IPv6:

char ip6[INET6_ADDRSTRLEN]; // space to hold the IPv6 string
struct sockaddr_in6 sa6;    // pretend this is loaded with something
inet_ntop(AF_INET6, &(sa6.sin6_addr), ip6, INET6_ADDRSTRLEN);
printf("The address is: %s\n", ip6);
 ```

obviously, these only work with IP number addresses, they won't work with hostnames like `www.youtube.com`, you'll need something we'll discover in the future named: `getaddrinfo()`


Now then, how to make system calls:
```C
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>

int getaddrinfo(const char *node, // e.g. "www.example.com" or IP
				const char *service, // e.g. "http" or port number
				const struct addrinfo *hints,
				struct addrinfo **res);
```

it returns back a pointer to a linkd list, in `res`, ans `hints` points to a struct of `addrinfo` with the relative info filled, this is an example of a server that listens to an IP at port 3490:

```C
int status;
struct addrinfo hints;
struct addrinfo *servinfo; // will point to the results

memset(&hints, 0, sizeof hints); // make sure the struct is empty
hints.ai_family = AF_UNSPEC;     // don't care IPv4 or IPv6
hints.ai_socktype = SOCK_STREAM; // TCP stream sockets
hints.ai_flags = AI_PASSIVE;     // fill in my IP for me

if ((status = getaddrinfo(NULL, "3490", &hints, &servinfo)) != 0) {
	fprintf(stderr, "gai error: %s\n", gai_strerror(status));
	exit(1);
}

// servinfo now points to a linked list of 1 or more
// struct addrinfos
// ... do everything until you don't need servinfo anymore ....

freeaddrinfo(servinfo); // free the linked-list
```

you can also use `getaddrinfo()` alongside some magic and `inet_ntop()` to get IP addresses:

```C
char ipstr[INET6_ADDRSTRLEN];
for (p = res; p != NULL; p = p->ai_next) {
void *addr;
struct sockaddr_in *ipv4;
struct sockaddr_in6 *ipv6;

if (p->ai_family == AF_INET) {
	ipv4 = (struct sockaddr_in *) p->ai_addr;
	addr = &(ipv4->sin_addr);
} else {
	ipv6 = (struct sockaddr_in6 *) p->ai_addr;
	addr = &(ipv6->sin6_addr);
}
inet_ntop(p->ai_family, addr, ipstr, sizeof(ipstr));
printf("%s\n", ipstr);
```

this is how a socket system call is done:

```C
int socket(int domain, int type, int protocol);
```

domain is either IPv4 or IPv6, type is about the socket type and the protocol is TCP or UDP, you could hardcode them, but one is advised to use constans like:
Domain: `PF_INET`, `PF_INET6`
Type: `SOCK_STREAM`, `SOCK_DGRAM`
Protocol: `0` for proper protocol, or call `getprotobyname()` to use a specified protocol

`AF_INET`, and `AF_INET6` are used in `sockaddr_in`, or `sockaddr_in6`, you could use the attribue `ai_family` and call it a day though:

```C
int s = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
```

this function will simply return a socket descriptor

this is the call for `bind()` which is used to associate a specific port with a socket:

```C
int bind(int sockfd, struct sockaddr *addr, int addrlen);
```

`sockfd` is the socket file descriptor than we get as a return value from the funciton `socket()`

you can use `AI_PASSIVE` for `ai_flags` but it would bind the socket to the local IP address, then you'd put NULL in `getaddrinfo()`, else don't use the flag and put a proper IP address in the parameter

know that all ports less than `1024` are reserved, you can use unused ones up to `65535`

the `connect()` call is the same as `bind()`:

```C
int connect(int sockfd, struct sockaddr *addr, int addrlen);
```

`addr` here contains the destination info; port and IP, `addrlen` is the length of the `addr` in bytes

both `connect()` and  and `bind()` return `-1` on error and set the global variable `errno` to the error's value

bind is about the local port, while connect is about the destination port

there's a fucntion that listens to calls and holds a queue of the calls, usually it's capped at 20, but you can set it:

```C
int listen(int sockfd, int backlog);
```

the queue is the number of calls that'll wait until to accept them

then accept will return a new soccket descriptor ready to do `send()` and `recv()` requests with the `connnect()`ed IP, the original socket descriptor will continue to `listen()` and  queue other calls:

```C
int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
```

`addr` is said to be a ptr to a `sockaddr_storage`, usually.

```C
getaddrinfo();
socket();
bind();
listen();
accept();
```

some code to demonstrate:

```C
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>

#define MYPORT "3490" // the port users will be connecting to
#define BACKLOG 10 // how many pending connections queue holds

int main(void)
{
	struct sockaddr_storage their_addr;
	socklen_t addr_size;
	struct addrinfo hints, *res;
	int sockfd, new_fd;
	// !! don't forget your error checking for these calls !!
	// first, load up address structs with getaddrinfo():
	
	memset(&hints, 0, sizeof hints);
	hints.ai_family = AF_UNSPEC; // use IPv4 or IPv6, whichever
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags = AI_PASSIVE; // fill in my IP for me
	
	getaddrinfo(NULL, MYPORT, &hints, &res);
	
	// make a socket, bind it, and listen on it:
	sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
	bind(sockfd, res->ai_addr, res->ai_addrlen);
	listen(sockfd, BACKLOG);

	// now accept an incoming connection:	
	addr_size = sizeof their_addr;
	new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &addr_size);
	
	// ready to communicate on socket descriptor new_fd!
	.
	.
	.
}
```


programs will sleep while waiting for `recv()` and `send()`, which are used for stream sockets or connected datagram sockets, unconnected datagrams sockets use `sendto()` and `recvfrom()`

```C
int send(int sockfd, const void *msg, int len, int flags);
```

`sockfd` here is the one you'll send to, `msg` is the pointer to what you want to send, `void` in it is a plalceholder, it could be anything, and `len` is it's length in bytes, and this function will return the number of bytes sent which might be less than `len`, ` -1` is returned and `errno` is set on error

```C
int recv(int sockfd, void *buf, int len, int flags);
```

`sockfd` is to read from, this will return `-1` on error, and `0` on disconnection from the other end

as mentioned before, unconnected datagram sockets use these:

```C
int sendto(int sockfd, const void *msg, int flags, unsigned int flag, struct sockaddr *to, socklen_t tolen);
```

```C
int recvfrom(int sockfd, void *buf, unsigned int flags, struct sockaddr *from, int *fromlen);
```


when you're done with a socket, close it and free the linked list that is `getaddrinfo()`:

```C
close(sockfd);
```

this closes it both ways, for more control use:

```C
int shutdown(int sockfd, int how);
```

| `how` | Effect                                                   |
| ----- | -------------------------------------------------------- |
| `0`   | Further receives are disallowed                          |
| `1`   | Further sends are disallowed                             |
| `2`   | Further sends and receives are disallowed (like close()) |

it return `0` on success, and `-1` on error, with errno set accordingly

know that shutdown only changes the usability of the socket, only `close()` closes it appropriatly

```C
int getpeername(int sockfd, struct sockaddr *addr, int *addrlen);
```

this will return the network address so you could use `inet_ntop()` and then use `getnameinfo()` or `gethostbyaddr()`

```C
#include <unistd.h>
int gethostname(char *hostname, size_t size);
```

this function is to get the name of the machine on which the script runs, then you get use `getaddrinfo()` to get the IP address
The arguments are simple: `hostname` is a pointer to an array of chars that will contain the `hostname` upon the function’s return, and `size` is the length in bytes of the `hostname` array.

Please refer to `https://github.com/Eyad-Jawad/Serverless-Data-Communiacator.git`  for implementation of server and client using TCP 

In UDP you'd need a listener that await for a connection, and it is the same in TCP, `getaddrinfo()`, `socket()`, `bind()`, and then `recvfrom()` and that's it! But remember to substitute `hints.ai_socktype = SOCK_STREAM`  to `SOCK_DGRAM`
Same with the talker which represents the server here, it starts with `getaddrinfo()`, `socket()`,  and then `sendto()` and that's it! If you do connect then you can use `send()` and `recv()` not `sendto()` or `recvfrom()`

many functions do `blocking`, that is, they are set to sleep until data arrive, like socket descriptors, `accept()` and all of `recv()`, you can set it otherwise:

```C
#include <unistd.h>
#include <fcntl.h>

sockfd = socket(PF_INET, SOCK_STREAM, 0);
fcntl(sockfd, F_SETFL, O_NOBLOCK);
```

By setting a socket to non-blocking, you can effectively “poll” the socket for information. If you try to read from a non-blocking socket and there’s no data there, it’s not allowed to block— it will return `-1` and `errno` will be set to `EAGAIN` or `EWOULDBLOCK`.

`poll()` is used to monitor sockets and see which one is ready to recive data, it is ineffecient when there are a lot of connections so you're ought to use `libevent` library

```C

#include <poll.h>

struct pollfd {
	int fd;        // the socket descriptor
	short events;  // bitmap of events we're interested in
	short revents; // on return, bitmap of events that occurred
};

int poll(struct pollfd fds[], nfds_t nfds, int timeout);
// you can pass timeout in ms, 
// or a negative value if you want to wait for ever

```

The events field is the bitwise-OR of the following:

| Macro   | Description                                                        |
| ------- | ------------------------------------------------------------------ |
| POLLIN  | Alert me when data is ready to `recv()` on this socket.            |
| POLLOUT | Alert me when I can `send()` data to this socket without blocking. |
| POLLHUP | Alert me when the remote closed the connection.                    |

then you can  check `revents` to check for the event:

```C

struct pollfd pfds[1];

pfds[0].fd = 0;
pfds[0].events = POLLIN;

numEvents = poll(pfds, 1, 2500);

if (numEvents == 0)
	printf("Poll timed out\n");
	
else if (pfds[0].revents & POLLIN)
	printf("Socket %d is ready to read", pfds[0].fd);
	
else
	printf("Error occurred: %d\n", pfds[0].revents);

```

if you want to delete an element, set `fd` to a negative value and `poll()` will ignore it

there's a function called `select()` that does a similar job to `poll()`, it monitors sockets and tells you if one of them is ready for reading, writing, or have raised an error, and it is also slow with big connections:

```C
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

int select(int numfds, fd_set *readfds, fd_set *writefds,
	fd_set *exceptfds, struct timeval *timeout);
	
```

if you want to know if a socket is ready to read, add `0` which is `STDIN` and the file descriptor to the set `readfds`, and `numfds` must be set to the highest `sockfd + 1`

when the function `select()` returns, you can check using one of these functions (`FD_ISSET()`) because the sets will be modified in respect:

![[Pasted image 20260704140733.png]]

```C

struct timeval {
	int tv_sec;  // seconds
	int tv_usec; // microseconds
};

```

use this struct to set a timelimit for the function, If you set the fields in your struct timeval to 0 , select() will timeout immediately, effectively polling all the file descriptors in your sets. If you set the parameter timeout to NULL, it will never timeout, and will wait until the first file descriptor is ready. Finally, if you don’t care about waiting for a certain set, you can just set it to NULL in the call to select()

Quick note to all you Linux fans out there: sometimes, in rare circumstances, Linux’s select() can return “ready-to-read” and then not actually be ready to read! This means it will block on the read() after the select() says it won’t! Why you little—! Anyway, the workaround solution is to set the O_NONBLOCK flag on the receiving socket so it errors with EWOULDBLOCK (which you can just safely ignore if it occurs). See the fcntl() reference page for more info on setting a socket to non-blocking.

you have grazed on `sendall()` so no introductions needed:

```C

#include <sys/types.h>
#include <sys/socket.h>

int sendall(int s, char *buf, int *len) {
	int total = 0;        // how many bytes we've sent
	int bytesleft = *len; // how many we have left to send
	int n;
	
	while(total < *len) {
		n = send(s, buf+total, bytesleft, 0);
		if (n == -1) { break; }
		total += n;
		bytesleft -= n;
	}
	
	*len = total; // return number actually sent here	
	return n==-1?-1:0; // return -1 on failure, 0 on success
}

```

if you want to send variable length data like `int`s or `float`s use data encapsulation, which there are libraries for that

you can use `htons()` or `ntohs()` for `int`, but not for `float`