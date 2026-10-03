Skip to main content

* Translations

  + [English](#/ "English")
  + [简体中文](#/zh-cn/ "简体中文")

Clear search

`/`
`⌃K`

[docsify](#/)
=============

[Markdown configuration](#/markdown?id=markdown-configuration)
==============================================================

**docsify** uses [marked](https://github.com/markedjs/marked) as its Markdown parser. You can customize how it renders your Markdown content to HTML by customizing `renderer`:

```
window.$docsify = {
  markdown: {
    smartypants: true,
    renderer: {
      link() {
        // ...
      },
    },
  },
};
```

Configuration Options Reference: [marked documentation](https://marked.js.org/#/USING_ADVANCED.md)

You can completely customize the parsing rules.

```
window.$docsify = {
  markdown(marked, renderer) {
    // ...

    return marked;
  },
};
```

[Supports mermaid](#/markdown?id=supports-mermaid)
--------------------------------------------------

Currently, docsify doesn't support the async mermaid render (the latest mermaid version supported is `v9.3.0`).

```
//  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.css">
//  <script src="//cdn.jsdelivr.net/npm/mermaid@9.3.0/dist/mermaid.min.js"></script>

let num = 0;
mermaid.initialize({ startOnLoad: false });

window.$docsify = {
  markdown: {
    renderer: {
      code({ text, lang }) {
        if (lang === 'mermaid') {
          return /* html */ `
            <div class="mermaid">${mermaid.render(
              'mermaid-svg-' + num++,
              text,
            )}</div>
          `;
        }
        return this.origin.code.apply(this, arguments);
      },
    },
  },
};
```

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/markdown.md)