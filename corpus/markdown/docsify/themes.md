Skip to main content

* Translations

  + [English](#/ "English")
  + [简体中文](#/zh-cn/ "简体中文")

Clear search

`/`
`⌃K`

[docsify](#/)
=============

[Themes](#/themes?id=themes)
============================

[Core theme](#/themes?id=core-theme)
------------------------------------

The Docsify "core" theme contains all of the styles and [theme properties](#/themes?id=theme-properties) needed to render a Docsify site. This theme is designed to serve as a minimalist theme on its own, in combination with [theme add-ons](#/themes?id=theme-add-ons), modified using core [classes](#/themes?id=classes), and as a starting point for [customization](#/themes?id=customization).

```
<!-- Core Theme -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@5/dist/themes/core.min.css" />
```

[Theme add-ons](#/themes?id=theme-add-ons)
------------------------------------------

Theme add-ons are used in combination with the [core theme](#/themes?id=core-theme). Add-ons contain CSS rules that modify [theme properties](#/themes?id=theme-properties) values and/or add custom style declarations. They can often (but not always) be used with other add-ons.

Theme add-ons must be loaded after the [core theme](#/themes?id=core-theme).

```
<!-- Core Theme -->
<link rel="stylesheet" href="..." />

<!-- Theme (add-on) -->
<link rel="stylesheet" href="..." />
```

### [Core Dark (Add-on)](#/themes?id=core-dark-add-on)

Dark mode styles for the [core theme](#/themes?id=core-theme). Styles can applied only when an operating system's dark mode is active by specifying a `media` attribute.

Preview Core Dark
  


Preview Core Dark (Dark Mode Only)

```
<!-- Core Dark (add-on) -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@5/dist/themes/addons/core-dark.min.css" />
```

```
<!-- Core Dark - Dark Mode Only (add-on) -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@5/dist/themes/addons/core-dark.min.css" media="(prefers-color-scheme: dark)" />
```

### [Vue theme (Add-on)](#/themes?id=vue-theme-add-on)

The popular Docsify v4 theme.

Preview Vue

```
<!-- Vue Theme (add-on) -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@5/dist/themes/addons/vue.min.css" />
```

[Classes](#/themes?id=classes)
------------------------------

The [core theme](#/themes?id=core-theme) provides several CSS classes for customizing your Docsify site. These classes should be applied to the `<body>` element within your `index.html` page.

```
<body class="...">
```

### [Loading](#/themes?id=loading)

Display a loading animation while waiting for Docsify to initialize.

```
<body class="loading">
```

### [Sidebar chevrons](#/themes?id=sidebar-chevrons)

Display expand/collapse icons on page links in the sidebar.

 Preview `sidebar-chevron-right`
  

 Preview `sidebar-chevron-left`

```
<body class="sidebar-chevron-right">
```

```
<body class="sidebar-chevron-left">
```

To prevent chevrons from displaying for specific page links, add a `no-chevron` class as follows:

```
[My Page](page.md ':class=no-chevron')
```

**Theme properties**

```
:root {
  --sidebar-chevron-collapsed-color: var(--color-mono-3);
  --sidebar-chevron-expanded-color : var(--theme-color);
}
```

### [Sidebar groups](#/themes?id=sidebar-groups)

Add visual distinction between groups of links in the sidebar.

 Preview `sidebar-group-box`
  

 Preview `sidebar-group-underline`

```
<body class="sidebar-group-box">
```

```
<body class="sidebar-group-underline">
```

### [Sidebar link clamp](#/themes?id=sidebar-link-clamp)

Limit multi-line sidebar links to a single line followed by an ellipses.

Preview `sidebar-link-clamp`

```
<body class="sidebar-link-clamp">
```

### [Sidebar toggle](#/themes?id=sidebar-toggle)

Display a "hamburger" icon (three lines) in the sidebar toggle button instead of the default "kebab" icon.

Preview `sidebar-toggle-chevron`
  


Preview `sidebar-toggle-hamburger`

```
<body class="sidebar-toggle-chevron">
```

```
<body class="sidebar-toggle-hamburger">
```

[Customization](#/themes?id=customization)
------------------------------------------

Docsify provides [theme properties](#/themes?id=theme-properties) for simplified customization of frequently modified styles.

1. Add a `<style>` tag after the theme stylesheet in your `index.html`.

   ```
   <!-- Theme -->
   <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@5/dist/themes/core.min.css" />

   <!-- Custom theme styles -->
   <style>
     :root {
       /* ... */
     }
   </style>
   ```

   Theme properties can also be set on a per-page basis in markdown.

   ```
   # My Heading

   Hello, World!

   <style>
     :root {
       /* ... */
     }
   </style>
   ```
2. Set custom [theme properties](#/themes?id=theme-properties) within a `:root` declaration.

   ```
   :root {
     --theme-color: red;
     --font-size  : 15px;
     --line-height: 1.5;
   }
   ```

   Custom [theme properties](#/themes?id=theme-properties) can be conditionally applied in light and/or dark mode.

   ```
   /* Light and dark mode */
   :root {
     --theme-color: pink;
   }

   /* Light mode only */
   @media (prefers-color-scheme: light) {
     :root {
       --color-bg  : #eee;
       --color-text: #444;
     }
   }

   /* Dark mode only */
   @media screen and (prefers-color-scheme: dark) {
     :root {
       --color-bg  : #222;
       --color-text: #ddd;
     }
   }
   ```
3. Custom fonts can be used by adding web font resources and modifying `--font-family` properties as needed:

   ```
   /* Fonts: Noto Sans, Noto Emoji, Noto Mono */
   @import url('https://fonts.googleapis.com/css2?family=Noto+Color+Emoji&family=Noto+Sans+Mono:wght@100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap');

   :root {
     --font-family      : 'Noto Sans', sans-serif;
     --font-family-emoji: 'Noto Color Emoji', sans-serif;
     --font-family-mono : 'Noto Sans Mono', monospace;
   }
   ```

   **Theme authors**: Consider providing instructions for loading your recommended web fonts manually instead of including them in your theme using `@import`. This allows users who prefer a different font to avoid loading your recommended web font(s) unnecessarily.
4. Advanced styling may require custom CSS declarations. This is expected, however custom CSS declarations may break when new versions of Docsify are released. When possible, leverage [theme properties](#/themes?id=theme-properties) instead of custom declarations or lock your [CDN](#/cdn) URLs to a [specific version](#/cdn?id=specific-version) to avoid potential issues when using custom CSS declarations.

   ```
   .sidebar li.active > a {
     border-right: 3px solid var(--theme-color);
   }
   ```

[Theme properties](#/themes?id=theme-properties)
------------------------------------------------

The following properties are available in all official Docsify themes. Default values for the "Core" theme are shown.

**Theme and plugin authors**: We encourage you to leverage these custom theme properties and to offer similar customization options in your projects.

### [Common](#/themes?id=common)

Below are the most commonly modified theme properties. [Advanced](#/themes?id=advanced) theme properties are also available for use but typically do not need to be modified.

```
/* Variables: Basic */
/* ========================================================================== */
:root {
  /* Color */
  --color-bg   : #fff;
  --color-text : #333;
  --theme-color: #0b85d7;

  /* Color: Monochromatic */
  --color-mono-min: var(--color-bg);
  --color-mono-1  : color-mix(in srgb, var(--color-mono-min), var(--color-mono-max) 5%);
  --color-mono-2  : color-mix(in srgb, var(--color-mono-min), var(--color-mono-max) 10%);
  --color-mono-3  : color-mix(in srgb, var(--color-mono-min), var(--color-mono-max) 20%);
  --color-mono-4  : color-mix(in srgb, var(--color-mono-min), var(--color-mono-max) 32%);
  --color-mono-5  : color-mix(in srgb, var(--color-mono-max), var(--color-mono-min) 50%);
  --color-mono-6  : color-mix(in srgb, var(--color-mono-max), var(--color-mono-min) 32%);
  --color-mono-7  : color-mix(in srgb, var(--color-mono-max), var(--color-mono-min) 20%);
  --color-mono-8  : color-mix(in srgb, var(--color-mono-max), var(--color-mono-min) 10%);
  --color-mono-9  : color-mix(in srgb, var(--color-mono-max), var(--color-mono-min) 5%);
  --color-mono-max: var(--color-text);

  /* Color: Theme Shades (darker) & Tints (lighter)*/
  /* NOTE: Values derived from --theme-color */
  --theme-color-1: color-mix(in srgb, var(--theme-color), var(--color-mono-min) 90%);
  --theme-color-2: color-mix(in srgb, var(--theme-color), var(--color-mono-min) 75%);
  --theme-color-3: color-mix(in srgb, var(--theme-color), var(--color-mono-min) 55%);
  --theme-color-4: color-mix(in srgb, var(--theme-color), var(--color-mono-min) 30%);
  --theme-color-5: color-mix(in srgb, var(--theme-color), var(--color-mono-max) 30%);
  --theme-color-6: color-mix(in srgb, var(--theme-color), var(--color-mono-max) 55%);
  --theme-color-7: color-mix(in srgb, var(--theme-color), var(--color-mono-max) 75%);
  --theme-color-8: color-mix(in srgb, var(--theme-color), var(--color-mono-max) 90%);

  /* Typography */
  --font-family      : system-ui, sans-serif;
  --font-family-emoji: 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  --font-family-mono : ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace;
  --font-size        : 16px; /* px */
  --font-size-xxxl   : calc(var(--font-size-xxl) * var(--modular-scale));
  --font-size-xxl    : calc(var(--font-size-xl) * var(--modular-scale));
  --font-size-xl     : calc(var(--font-size-l) * var(--modular-scale));
  --font-size-l      : calc(1rem * var(--modular-scale));
  --font-size-m      : var(--font-size);
  --font-size-s      : max(13px, calc(var(--font-size-m) / var(--modular-scale)));
  --font-size-xs     : max(11px, calc(var(--font-size-s) / var(--modular-scale)));
  --font-size-emoji  : 1.2em;
  --font-size-mono   : 0.875rem;
  --font-weight      : 350;
  --font-weight-mono : var(--font-weight);
  --line-height      : 1.6;
  --modular-scale    : 1.250; /* 1.067, 1.125, 1.200, 1.250, 1.333, 1.414, 1.500, 1.618 */

  /* Common */
  --border-color      : var(--color-mono-2);
  --border-radius     : 3px; /* Single value */
  --duration-slow     : 500ms;
  --duration-medium   : 250ms;
  --duration-fast     : 150ms;
  --margin-block      : 1rem; /* Single value */
  --scroll-padding-top: var(--margin-block);

  /* Content */
  --content-margin-inline: 45px; /* Single value */
  --content-max-width    : 72ch;

  /* Cover */
  --cover-bg           : unset;
  --cover-bg-brightness: 1;
  --cover-bg-overlay   : radial-gradient(transparent 60%, rgba(0, 0, 0, 0.1));
  --cover-color        : ;
  --cover-title-color  : var(--strong-color);
  --cover-title-font   : var(--font-size-xxxl) var(--font-family);

  /* Elements */
  --blockquote-bg                 : ;
  --blockquote-border-color       : var(--theme-color);
  --blockquote-border-radius      : 0;
  --blockquote-border-width       : 0 0 0 4px;
  --blockquote-color              : var(--color-mono-6);
  --blockquote-padding            : 0 0 0 1.5em;
  --button-bg                     : var(--theme-color);
  --button-border-radius          : 100vh;
  --button-color                  : #fff;
  --button-padding                : 0.3em 1.25em 0.315em 1.25em;
  --callout-bg                    : var(--color-mono-1);
  --callout-border-color          : ;
  --callout-border-radius         : var(--border-radius);
  --callout-border-width          : 1px;
  --callout-charm-bg              : ;
  --callout-charm-border-radius   : 100vh;
  --callout-charm-color           : #fff;
  --callout-charm-content         : '';
  --callout-charm-font-size       : 16px;
  --callout-charm-inset           : 1em auto auto 15px;
  --callout-charm-size            : 26px;
  --callout-charm-translate       : 0;
  --callout-color                 : ;
  --callout-padding               : 1em 1em 1em calc(25px + var(--callout-charm-size));
  --code-bg                       : var(--color-mono-1);
  --code-color                    : ;
  --codeblock-bg                  : var(--code-bg);
  --codeblock-color               : var(--code-color);
  --codeblock-comment             : #6e8090;
  --codeblock-function            : #dd4a68;
  --codeblock-important           : #c94922;
  --codeblock-keyword             : #07a;
  --codeblock-operator            : #a67f59;
  --codeblock-property            : #c08b30;
  --codeblock-punctuation         : #999;
  --codeblock-selector            : #690;
  --codeblock-tag                 : #905;
  --codeblock-variable            : #e90;
  --form-element-bg               : var(--color-mono-1);
  --form-element-border-color     : var(--color-mono-3);
  --form-element-border-radius    : var(--border-radius);
  --form-element-color            : ;
  --heading-color                 : var(--strong-color);
  --heading-font-weight           : 600;
  --heading-line-height           : calc(2ex + 5px); /* Unit required */
  --kbd-bg                        : var(--color-mono-1);
  --kbd-border                    : 1px solid var(--color-mono-3);
  --kbd-border-radius             : 4px;
  --kbd-color                     : var(--color-mono-5);
  --kbd-alt-bg                    : var(--color-mono-1);
  --kbd-alt-border                : none;
  --kbd-alt-border-radius         : var(--kbd-border-radius);
  --kbd-alt-box-shadow            : 0 2px 0 1px var(--color-mono-3);
  --kbd-alt-color                 : var(--kbd-color);
  --link-color                    : ;
  --link-color-hover              : var(--theme-color);
  --link-underline-color          : var(--theme-color);
  --link-underline-color-hover    : var(--link-underline-color);
  --link-underline-thickness      : 2px;
  --link-underline-thickness-hover: var(--link-underline-thickness);
  --mark-bg                       : #fef08a;
  --mark-color                    : ;
  --strong-color                  : color-mix(in srgb, var(--color-text), black 35%);
  --strong-font-weight            : 600;
  --table-row-alt-bg              : var(--color-mono-1);

  /* Navbar */
  --navbar-font-size        : var(--font-size);
  --navbar-height           : 4em;
  --navbar-link-color       : ;
  --navbar-link-color-active: var(--theme-color);
  --navbar-drop-link-spacing: 0.5em;

  /* Sidebar */
  --sidebar-bg                      : var(--color-bg);
  --sidebar-border-color            : var(--border-color);
  --sidebar-color                   : ;
  --sidebar-font-size               : var(--font-size);
  --sidebar-group-border            : ;
  --sidebar-group-spacing           : ;
  --sidebar-group-title-border      : ;
  --sidebar-group-title-color       : var(--strong-color);
  --sidebar-group-title-font-size   : ;
  --sidebar-group-title-font-weight : var(--strong-font-weight);
  --sidebar-group-title-spacing     : ;
  --sidebar-link-color              : var(--color-text);
  --sidebar-link-color-active       : var(--theme-color);
  --sidebar-link-spacing            : 0.75em;
  --sidebar-name-color              : var(--strong-color);
  --sidebar-name-font-family        : var(--font-family);
  --sidebar-name-font-size          : var(--font-size-xl);
  --sidebar-name-font-weight        : var(--strong-font-weight);
  --sidebar-name-margin             : 1.5rem 20px;
  --sidebar-pagelink-bg             : ;
  --sidebar-pagelink-bg-collapsed   : ;
  --sidebar-pagelink-bg-empty       : ;
  --sidebar-pagelink-bg-expanded    : ;
  --sidebar-toggle-alignment        : center; /* start center end */
  --sidebar-toggle-bg               : var(--color-mono-2);
  --sidebar-toggle-bg-hover         : var(--button-bg);
  --sidebar-toggle-color            : var(--color-mono-4);
  --sidebar-toggle-color-hover      : var(--button-color);
  --sidebar-toggle-height           : 80px;
  --sidebar-toggle-margin-block     : 20px;
  --sidebar-toggle-width            : 22px;
  --sidebar-width                   : 280px;
}

/* Scoped Variables */
/* ========================================================================== */
.callout {
  &.caution {
    /* Tailwind: red 50/200/500 */
    --callout-bg          : #fef2f2;
    --callout-border-color: #fecaca;
    --callout-charm-bg    : #ef4444 center no-repeat url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="13" height="13" fill="white"><path d="M10 14C10 15.1 9.1 16 8 16 6.9 16 6 15.1 6 14 6 12.9 6.9 12 8 12 9.1 12 10 12.9 10 14Z"/><path d="M10 1.6C10 1.2 9.8 0.9 9.6 0.7 9.2 0.3 8.6 0 8 0 7.4 0 6.8 0.2 6.5 0.6 6.2 0.9 6 1.2 6 1.6 6 1.7 6 1.8 6 1.9L6.8 9.6C6.9 9.9 7 10.1 7.2 10.2 7.4 10.4 7.7 10.5 8 10.5 8.3 10.5 8.6 10.4 8.8 10.3 9 10.1 9.1 9.9 9.2 9.6L10 1.9C10 1.8 10 1.7 10 1.6Z"/></svg>');
  }

  &.important {
    /* Tailwind: violet 50/200/500 */
    --callout-bg          : #f5f3ff;
    --callout-border-color: #ddd6fe;
    --callout-charm-bg    : #8b5cf6 center no-repeat url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16" fill="white"><path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path></svg>');
  }

  &.note {
    --callout-bg          : var(--theme-color-1);
    --callout-border-color: var(--theme-color-2);
    --callout-charm-bg    : var(--theme-color) center no-repeat url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14" fill="white"><path d="M9.1 0C10.2 0 10.7 0.7 10.7 1.6 10.7 2.6 9.8 3.6 8.6 3.6 7.6 3.6 7 3 7 2 7 1.1 7.7 0 9.1 0Z"/><path d="M5.8 16C5 16 4.4 15.5 5 13.2L5.9 9.1C6.1 8.5 6.1 8.2 5.9 8.2 5.7 8.2 4.6 8.6 3.9 9.1L3.5 8.4C5.6 6.6 7.9 5.6 8.9 5.6 9.8 5.6 9.9 6.6 9.5 8.2L8.4 12.5C8.2 13.2 8.3 13.5 8.5 13.5 8.7 13.5 9.6 13.2 10.4 12.5L10.9 13.2C8.9 15.2 6.7 16 5.8 16Z"/></svg>');
  }

  &.tip {
    /* Tailwind: teal 50/200/500 */
    --callout-bg          : #f0fdfa;
    --callout-border-color: #99f6e4;
    --callout-charm-bg    : #14b8a6 center no-repeat url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14" fill="white"><path d="M8 1.5c-2.363 0-4 1.69-4 3.75 0 .984.424 1.625.984 2.304l.214.253c.223.264.47.556.673.848.284.411.537.896.621 1.49a.75.75 0 0 1-1.484.211c-.04-.282-.163-.547-.37-.847a8.456 8.456 0 0 0-.542-.68c-.084-.1-.173-.205-.268-.32C3.201 7.75 2.5 6.766 2.5 5.25 2.5 2.31 4.863 0 8 0s5.5 2.31 5.5 5.25c0 1.516-.701 2.5-1.328 3.259-.095.115-.184.22-.268.319-.207.245-.383.453-.541.681-.208.3-.33.565-.37.847a.751.751 0 0 1-1.485-.212c.084-.593.337-1.078.621-1.489.203-.292.45-.584.673-.848.075-.088.147-.173.213-.253.561-.679.985-1.32.985-2.304 0-2.06-1.637-3.75-4-3.75ZM5.75 12h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1 0-1.5ZM6 15.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg>');
  }

  &.warning {
    /* Tailwind: amber 50/200/300 */
    --callout-bg          : #fffbeb;
    --callout-border-color: #fde68a;
    --callout-charm-bg    : #fcd34d center no-repeat url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="13" height="13" fill="#a16207"><path d="M10 14C10 15.1 9.1 16 8 16 6.9 16 6 15.1 6 14 6 12.9 6.9 12 8 12 9.1 12 10 12.9 10 14Z"/><path d="M10 1.6C10 1.2 9.8 0.9 9.6 0.7 9.2 0.3 8.6 0 8 0 7.4 0 6.8 0.2 6.5 0.6 6.2 0.9 6 1.2 6 1.6 6 1.7 6 1.8 6 1.9L6.8 9.6C6.9 9.9 7 10.1 7.2 10.2 7.4 10.4 7.7 10.5 8 10.5 8.3 10.5 8.6 10.4 8.8 10.3 9 10.1 9.1 9.9 9.2 9.6L10 1.9C10 1.8 10 1.7 10 1.6Z"/></svg>');
  }
}
```

### [Advanced](#/themes?id=advanced)

Advanced theme properties are also available for use but typically do not need to be modified. Values derived from [common](#/themes?id=common) theme properties but can be set explicitly if preferred.

```
/* Variables: Advanced */
/* ========================================================================== */
/* prettier-ignore */
:root {
  /* z-index */
  --z-skip-to-content: 2147483647;
  --z-progress       : 2147483637;
  --z-sidebar        : 60;
  --z-sidebar-toggle : 50;
  --z-main-overlay   : 40;
  --z-github-corner  : 30;
  --z-app-nav        : 20;
  --z-cover          : 10;
}
```

[Community](#/themes?id=community)
----------------------------------

See [Awesome Docsify](#/awesome) for additional community themes.

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/themes.md)