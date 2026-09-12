In jinja you'd write the `HTML` code then pass in the `JSON` to the `jijna` engine and it handles the rest:

```Python

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="directory_name_while_html_files_are")

@app.get("/route)
def route(request: Request):
	return templates.TemplateResponse(
		request,
		"the_file_to_be_served.html",
		{"args":"values"},
	)

```

And that's it, you can also pass to the decorator the name of it so you can do [[url_for|this]]
