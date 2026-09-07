## Memory Struct

First you need a struct to write into:

```C

struct MemoryStruct {
	char *memory;
	size_t size;
};

```

## The Function

Then you need a function that is fed to the curl to handle the writing and the sort:

```C

size_t write_cb(char *contents, size_t size, size_t nmemb, void *userp) {
	size_t realsize = size * nmemb;
	struct MemoryStruct *mem = (struct MemoryStruct *) userp;
	
	char *ptr = realloc(mem->memory, mem->size + realsize + 1);
	if (!ptr) {
		printf("not enough memory (realloc failed, returned NULL)\n");
		return 0;
	}
	
	mem->memory = ptr;
	memcpy(&(mem->memory[mem->size]), contents, realsize);
	mem->size += realsize;
	mem->memory[mem->size] = 0;
	
	return realsize;
}

```

`write_cb`: `write callback`
`nmemb`: `number of members`: number of elements, and `size` is the size of each element
`userp`: `user pointer`: It points to the pointer of the user bellow

Then you should tell the curl how to do it:

```C
struct MemoryStruct chunk;
chunk.memory = malloc(1);
chunk.size = 0;

.
.
.

curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *) &chunk);

.
.
.

// after using chunk.memory
free(chunk.memory);

```

be careful of freeing `chunk.memory` before actually using it