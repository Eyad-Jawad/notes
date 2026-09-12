The syntax involves two elements:
1. `{% keyword %}
2. `{{ variable }}`

Some basic ones:

#### If

```HTML

{% if title %}
	<title> site {{ title }} </title>
{% else %}
	<title> site </title>
{% endif %}

```

#### For

```HTML

{% for x in agrs %}
	<h1> {{ x }} </h1>
{% endfor %}

```

There's also the `block` keyword which is used in [[Inheritance]]