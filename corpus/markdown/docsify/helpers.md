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
    - [Callouts](#/helpers?id=callouts "Callouts")
    - [Link attributes](#/helpers?id=link-attributes "Link attributes")
    - [Task lists](#/helpers?id=task-lists "Task lists")
    - [Images](#/helpers?id=images "Images")
    - [Heading IDs](#/helpers?id=heading-ids "Heading IDs")
    - [Markdown + HTML](#/helpers?id=markdown--html "Markdown + HTML")
  + [Vue compatibility](#/vue "Vue compatibility")
  + [CDN](#/cdn "CDN")
  + [Offline Mode (PWA)](#/pwa "Offline Mode (PWA)")
  + [Embed Files](#/embed-files "Embed Files")
  + [UI Kit](#/ui-kit "UI Kit")
* Upgrading

  + [v4 to v5](#/v5-upgrade "v4 to v5")

* [Awesome docsify](#/awesome "Awesome docsify")
* [Changelog](#/changelog "Changelog")

[Doc helper](#/helpers?id=doc-helper)
=====================================

docsify extends Markdown syntax to make your documents more readable.

> Note: For the special code syntax cases, it's better to put them within code backticks to avoid any conflict from configurations or emojis.

[Callouts](#/helpers?id=callouts)
---------------------------------

Docsify supports [GitHub style](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts) callouts (also known as "admonitions" or "alerts").

**Caution** callouts communicate negative potential consequences of an action.

**Important** callouts communicate information necessary for users to succeed.

**Note** callouts communicate information that users should take into account.

**Tip** callouts communicate optional information to help a user be more successful.

**Warning** callouts communicate potential risks user should be aware of.

**Markdown**

```
> [!CAUTION]
> **Caution** callouts communicate negative potential consequences of an action.

> [!IMPORTANT]
> **Important** callouts communicate information necessary for users to succeed.

> [!NOTE]
> **Note** callouts communicate information that users should take into account.

> [!TIP]
> **Tip** callouts communicate optional information to help a user be more successful.

> [!WARNING]
> **Warning** callouts communicate potential risks user should be aware of.
```

### [Legacy Style ⚠️](#/helpers?id=legacy-style-)

The following Docsify v4 callout syntax has been deprecated and will be removed in a future version.

Legacy **Important** callouts are deprecated.

Legacy **Tip** callouts are deprecated.

**Markdown**

```
!> Legacy **Important** callouts are deprecated.

?> Legacy **Tip** callouts are deprecated.
```

[Link attributes](#/helpers?id=link-attributes)
-----------------------------------------------

### [disabled](#/helpers?id=disabled)

```
[link](/demo ':disabled')
```

### [href](#/helpers?id=href)

Sometimes we will use some other relative path for the link, and we have to tell docsify that we don't need to compile this link. For example:

```
[link](/demo/)
```

It will be compiled to `<a href="/#/demo/">link</a>` and will load `/demo/README.md`. Maybe you want to jump to `/demo/index.html`.

Now you can do that

```
[link](/demo/ ':ignore')
```

You will get `<a href="/demo/">link</a>`html. Do not worry, you can still set the title for the link.

```
[link](/demo/ ':ignore title')

<a href="/demo/" title="title">link</a>
```

### [target](#/helpers?id=target)

```
[link](/demo ':target=_blank')
[link](/demo2 ':target=_self')
```

[Task lists](#/helpers?id=task-lists)
-------------------------------------

```
- [ ] foo
- bar
- [x] baz
- [] bam <~ not working
  - [ ] bim
  - [ ] lim
```

* foo
* bar
* baz
* [] bam <~ not working
  + bim
  + lim

[Images](#/helpers?id=images)
-----------------------------

### [Class names](#/helpers?id=class-names)

```
![logo](https://docsify.js.org/_media/icon.svg ':class=someCssClass')

<!-- Multiple class names -->

![logo](https://docsify.js.org/_media/icon.svg ':class=someCssClass :class=anotherCssClass')
```

### [IDs](#/helpers?id=ids)

```
![logo](https://docsify.js.org/_media/icon.svg ':id=someCssId')
```

### [Sizes](#/helpers?id=sizes)

```
![logo](https://docsify.js.org/_media/icon.svg ':size=WIDTHxHEIGHT')
![logo](https://docsify.js.org/_media/icon.svg ':size=50x100')
![logo](https://docsify.js.org/_media/icon.svg ':size=100')

<!-- Support percentage -->

![logo](https://docsify.js.org/_media/icon.svg ':size=10%')
```

![logo](https://docsify.js.org/_media/icon.svg)
![logo](https://docsify.js.org/_media/icon.svg)
![logo](https://docsify.js.org/_media/icon.svg)

[Heading IDs](#/helpers?id=heading-ids)
---------------------------------------

```
### Hello, world! :id=hello-world
```

[Markdown + HTML](#/helpers?id=markdown--html)
----------------------------------------------

You need to insert a space between the html and markdown content.
This is useful for rendering markdown content in the details element.

```
<details>
<summary>Self-assessment (Click to expand)</summary>

- Abc
- Abc

</details>
```

Self-assessment (Click to expand)

* Abc
* Abc

Markdown content can also be wrapped in html tags.

```
<div style='color: red'>

- listitem
- listitem
- listitem

</div>
```

* listitem
* listitem
* listitem

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/helpers.md)