Skip to main content

* Translations

  + [English](#/ "English")
  + [简体中文](#/zh-cn/ "简体中文")

Clear search

`/`
`⌃K`

[docsify](#/)
=============

[Cover](#/cover?id=cover)
=========================

Activate the cover feature by setting `coverpage` to **true**. See [coverpage configuration](#/configuration?id=coverpage).

[Basic usage](#/cover?id=basic-usage)
-------------------------------------

Set `coverpage` to **true**, and create a `_coverpage.md`:

```
window.$docsify = {
  coverpage: true,
};
```

```
<!-- _coverpage.md -->

![logo](_media/icon.svg)

# docsify

> A magical documentation site generator

- Simple and lightweight
- No statically built HTML files
- Multiple themes

[GitHub](https://github.com/docsifyjs/docsify/)
[Get Started](#docsify)
```

[Customization](#/cover?id=customization)
-----------------------------------------

The cover page can be customized using [theme properties](#/themes?id=theme-properties):

```
:root {
  --cover-bg         : url('path/to/image.png');
  --cover-bg-overlay : rgba(0, 0, 0, 0.5);
  --cover-color      : #fff;
  --cover-title-color: var(--theme-color);
  --cover-title-font : 600 var(--font-size-xxxl) var(--font-family);
}
```

Alternatively, a background color or image can be specified in the cover page markdown.

```
<!-- background color -->

![color](#f0f0f0)
```

```
<!-- background image -->

![](_media/bg.png)
```

[Coverpage as homepage](#/cover?id=coverpage-as-homepage)
---------------------------------------------------------

Normally, the coverpage and the homepage appear at the same time. Of course, you can also separate the coverpage by [`onlyCover`](#/configuration?id=onlycover) option.

[Multiple covers](#/cover?id=multiple-covers)
---------------------------------------------

If your docs site is in more than one language, it may be useful to set multiple covers.

For example, your docs structure is like this

```
.
└── docs
    ├── README.md
    ├── guide.md
    ├── _coverpage.md
    └── zh-cn
        ├── README.md
        └── guide.md
        └── _coverpage.md
```

Now, you can set

```
window.$docsify = {
  coverpage: ['/', '/zh-cn/'],
};
```

Or a special file name

```
window.$docsify = {
  coverpage: {
    '/': 'cover.md',
    '/zh-cn/': 'cover.md',
  },
};
```

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/cover.md)