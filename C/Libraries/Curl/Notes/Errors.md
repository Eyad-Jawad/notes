## Setup The Error Buffer

To set up the error buffer you don't need to do much:

```C

char buf[CURL_ERROR_SIZE];
curl_easy_setopt(curl, CURLOPT_ERRORBUFFER, buf);

```

And if an error occurs you can print `buf`