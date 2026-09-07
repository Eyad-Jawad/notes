you already know ho w to use tags, so know this:
<!DOCTYPE html>All pages should begin with <!DOCTYPE html>. This special string is known as a declaration and ensures the browser tries to meet industry-wide specifications.
<html> The html element is the root element of an HTML page and wraps all content on the page. you can add a lang="en" attribute to indicate that the language of the page is English
<h1>: for huge header
<h2>: for subheading
all the way to <h6>
<head> The head element is used to contain metadata about the document, such as its title, links to stylesheets, and scripts. Metadata is information about the page that isn't displayed directly on the page.
<body> All page content elements that should be rendered to the page go inside the body element.
<p>: for paragraph
<img, src="" alt=""> this tag is used to show images, the attribute src is for the source of the image, and the attribute alt is a description, it's a good practice to add one to every image.
<input/> for input, 
	attributes:
		type= "checkbox" shows a todo-list-like box, you can add another attribute:
			checked: which adds the box checked automatically

<a href="" target=""> also known as an anchor element for linked texts, to open links in a new tab, you can use the target="_blank" attribute on the anchor (a) element.
	This first example uses the href and target attributes. The href attribute specifies the URL of a link and the target attribute specifies where to open the link. You use a link for href="", and target="_blank" enables the link to open in a new browser tab.
<link rel="" href=""> The link element is used to link to external resources like stylesheets and site icons. Here is the basic syntax for using the `link` element for an external CSS file
	rel="stylesheet" to indicate that the relationship is a CSS stylesheet
	href="./styles.css" the . and / is to indicate that the file is in the current directory/folder
	rel="preconnect" value for the attribute tells the browser to create an early connection to the value specified in the href attribute.	
	rel="icon" this one is clear
<script> // is used to run code, usually JS, I had to close it  and put a comment to avoid running an actual script lol, you should say src="path.js"</script>
<main> HTML5 has some elements that identify different content areas. These elements make your HTML easier to read and help with Search Engine Optimization (SEO) and accessibility.
The main element is used to represent the main content of the body of an HTML document. Content inside the main element should be unique to the document and should not be repeated in other parts of the document.
<section> The section element is used to define sections in a document, such as chapters, headers, footers, or any other sections of the document. It is a semantic element that helps with SEO and accessibility.
<hr /> element which creates a horizontal rule often used to visually separate sections of content.
<br /> makes a newline
<Blockquotes> are used to indicate a section of text that is a quotation from another source. Browsers typically add indentation and sometimes italicize the text.
<div> A container element for other elements (generally for shared CSS)
<id> A reference the style sheet can use, put in any element: id=""
<class> same as id, diff listed below
<ul> To create an unordered list of items, you can use the ul element.
<li> The li element is used to create a list item in an ordered or unordered list.
<button class="btn"> A button that can be clicked
<figure> The figure element represents self-contained content and will allow you to associate an image with a caption.
<figcaption> A figure caption (figcaption) element is used to add a caption to describe the image contained within the figure element.
<ol> The code for an ordered list (ol) is similar to an unordered list, but list items in an ordered list are numbered when displayed.
<em> To place emphasis on a specific word or phrase, you can use the em element (italic)
<strong> The strong element is used to indicate that some text is of strong importance or urgent (bold)
<footer> The footer element is used to define a footer for a document or section. A footer typically contains information about the author of the document, copyright data, links to terms of use, contact information, and more.

What distinguishes an opening tag from a closing tag is the forward slash (`/`) placed immediately after the left angle bracket in a closing tag. Some HTML elements do not have a closing tag. These are known as void elements. like:
<img>, some people add a / at the end of the tag to indicate that it is void, but it is unnecessary 
HTML boilerplate is like a ready-made template for your webpages. For example:
<!DOCTYPE html> <!-- it tells the browser which html version this is-->
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
  </body>
</html>

The head section contains important behind-the-scenes information (like the stylesheet):
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document Title Goes Here</title>
  <link rel="stylesheet" href="./styles.css" />
</head>

UTF-8 supports every character in the Unicode character set - and this includes characters and symbols from all writing systems, languages, and technical symbols. Here is an example of using the meta element with the charset attribute to set the character encoding to UTF-8:
<meta charset="UTF-8" />
Here is an extended code example of using the UTF-8 character encoding:
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Examples of the UTF-8 encoding</title>
  </head>
  <body>
    <p>Café</p>
  </body>
</html>

you should be careful not to overuse div, sometimes section is better, section has a semantic meaning for browsers to know, while div doesn't have one

an id must be unique, and not have spaces, a class however can have spaces, a space indicates a new style, it can be used to group many styles at once into a single element
you shouldn't use an id more than once in the html file, it'll do weird stuff for the JS, you could use a class many times though
By using a named character reference, the HTML parser will not confuse this with an actual HTML element. EX:
&#60; will be shown as <        > I had to close it so it doesn't mess up the editor
there are three types of it: Named, Decimal numeric, and Hexadecimal numeric character references.

SEO, or Search Engine Optimization, is a practice that optimizes web pages so they become more visible and rank higher on search engines. One way to improve your site's SEO, is to provide a short description for the web page using the meta element. by using the name="" and content="" attributes 
One place where the page description can be found is in the search engine results page snippet.

