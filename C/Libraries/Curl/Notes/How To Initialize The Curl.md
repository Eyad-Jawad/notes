## The Variable

First you need to declare the curl variable itself:

```C
#include <curl/curl.h>

CURL *curl;
curl = curl_easy_init();

```

But before that you need to initialize the global curl first:

```C

CURLcode res;
res = curl_global_init(CURL_GLOBAL_ALL);

if (res != CURLE_OK) {
	...
}

```
## The Link/Website 

To provide curl with the website you want to "curl" or scrape, call this:

```C

curl_easy_setopt(curl, CURLOPT_URL, url);

```

And that's it, the `url` needs to be a `char *` though

## Cleanup

Then after you finished using it call:

```C

curl_easy_cleanup(curl);
curl_global_cleanup();

```