Skip to main content

* Translations

  + [English](#/ "English")
  + [简体中文](#/zh-cn/ "简体中文")

Clear search

`/`
`⌃K`

[docsify](#/)
=============

* Getting started

  + [Quick start](#/quickstart "Quick start")
  + [Adding pages](#/adding-pages "Adding pages")
  + [Cover page](#/cover "Cover page")
  + [Custom navbar](#/custom-navbar "Custom navbar")
    - [HTML](#/custom-navbar?id=html "HTML")
    - [Markdown](#/custom-navbar?id=markdown "Markdown")
    - [Nesting](#/custom-navbar?id=nesting "Nesting")
    - [Combining custom navbars with the emoji plugin](#/custom-navbar?id=combining-custom-navbars-with-the-emoji-plugin "Combining custom navbars with the emoji plugin")
* Customization

  + [Configuration](#/configuration "Configuration")
  + [Themes](#/themes "Themes")
  + [List of Plugins](#/plugins "List of Plugins")
  + [Write a Plugin](#/write-a-plugin "Write a Plugin")
  + [Markdown configuration](#/markdown "Markdown configuration")
  + [Language highlighting](#/language-highlight "Language highlighting")
  + [Emoji](#/emoji "Emoji")
* Guide

  + [Deploy](#/deploy "Deploy")
  + [Helpers](#/helpers "Helpers")
  + [Vue compatibility](#/vue "Vue compatibility")
  + [CDN](#/cdn "CDN")
  + [Offline Mode (PWA)](#/pwa "Offline Mode (PWA)")
  + [Embed Files](#/embed-files "Embed Files")
  + [UI Kit](#/ui-kit "UI Kit")
* Upgrading

  + [v4 to v5](#/v5-upgrade "v4 to v5")

* [Awesome docsify](#/awesome "Awesome docsify")
* [Changelog](#/changelog "Changelog")

[Custom navbar](#/custom-navbar?id=custom-navbar)
=================================================

[HTML](#/custom-navbar?id=html)
-------------------------------

If you need custom navigation, you can create a HTML-based navigation bar.

Note that documentation links begin with `#/`.

```
<!-- index.html -->

<body>
  <nav>
    <a href="#/">EN</a>
    <a href="#/zh-cn/">简体中文</a>
  </nav>
  <div id="app"></div>
</body>
```

[Markdown](#/custom-navbar?id=markdown)
---------------------------------------

Alternatively, you can create a custom markdown-based navigation file by setting `loadNavbar` to **true** and creating `_navbar.md`, compare [loadNavbar configuration](#/configuration?id=loadnavbar).

```
<!-- index.html -->

<script>
  window.$docsify = {
    loadNavbar: true,
  };
</script>
<script src="//cdn.jsdelivr.net/npm/docsify@5/dist/docsify.min.js"></script>
```

```
<!-- _navbar.md -->

- [En](/)
- [chinese](/zh-cn/)
```

To create drop-down menus:

```
<!-- _navbar.md -->

- Translations

  - [En](/)
  - [chinese](/zh-cn/)
```

You need to create a `.nojekyll` in `./docs` to prevent GitHub Pages from ignoring files that begin with an underscore.

`_navbar.md` is loaded from each level directory. If the current directory doesn't have `_navbar.md`, it will fall back to the parent directory. If, for example, the current path is `/guide/quick-start`, the `_navbar.md` will be loaded from `/guide/_navbar.md`.

[Nesting](#/custom-navbar?id=nesting)
-------------------------------------

You can create sub-lists by indenting items that are under a certain parent.

```
<!-- _navbar.md -->

- Getting started

  - [Quick start](quickstart.md)
  - [Writing more pages](more-pages.md)
  - [Custom navbar](custom-navbar.md)
  - [Cover page](cover.md)

- Configuration

  - [Configuration](configuration.md)
  - [Themes](themes.md)
  - [Using plugins](plugins.md)
  - [Markdown configuration](markdown.md)
  - [Language highlight](language-highlight.md)
```

renders as

![Nesting navbar](/_images/nested-navbar.png "Nesting navbar")

[Combining custom navbars with the emoji plugin](#/custom-navbar?id=combining-custom-navbars-with-the-emoji-plugin)
-------------------------------------------------------------------------------------------------------------------

If you use the [emoji plugin](#/plugins?id=emoji):

```
<!-- index.html -->

<script>
  window.$docsify = {
    // ...
  };
</script>
<script src="//cdn.jsdelivr.net/npm/docsify@5/dist/docsify.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/docsify@5/dist/plugins/emoji.min.js"></script>
```

you could, for example, use flag emojis in your custom navbar Markdown file:

```
<!-- _navbar.md -->

- [:us:, :uk:](/)
- [:cn:](/zh-cn/)
```

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/custom-navbar.md)