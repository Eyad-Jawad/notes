You can set some surronding code to be wrapped in `HTML` code in `jinja` to make things eaiser, first the parent file:

```HTML

<!-- parent.html --->

<h1>Some contect</h1>

{% block blockname %}
{% endblock blockname %}

```

Then the child file:

```HTML

{% extends "parent.html" %}
{% block blockname %}
	
	<h1>Some boilprete</h1>
	
{% endblock blockname %}

```
