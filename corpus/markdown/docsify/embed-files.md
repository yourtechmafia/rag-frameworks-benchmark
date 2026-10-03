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
  + [Vue compatibility](#/vue "Vue compatibility")
  + [CDN](#/cdn "CDN")
  + [Offline Mode (PWA)](#/pwa "Offline Mode (PWA)")
  + [Embed Files](#/embed-files "Embed Files")
    - [Embedded file type](#/embed-files?id=embedded-file-type "Embedded file type")
    - [Markdown with YAML Front Matter](#/embed-files?id=markdown-with-yaml-front-matter "Markdown with YAML Front Matter")
    - [Embedded code fragments](#/embed-files?id=embedded-code-fragments "Embedded code fragments")
    - [Tag attribute](#/embed-files?id=tag-attribute "Tag attribute")
    - [The code block highlight](#/embed-files?id=the-code-block-highlight "The code block highlight")
    - [Embed a gist](#/embed-files?id=embed-a-gist "Embed a gist")
  + [UI Kit](#/ui-kit "UI Kit")
* Upgrading

  + [v4 to v5](#/v5-upgrade "v4 to v5")

* [Awesome docsify](#/awesome "Awesome docsify")
* [Changelog](#/changelog "Changelog")

[Embed files](#/embed-files?id=embed-files)
===========================================

With docsify 4.6 it is now possible to embed any type of file.

You can embed these files as video, audio, iframes, or code blocks, and even Markdown files can even be embedded directly into the document.

For example, here is an embedded Markdown file. You only need to do this:

```
[filename](_media/example.md ':include')
```

Then the content of `example.md` will be displayed directly here:

> This is from the `example.md`

You can check the original content for [example.md](_media/example.md).

Normally, this will be compiled into a link, but in docsify, if you add `:include` it will be embedded. You can use single or double quotation marks around as you like.

External links can be used too - just replace the target. If you want to use a gist URL, see [Embed a gist](#/embed-files?id=embed-a-gist) section.

[Embedded file type](#/embed-files?id=embedded-file-type)
---------------------------------------------------------

Currently, file extensions are automatically recognized and embedded in different ways.

These types are supported:

* **iframe** `.html`, `.htm`
* **markdown** `.markdown`, `.md`
* **audio** `.mp3`
* **video** `.mp4`, `.ogg`
* **code** other file extension

Of course, you can force the specified type. For example, a Markdown file can be embedded as a code block by setting `:type=code`.

```
[filename](_media/example.md ':include :type=code')
```

You will get:

```
> This is from the `example.md`
```

[Markdown with YAML Front Matter](#/embed-files?id=markdown-with-yaml-front-matter)
-----------------------------------------------------------------------------------

Front Matter, commonly utilized in blogging systems like Jekyll, serves to define metadata for a document. The [front-matter.js](https://www.npmjs.com/package/front-matter) package facilitates the extraction of metadata (front matter) from documents.

When using Markdown, YAML front matter will be stripped from the rendered content. The attributes cannot be used in this case.

```
<script src="//cdn.jsdelivr.net/npm/docsify@5/dist/plugins/front-matter.min.js"></script>
```

```
[filename](_media/example-with-yaml.md ':include')
```

You will get just the content

> This is from the `example-with-yaml.md`

[Embedded code fragments](#/embed-files?id=embedded-code-fragments)
-------------------------------------------------------------------

Sometimes you don't want to embed a whole file. Maybe because you need just a few lines but you want to compile and test the file in CI.

```
[filename](_media/example.js ':include :type=code :fragment=demo')
```

In your code file you need to surround the fragment between `/// [demo]` lines (before and after the fragment).
Alternatively you can use `### [demo]`. By default, only identifiers are omitted. To omit the entire line containing the identifier in the fragment output, add the `:omitFragmentLine` option. This is useful if your code fragment is e.g. HTML and you want to hide the Docsify fragment identifier from showing in your HTML source. `<!-- /// [demo] -->` in your source file and `:omitFragmentLine` will make the `-->` not show up in your Docsify code fragment section.

Example: In the source file \_media/example.js, `/// [demo]` identifiers have been included:

```
[filename](_media/example.js ':include :type=code')
```

```
import fetch from 'fetch';

const URL = 'https://example.com';
const PORT = 8080;

/// [demo]
const result = fetch(`${URL}:${PORT}`)
  .then(response => {
    return response.json();
  })
  .then(myJson => {
    console.log(JSON.stringify(myJson));
  });
/// [demo]

result.then(console.log).catch(console.error);
```

Adding the `:fragment=demo` results in the following:

```
[filename](_media/example.js ':include :type=code :fragment=demo')
```

```
const result = fetch(`${URL}:${PORT}`)
  .then(response => {
    return response.json();
  })
  .then(myJson => {
    console.log(JSON.stringify(myJson));
  });
```

[Tag attribute](#/embed-files?id=tag-attribute)
-----------------------------------------------

If you embed the file as `iframe`, `audio` and `video`, then you may need to set the attributes of these tags.

Note, for the `audio` and `video` types, docsify adds the `controls` attribute by default. When you want add more attributes, the `controls` attribute need to be added manually if need be.

```
[filename](_media/example.mp4 ':include :type=video controls width=100%')
```

```
[cinwell website](https://cinwell.com ':include :type=iframe width=100% height=400px')
```

Did you see it? You only need to write directly. You can check [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) for these attributes.

[The code block highlight](#/embed-files?id=the-code-block-highlight)
---------------------------------------------------------------------

Embedding any type of source code file, you can specify the highlighted language or automatically identify.

```
[](_media/example.html ':include :type=code text')
```

⬇️

```
<style>
  html,
  body {
    margin: 0;
    padding: 0;
    min-height: 100%;
  }

  body {
    background-color: #4158d0;
    background-image: linear-gradient(
      43deg,
      #4158d0 0%,
      #c850c0 46%,
      #ffcc70 100%
    );
    color: #fff;
    font-family: sans-serif;
  }

  main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
</style>

<main>
  <p>Example HTML Page</p>
</main>
```

How to set highlight? You can see [here](#/language-highlight).

[Embed a gist](#/embed-files?id=embed-a-gist)
---------------------------------------------

You can embed a gist as markdown content or as a code block - this is based on the approach at the start of [Embed Files](#/embed-files?id=embed-files) section, but uses a raw gist URL as the target.

**No** plugin or app config change is needed here to make this work. In fact, the "Embed" `script` tag that is copied from a gist will *not* load even if you make plugin or config changes to allow an external script.

### [Identify the gist's metadata](#/embed-files?id=identify-the-gists-metadata)

Start by viewing a gist on `gist.github.com`. For the purposes of this guide, we use this gist:

* <https://gist.github.com/anikethsaha/f88893bb563bb7229d6e575db53a8c15>

Identify the following items from the gist:

| Field | Example | Description |
| --- | --- | --- |
| **Username** | `anikethsaha` | The gist's owner. |
| **Gist ID** | `c2bece08f27c4277001f123898d16a7c` | Identifier for the gist. This is fixed for the gist's lifetime. |
| **Filename** | `content.md` | Select a name of a file in the gist. This needed even on a single-file gist for embedding to work. |

You will need those to build the *raw gist URL* for the target file. This has the following format:

* `https://gist.githubusercontent.com/USERNAME/GIST_ID/raw/FILENAME`

Here are two examples based on the sample gist:

* <https://gist.githubusercontent.com/anikethsaha/f88893bb563bb7229d6e575db53a8c15/raw/content.md>
* <https://gist.githubusercontent.com/anikethsaha/f88893bb563bb7229d6e575db53a8c15/raw/script.js>

Alternatively, you can get a raw URL directly clicking the *Raw* button on a gist file. But, if you use that approach, just be sure to **remove** the revision number between `raw/` and the filename so that the URL matches the pattern above instead. Otherwise your embedded gist will **not** show the latest content when the gist is updated.

Continue with one of the sections below to embed the gist on a Docsify page.

### [Render markdown content from a gist](#/embed-files?id=render-markdown-content-from-a-gist)

This is a great way to embed content **seamlessly** in your docs, without sending someone to an external link. This approach is well-suited to reusing a gist of say installation instructions across doc sites of multiple repos. This approach works equally well with a gist owned by your account or by another user.

Here is the format:

```
[LABEL](https://gist.githubusercontent.com/USERNAME/GIST_ID/raw/FILENAME ':include')
```

For example:

```
[gist: content.md](https://gist.githubusercontent.com/anikethsaha/f88893bb563bb7229d6e575db53a8c15/raw/content.md ':include')
```

Which renders as:

This is a **markdown** file in a gist.

The `LABEL` can be any text you want. It acts as a *fallback* message if the link is broken - so it is useful to repeat the filename here in case you need to fix a broken link. It also makes an embedded element easy to read at a glance.

### [Render a codeblock from a gist](#/embed-files?id=render-a-codeblock-from-a-gist)

The format is the same as the previous section, but with `:type=code` added to the alt text. As with the [Embedded file type](#/embed-files?id=embedded-file-type) section, the syntax highlighting will be **inferred** from the extension (e.g. `.js` or `.py`), so you can leave the `type` set as `code`.

Here is the format:

```
[LABEL](https://gist.githubusercontent.com/USERNAME/GIST_ID/raw/FILENAME ':include :type=code')
```

For example:

```
[gist: script.js](https://gist.githubusercontent.com/anikethsaha/f88893bb563bb7229d6e575db53a8c15/raw/script.js ':include :type=code')
```

Which renders as:

```
console.log("[Docsify Example] : This is a script in a gist");
```

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/embed-files.md)

![qingwei-li](https://github.com/qingwei-li.png)

Qingwei Li
==========

> A Web developer who loves to create amazing things

* [Twitter](https://twitter.com/cinwell_li)
* [GitHub](https://github.com/qingwei-li)

loading

#### ⬇️ My projects ⬇️

* ![](https://cdn.statically.io/gh/QingWei-Li/notea/gh-pages/screen.png)

  ##### Notea

  📒 Self hosted note taking app stored on S3.

  web app

  + [GitHub](https://github.com/qingwei-li/Notea)
  + [Website](https://cinwell.com/notea)
  + [Demo](https://notea.cinwell.com)
* ![](https://docsify.js.org/_media/icon.svg)

  ##### docsify

  🃏 A magical documentation site generator.

  tool

  + [GitHub](https://github.com/qingwei-li/docsify)
  + [Documentation](https://docsify.js.org/)
* ![](https://cloud.githubusercontent.com/assets/7565692/21482443/093e4970-cbaf-11e6-89f0-eae73fc49741.png)

  ##### vuep

  🎡 A component for rendering Vue.JS 2.0 components with live editor and preview.

  component

  + [GitHub](https://github.com/qingwei-li/vuep)
  + [Documentation](https://cinwell.com/vuep/)
* ![](https://cloud.githubusercontent.com/assets/7565692/23977197/9da0b77c-0a27-11e7-8f14-4d3845a524a0.png)

  ##### vue-trend

  🌈 Simple, elegant spark lines for Vue.JS 2.0.

  component

  + [GitHub](https://github.com/qingwei-li/vue-trend)
  + [Live Demo](https://jsfiddle.net/nyh18bLq/)
* ![](https://user-images.githubusercontent.com/7565692/35255046-f47a5390-0027-11e8-948e-f0d5003ec3e2.png)

  ##### vue-markdown-loader

  📇 Convert Markdown file to Vue.JS 2.0 component.

  tool

  + [GitHub](https://github.com/qingwei-li/vue-markdown-loader)
  + [Demo](glitch.com/edit/#!/vue-markdown)
* ![](https://cloud.githubusercontent.com/assets/7565692/25064699/68349860-2232-11e7-85e9-fbdd88de317c.png)

  ##### npmarket

  🛒 More efficient search for node packages

  web app

  + [GitHub](https://github.com/qingwei-li/npmarket)
  + [Website](https://npmarket.netlify.com)
* ![](https://user-images.githubusercontent.com/7565692/36073530-564f1a02-0f6d-11e8-803e-a34fa9366b4e.png)

  ##### markdone/cssume

  📄 An elegant css theme for resume generated by Markdown

  css

  + [GitHub](https://github.com/markdone/cssume)
  + [Demo](https://markdone.github.io/cssume/)
* ![](https://user-images.githubusercontent.com/7565692/38164663-4632dae4-353a-11e8-9c7e-2a39bdce1f0f.png)

  ##### Laue

  🖖📈 Modern charts for Vue.js 2.0

  component

  + [GitHub](https://github.com/qingwei-li/Laue)
  + [Documentation](https://laue.js.org)
* ![](https://user-images.githubusercontent.com/7565692/38162374-906003e4-3512-11e8-8780-a22350a665fc.png)

  ##### Vuep.run

  🏃 An online playground for Vue

  web app

  + [GitHub](https://github.com/qingwei-li/Vuep.run)
  + [Website](https://vuep.run)
* ![](https://user-images.githubusercontent.com/7565692/38164640-f55200c8-3539-11e8-9c45-247b430339ea.png)

  ##### hostext

  🔡 Text hosting service

  microservice

  + [GitHub](https://github.com/qingwei-li/hostext)
  + [Website](https://text.cinwell.xyz)

[More projects](https://github.com/QingWei-Li?utf8=%E2%9C%93&tab=repositories&q=&type=source)