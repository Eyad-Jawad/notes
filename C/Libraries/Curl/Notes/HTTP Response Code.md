## The Function

You should check on the HTTP response code when executing some curl code, and to do that call:

```C

long status = 0;
curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &status);

.
.
.
if (status == 200) { // Should be a success
	...
} else if (status == 429) { // Rate limit
	...
}
.
.
.

```
