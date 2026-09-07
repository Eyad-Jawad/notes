### fprintf

If you call fprintf with a string you don't know about, you should call it like this:

```C

fprintf(file, "%s", str);

```

because if the string has some formatting characters bad things will happen, in this specific case you should call `fputs`

### buffer_len < alloc_len

Sometimes the length of the string can be smaller than the length of the allocated string, this happens when `'\0'` is present before the actual end of the allocated memory, which is quite normal. This allows some interesting functions like this one which removes occurrences of `<p>` and replaces `</p>` with `'\n'`:

```C

void cleanChapter(char *txtChapter) {
	char *src = txtChapter;
	char *dst = txtChapter;

	while (*src) {
		if (strncmp(src, "<p>", 3) == 0) {
			src += 3;
		} else if (strncmp(src, "</p>", 4) == 0) {
			*dst++ = '\n';
			src += 4;
		} else {
			*dst++ = *src++;
		}
	} 
	*dst = '\0';
}

```

### Sleep

The function `sleep` which is very useful, lives in `unistd.h` and takes seconds as an arugment