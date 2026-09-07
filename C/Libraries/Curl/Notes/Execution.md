# The Function

After you have called all the function and set all the configs, you need only call:

```C

CURLcode res = curl_easy_perform(curl);

```

But you also need to check for errors, in this case you should only be concerned with `res`:

```C

if (res != CURLE_OK) {
	printf("curl_easy_perform() failed: %s\n", errorBuffer);
	/* cleanup */
	return NULL;
}

```

If you want (or should) you can also check the HTTP response code, becuase it can also indicate an error: [[HTTP Response Code]]
