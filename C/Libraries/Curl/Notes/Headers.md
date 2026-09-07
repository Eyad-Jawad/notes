## Functions

There are many headers but this is how it's done

```C

curl_easy_setopt(curl, CURLOPT_USERAGENT, "Mozilla/5.0");
curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

```

The first one sets the user agent while the second one tells the curl to follow the redirection