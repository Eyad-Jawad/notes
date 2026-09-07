CSS can be applied to a webpage in three main ways: inline, internal, or external.
Each method has its own use case, advantages, and limitations, and knowing when to use each one is essential for writing clean, efficient, and maintainable code.

Inline CSS is generally used for quick, one-off styles or to override other styles for a specific element. (where you directly write the style in the element)

/* a comment in CSS looks like a comment in 89C * /

Internal CSS is written within the `style` tags inside the `head` section of an HTML document. It applies styles to the entire page and is useful when you need to style a single document.

External CSS is written in a separate `.css` file and linked to the HTML document using the `link` element in the `head` section.
It allows you to style multiple pages consistently and is the preferred method in professional web development.

```css
#idName {
color : red;
}
```
the # symbol indicates that the targeted thing is an id
for classes however, we'd use :
```css
.box {
width: 100px;
height: 100px;
}
```

```css
selector {
  property: value;
}
```

to access states of elements:
```css
element:state {
}
```

for styling:
element : state
When you use these states to style your links, there is a specific order you need to write your CSS in: link, visited, hover, focus, then active

the meta viewport is very important gives the browser instructions on how to control the page's dimensions and scaling on different devices, particularly on mobile phones and tablets.
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
The meta viewport element also allows you to control whether users can zoom in and out of your web pages.
While it's possible to disable zooming with the `user-scalable=no` attribute, it's generally recommended to avoid this for accessibility reasons.

In CSS, the `width` and `height` properties are used to control the dimensions of elements on a webpage.
These properties can be defined in different units such as pixels (`px`), percentages (`%`), viewport units (`vw`, `vh`), and more.
The `min-width` and `min-height` properties specify the minimum width and height an element can be. Even if the content inside is smaller, the element won’t shrink below this value.
`max-width` and `max-height` are pretty clear at this point

CSS combinators are used to define the relationship between selectors in CSS. They help in selecting elements based on their relationship to other elements, which allows for more precise and efficient styling.
parent descendant {

}
ex:
figure img {

}

he child combinator (`>`) in CSS is used to select elements that are direct children of a specified parent element.
This combinator targets only elements with a specific parent, making your CSS rules more precise and preventing unintended styling of deeper nested elements.
parent child {

}

The next-sibling combinator (`+`) in CSS selects an element that immediately follows a specified sibling element. This combinator is useful when you want to apply styles to an element that directly follows another element, allowing for targeted styling based on the element's position relative to its siblings.
child + sibling {

}

Unlike the next-sibling combinator, which targets only the immediately following sibling, the subsequent-sibling combinator (`~`) can target any siblings that follow the specified element, offering greater flexibility in styling.
h2 ~ p {

}

Block-level elements are elements that take up the full width available to them by default, stretching across the width of their container.
These elements always start on a new line and push other content to the next line, creating a "block" of content.
Block-level elements have the CSS property `display: block;` applied by default. This property ensures that the element stretches to fill the container's width and appears on a new line.
Some common block-level elements are `div` elements, paragraphs, headings, ordered lists, unordered lists, and section elements.

Inline elements, unlike block-level elements, only take up as much width as they need and do not start on a new line. These elements flow within the content, allowing text and other inline elements to appear alongside them.
Inline elements have the CSS property `display: inline;` applied by default. This property ensures that the element remains within the flow of the content and does not break onto a new line.
you can utilize this by saying <style></style> and then work with it as you'd work with a CSS file.
Common inline elements are `span`, `anchor`, and `img` elements.
Inline elements are best used for styling smaller portions of text or content within a line, such as emphasizing a word, creating hyperlinks, or applying specific styles to parts of a paragraph.
In short, the key difference between `inline` and `inline-block` is that `inline` elements cannot have their size controlled, whereas `inline-block` elements allow for full control over dimensions while still staying inline with other content.

Margins control the space outside an element, helping to separate it from other elements and define the layout structure, while padding controls the space inside an element, improving content readability and aesthetic appeal.
The four different `margin` properties are `margin-top`, `margin-right`, `margin-bottom` and `margin-left`.
When using a singular value on the `margin` shorthand, that exact value will be applied to all four sides of the target element.
When using two values, the first value applies to the `top` and `bottom`, while the second value applies to the `left` and `right` sides of the element.
margin: 20px 30px;
If three values are provided, the first value applies to the `top` margin, the second value to the `left` and `right` margin, and the third value to the `bottom` margin.
The first value targets the `top`, the second value targets the `right`, the third value targets the `bottom`, and the fourth value targets the `left`.
The `padding` property is used to apply space inside the element, between the content and its border.

Like the `margin` property, the four `padding` properties are `padding-top`, `padding-right`, `padding-bottom` and `padding-left`.
its shorthand is just the same as margin

you can set all of the above to `auto `and it'll center them ig

to link to something in the CSS file you should say:
property: url(https://somehing.com);

if you have some value you could say:
property: value1, value2;
which is a fallback, which are used in instances where the initial is not found/available.
