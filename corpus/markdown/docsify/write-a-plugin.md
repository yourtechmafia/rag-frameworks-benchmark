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
    - [Setup](#/write-a-plugin?id=setup "Setup")
    - [Template](#/write-a-plugin?id=template "Template")
    - [Lifecycle Hooks](#/write-a-plugin?id=lifecycle-hooks "Lifecycle Hooks")
    - [Tips](#/write-a-plugin?id=tips "Tips")
    - [Examples](#/write-a-plugin?id=examples "Examples")
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

[Write a plugin](#/write-a-plugin?id=write-a-plugin)
====================================================

A docsify plugin is a function with the ability to execute custom JavaScript code at various stages of Docsify's lifecycle.

[Setup](#/write-a-plugin?id=setup)
----------------------------------

Docsify plugins can be added directly to the `plugins` array:

```
window.$docsify = {
  plugins: [
    function myPlugin1(hook, vm) {
      // ...
    },
    function myPlugin2(hook, vm) {
      // ...
    },
  ],
};
```

Alternatively, a plugin can be stored in a separate file and "installed" using a standard `<script>` tag:

```
// docsify-plugin-myplugin.js

{
  function myPlugin(hook, vm) {
    // ...
  }

  // Add plugin to docsify's plugin array
  window.$docsify = window.$docsify || {};
  $docsify.plugins = [...($docsify.plugins || []), myPlugin];
}
```

```
<script src="docsify-plugin-myplugin.js"></script>
```

[Template](#/write-a-plugin?id=template)
----------------------------------------

Below is a plugin template with placeholders for all available lifecycle hooks.

1. Copy the template
2. Modify the `myPlugin` name as appropriate
3. Add your plugin logic
4. Remove unused lifecycle hooks
5. Save the file as `docsify-plugin-[name].js`
6. Load your plugin using a standard `<script>` tag

```
{
  function myPlugin(hook, vm) {
    // Invoked one time when docsify script is initialized
    hook.init(() => {
      // ...
    });

    // Invoked one time when the docsify instance has mounted on the DOM
    hook.mounted(() => {
      // ...
    });

    // Invoked on each page load before new markdown is transformed to HTML.
    // Supports asynchronous tasks (see beforeEach documentation for details).
    hook.beforeEach(markdown => {
      // ...
      return markdown;
    });

    // Invoked on each page load after new markdown has been transformed to HTML.
    // Supports asynchronous tasks (see afterEach documentation for details).
    hook.afterEach(html => {
      // ...
      return html;
    });

    // Invoked on each page load after new HTML has been appended to the DOM
    hook.doneEach(() => {
      // ...
    });

    // Invoked one time after rendering the initial page
    hook.ready(() => {
      // ...
    });
  }

  // Add plugin to docsify's plugin array
  window.$docsify = window.$docsify || {};
  $docsify.plugins = [myPlugin, ...($docsify.plugins || [])];
}
```

[Lifecycle Hooks](#/write-a-plugin?id=lifecycle-hooks)
------------------------------------------------------

Lifecycle hooks are provided via the `hook` argument passed to the plugin function.

### [init()](#/write-a-plugin?id=init)

Invoked one time when docsify script is initialized.

```
hook.init(() => {
  // ...
});
```

### [mounted()](#/write-a-plugin?id=mounted)

Invoked one time when the docsify instance has mounted on the DOM.

```
hook.mounted(() => {
  // ...
});
```

### [beforeEach()](#/write-a-plugin?id=beforeeach)

Invoked on each page load before new markdown is transformed to HTML.

```
hook.beforeEach(markdown => {
  // ...
  return markdown;
});
```

For asynchronous tasks, the hook function accepts a `next` callback as a second argument. Call this function with the final `markdown` value when ready. To prevent errors from affecting docsify and other plugins, wrap async code in a `try/catch/finally` block.

```
hook.beforeEach((markdown, next) => {
  try {
    // Async task(s)...
  } catch (err) {
    // ...
  } finally {
    next(markdown);
  }
});
```

### [afterEach()](#/write-a-plugin?id=aftereach)

Invoked on each page load after new markdown has been transformed to HTML.

```
hook.afterEach(html => {
  // ...
  return html;
});
```

For asynchronous tasks, the hook function accepts a `next` callback as a second argument. Call this function with the final `html` value when ready. To prevent errors from affecting docsify and other plugins, wrap async code in a `try/catch/finally` block.

```
hook.afterEach((html, next) => {
  try {
    // Async task(s)...
  } catch (err) {
    // ...
  } finally {
    next(html);
  }
});
```

### [doneEach()](#/write-a-plugin?id=doneeach)

Invoked on each page load after new HTML has been appended to the DOM.

```
hook.doneEach(() => {
  // ...
});
```

### [ready()](#/write-a-plugin?id=ready)

Invoked one time after rendering the initial page.

```
hook.ready(() => {
  // ...
});
```

[Tips](#/write-a-plugin?id=tips)
--------------------------------

* Access Docsify methods and properties using `window.Docsify`
* Access the current Docsify instance using the `vm` argument
* Developers who prefer using a debugger can set the [`catchPluginErrors`](#/configuration?id=catchpluginerrors) configuration option to `false` to allow their debugger to pause JavaScript execution on error
* Be sure to test your plugin on all supported platforms and with related configuration options (if applicable) before publishing

[Examples](#/write-a-plugin?id=examples)
----------------------------------------

#### [Page Footer](#/write-a-plugin?id=page-footer)

```
window.$docsify = {
  plugins: [
    function pageFooter(hook, vm) {
      const footer = /* html */ `
        <hr/>
        <footer>
          <span><a href="https://github.com/QingWei-Li">cinwell</a> ©2017.</span>
          <span>Proudly published with <a href="https://github.com/docsifyjs/docsify" target="_blank">docsify</a>.</span>
        </footer>
      `;

      hook.afterEach(html => {
        return html + footer;
      });
    },
  ],
};
```

### [Edit Button (GitHub)](#/write-a-plugin?id=edit-button-github)

```
window.$docsify = {
  plugins: [
    function editButton(hook, vm) {
      // The date template pattern
      $docsify.formatUpdated = '{YYYY}/{MM}/{DD} {HH}:{mm}';

      hook.beforeEach(html => {
        const url =
          'https://github.com/docsifyjs/docsify/blob/main/docs/' +
          vm.route.file;
        const editHtml = '[📝 EDIT DOCUMENT](' + url + ')\n';

        return (
          editHtml +
          html +
          '\n----\n' +
          'Last modified ' +
          editHtml
        );
      });
    },
  ],
};
```

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/write-a-plugin.md)