The open graph protocol enables you to control how your website's content appears across various social media platforms
The first important OG property to include would be the title:
<meta content="EyadJawad.com" property="og:title" />

The next important OG property would be the `type`. Here is an example of using the OG `type` for the freeCodeCamp homepage:
<meta property="og:type" content="website" />

The third important OG property would be the image. Here is an example of setting the OG image for the freeCodeCamp homepage:
<meta
  content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
  property="og:image"
/>

The fourth important OG property would be the url:
<meta property="og:url" content="https://www.EyadJawad.com" />

There are many more OG properties that you can set, like description, audio, video and locale. However, the open graph url, image, type, and title are the most important ones to include.

The audio and video elements allow you to add sound and video content to your HTML documents. The audio element supports popular audio formats like mp3, wav, and ogg. The video element supports mp4, ogg, and webm formats.
<audio
	src=""
	controls
	loop
	muted
></audio>

When it comes to audio file types, there are differences in which browsers support which type. To accommodate this, you can use source elements inside the audio element and the browser will select the first source that it understands. Here's an example of using multiple source elements for an audio element:
<audio controls>
  <source src="audio.ogg" type="audio/ogg" />
  <source src="audio.wav" type="audio/wav" />
  <source src="audio.mp3" type="audio/mpeg" />
</audio>

<video
	src=""
	controls
	loop
	autoplay
	muted
	poster=""
	width=""
></video>
you could also use the same things as in audio

There are three tools to consider when using media, such as images, on your web pages: the size, the format, and the compression.
 When you are building a website, you'll often style images to display in a specific size. If you serve an image that is 1920x1080 but you are styling it to be much smaller, you're requiring your users to download unnecessary data. A smaller resolution results in a smaller file size.
 The next thing to consider is your file format. Two of the most common file formats are PNG and JPG, but these are no longer the most ideal formats for serving images. Unless you need support for older browsers, you should consider using a more optimized format, like WEBP or AVIF.
 Finally, you can run compression algorithms on your images. A compression algorithm is used to reduce the size for files or data. There are options like pngcrush to compress your images locally, or you can use online compression tools.

put copyrights in mind when using media unless it's posted on a public domain it may have a license or something
SVG stands for a scalable vector graphic. EX:
<!-- Star Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="gold" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2L14.9 8.6L22 9.3L17 14.1L18.3 21.2L12 17.8L5.7 21.2L7 14.1L2 9.3L9.1 8.6L12 2Z"/>
</svg>
<!-- Heart Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="crimson" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 21.35L10.55 20.03C5.4 15.36 2 12.28 2 8.5C2 6 4 4 6.5 4C8 4 9.5 4.8 10.5 6.09C11.5 4.8 13 4 14.5 4C17 4 19 6 19 8.5C19 12.28 15.6 15.36 10.45 20.04L12 21.35Z"/>
</svg>
<!-- Checkmark Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="green" xmlns="http://www.w3.org/2000/svg">
  <path d="M20.29 5.71L9 17L3.71 11.71L5.12 10.29L9 14.17L18.88 4.29L20.29 5.71Z"/>
</svg>

One of the most popular icon libraries, Font Awesome, uses SVG images for their icons. SVGs are also great for webpage logos, because they scale perfectly. They allow you to adapt your layout to any responsive design you need. 

A replaced element is an element whose content is determined by an external resource rather than by CSS itself. CSS, or cascading stylesheets, is used to add styles to a web page
the iframe element, which embeds an external site on your web page.
<iframe width="" height="" title="" src=""> </iframe>
If you want to embed direct HTML within the iframe element you have to use the srcdoc attribute instead of src.

attrs:
allowfullscreen
for a YouTube link:
allow="accelerometer autoplay clipboard-write encrypted-media gyroscope web-share"
for safety:
referrerpolicy="strict-origin-when-cross-origin"
rel="noopener noreferrer"

There are four important possible values for this attribute. Note that each value is preceded by an underscore. (target="_blank)
The first value is _self, which is the default value. This opens the link in the current browsing context. In most cases, this will be the current tab or window.
The second value is _blank, which opens the link in a new browsing context. Typically, this will open in a new tab. But some users might configure their browsers to open a new window instead.
The third value is _parent, which opens the link in the parent of the current context. For example, if your website has an iframe, a _parent value in that iframe would open in your website's tab/window, not in the embedded frame.
The fourth value is _top, which opens the link in the top-most browsing context - think "the parent of the parent". This is similar to _parent, but the link will always open in the full browser tab/window, even for nested embedded frames.

So, which should you use and when: an absolute path, an absolute URL, or a relative path? Here are the rules you should follow:
Use absolute paths when you want to reference a resource from a fixed location, such as from the root of your site or a known directory on your local machine.
Use absolute URL when linking to a resource hosted on an external website.
Use relative paths when linking to resources within the same website.
Use relative paths if you want to keep your code cleaner and easier to maintain during development.
Use relative paths during local testing to ensure links work without an internet connection.

A single dot points to the current directory, and two dots point to the parent directory.

[HTML basics review]( https://www.freecodecamp.org/learn/responsive-web-design-v9/review-basic-html/basic-html-review )

<article>: specifies independent, self-contained content. An article should make sense on its own and it should be possible to distribute it independently from the rest of the site.