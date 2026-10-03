Skip to main content

* Translations

  + [English](#/ "English")
  + [简体中文](#/zh-cn/ "简体中文")

Clear search

`/`
`⌃K`

[docsify](#/)
=============

[Language highlighting](#/language-highlight?id=language-highlighting)
======================================================================

[Prism](#/language-highlight?id=prism)
--------------------------------------

Docsify uses [Prism](https://prismjs.com) for syntax highlighting within code blocks. Prism supports the following languages by default (additional [language support](#/language-highlight?id=language-support) also available):

* Markup: HTML, XML, SVG, MathML, SSML, Atom, RSS
* CSS
* C-like
* JavaScript

To enable syntax highlighting, create a markdown codeblock using backticks (```` ``` ````) with a [language](https://prismjs.com/#supported-languages) specified on the first line (e.g., `html`, `css`, `js`):

```
```html
<p>This is a paragraph</p>
<a href="//docsify.js.org/">Docsify</a>
```
```

```
```css
p {
  color: red;
}
```
```

```
```js
function add(a, b) {
  return a + b;
}
```
```

The above markdown will be rendered as:

```
<p>This is a paragraph</p>
<a href="//docsify.js.org/">Docsify</a>
```

```
p {
  color: red;
}
```

```
function add(a, b) {
  return a + b;
}
```

[Language support](#/language-highlight?id=language-support)
------------------------------------------------------------

Support for additional [languages](https://prismjs.com/#supported-languages) is available by loading the Prism [grammar files](https://cdn.jsdelivr.net/npm/prismjs@1/components/):

Prism grammar files must be loaded after Docsify.

```
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-bash.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-docker.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-git.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-java.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-jsx.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-markdown.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-php.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-python.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-rust.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-sql.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-swift.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-typescript.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-yaml.min.js"></script>
```

[Theme support](#/language-highlight?id=theme-support)
------------------------------------------------------

Docsify's official [themes](#/themes) are compatible with Prism syntax highlighting themes.

Prism themes must be loaded after Docsify themes.

```
<!-- Light and dark mode -->
<link
  rel="stylesheet"
  href="//cdn.jsdelivr.net/npm/prism-themes@1/themes/prism-one-light.min.css"
/>
```

Themes can be applied in light and/or dark mode

```
<!-- Dark mode only -->
<link
  rel="stylesheet"
  media="(prefers-color-scheme: dark)"
  href="//cdn.jsdelivr.net/npm/prism-themes@1/themes/prism-one-dark.min.css"
/>

<!-- Light mode only -->
<link
  rel="stylesheet"
  media="(prefers-color-scheme: light)"
  href="//cdn.jsdelivr.net/npm/prism-themes@1/themes/prism-one-light.min.css"
/>
```

The following Docsify [theme properties](#/themes?id=theme-properties) will override Prism theme styles by default:

```
--border-radius
--font-family-mono
--font-size-mono
```

To use the values specified in the Prism theme, set the desired theme property to `unset`:

```
<style>
  :root {
    --border-radius   : unset;
    --font-family-mono: unset;
    --font-size-mono  : unset;
  }
</style>
```

[Dynamic content](#/language-highlight?id=dynamic-content)
----------------------------------------------------------

Dynamically generated Code blocks can be highlighted using Prism's [`highlightElement()`](https://prismjs.com/docs/Prism.html#.highlightElement) method:

```
const code = document.createElement('code');
code.innerHTML = "console.log('Hello World!')";
code.setAttribute('class', 'language-javascript');
Prism.highlightElement(code);
```

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/language-highlight.md)