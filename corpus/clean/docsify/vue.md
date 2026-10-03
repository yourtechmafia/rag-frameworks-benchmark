Vue compatibility
===============================================

Docsify allows [Vue.js](https://vuejs.org) content to be added directly to your markdown pages. This can greatly simplify working with data and adding reactivity to your site.

Vue [template syntax](https://vuejs.org/guide/essentials/template-syntax) can be used to add dynamic content to your pages. Vue content becomes more interesting when [data](#/vue?id=data), [computed properties](#/vue?id=computed-properties), [methods](#/vue?id=methods), and [lifecycle hooks](#/vue?id=lifecycle-hooks) are used. These options can be specified as [global options](#/vue?id=global-options) or within DOM [mounts](#/vue?id=mounts) and [components](#/vue?id=components).

Setup
-----------------------

To get started, add Vue.js to your `index.html` file. Choose the production version for your live site or the development version for helpful console warnings and [Vue.js devtools](https://github.com/vuejs/vue-devtools) support.

```
<!-- Production -->
<script src="//cdn.jsdelivr.net/npm/vue@3/dist/vue.global.prod.js"></script>

<!-- Development -->
<script src="//cdn.jsdelivr.net/npm/vue@3/dist/vue.global.js"></script>
```

Template syntax
-------------------------------------------

Vue [template syntax](https://vuejs.org/guide/essentials/template-syntax) offers several useful features like support for [JavaScript expressions](https://vuejs.org/guide/essentials/template-syntax.html#using-javascript-expressions) and Vue [directives](https://vuejs.org/guide/essentials/template-syntax.html#directives) for loops and conditional rendering.

```
<!-- Hide in docsify, show elsewhere (e.g. GitHub) -->
<p v-if="false">Text for GitHub</p>

<!-- Sequenced content (i.e. loop)-->
<ul>
  <li v-for="i in 3">Item {{ i }}</li>
</ul>

<!-- JavaScript expressions -->
<p>2 + 2 = {{ 2 + 2 }}</p>
```

* Item 1
* Item 2
* Item 3

2 + 2 = 4

[View output on GitHub](https://github.com/docsifyjs/docsify/blob/develop/docs/vue.md#template-syntax)

Code Blocks
-----------------------------------

Docsify ignores Vue template syntax within code blocks by default:

```
```
{{ message }}
```
```

To process Vue template syntax within a code block, wrap the code block in an element with a `v-template` attribute:

```
<div v-template>

```
{{ message }}
```

</div>
```

Data
---------------------

```
{
  data() {
    return {
      message: 'Hello, World!'
    };
  }
}
```

```
<!-- Show message in docsify, show "{{ message }}" elsewhere (e.g. GitHub)  -->
{{ message }}

<!-- Show message in docsify, hide elsewhere (e.g. GitHub)  -->
<p v-text="message"></p>
```

Hello, World!

Hello, World!

[View output on GitHub](https://github.com/docsifyjs/docsify/blob/develop/docs/vue.md#data)

Computed properties
---------------------------------------------------

```
{
  computed: {
    timeOfDay() {
      const date = new Date();
      const hours = date.getHours();

      if (hours < 12) {
        return 'morning';
      }
      else if (hours < 18) {
        return 'afternoon';
      }
      else {
        return 'evening'
      }
    }
  },
}
```

```
Good {{ timeOfDay }}!
```

Good morning!

Methods
---------------------------

```
{
  data() {
    return {
      message: 'Hello, World!'
    };
  },
  methods: {
    hello() {
      alert(this.message);
    }
  },
}
```

```
<button @click="hello">Say Hello</button>
```

Say Hello

Lifecycle Hooks
-------------------------------------------

```
{
  data() {
    return {
      images: null,
    };
  },
  created() {
    fetch('https://api.domain.com/')
      .then(response => response.json())
      .then(data => (this.images = data))
      .catch(err => console.log(err));
  }
}

// API response:
// [
//   { title: 'Image 1', url: 'https://domain.com/1.jpg' },
//   { title: 'Image 2', url: 'https://domain.com/2.jpg' },
//   { title: 'Image 3', url: 'https://domain.com/3.jpg' },
// ];
```

```
<div style="display: flex;">
  <figure style="flex: 1;">
    <img v-for="image in images" :src="image.url" :title="image.title">
    <figcaption>{{ image.title }}</figcaption>
  </figure>
</div>
```

Image 1

Image 2

Image 3

Global options
-----------------------------------------

Use `vueGlobalOptions` to specify global Vue options for use with Vue content not explicitly mounted with [vueMounts](#/vue?id=mounts), [vueComponents](#/vue?id=components), or a [markdown script](#/vue?id=markdown-script). Changes to global `data` will persist and be reflected anywhere global references are used.

```
window.$docsify = {
  vueGlobalOptions: {
    data() {
      return {
        count: 0,
      };
    },
  },
};
```

```
<p>
  <button @click="count += 1">+</button>
  {{ count }}
  <button @click="count -= 1">-</button>
</p>
```

+ 0 -

Notice the behavior when multiple global counters are rendered:

+ 0 -

Changes made to one counter affect the both counters. This is because both instances reference the same global `count` value. Now, navigate to a new page and return to this section to see how changes made to global data persist between page loads.

Mounts
-------------------------

Use `vueMounts` to specify DOM elements to mount as Vue instances and their associated options. Mount elements are specified using a [CSS selector](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) as the key with an object containing Vue options as their value. Docsify will mount the first matching element in the main content area each time a new page is loaded. Mount element `data` is unique for each instance and will not persist as users navigate the site.

```
window.$docsify = {
  vueMounts: {
    '#counter': {
      data() {
        return {
          count: 0,
        };
      },
    },
  },
};
```

```
<div id="counter">
  <button @click="count += 1">+</button>
  {{ count }}
  <button @click="count -= 1">-</button>
</div>
```

+ 0 -

Components
---------------------------------

Use `vueComponents` to create and register global [Vue components](https://vuejs.org/guide/essentials/component-basics.html). Components are specified using the component name as the key with an object containing Vue options as the value. Component `data` is unique for each instance and will not persist as users navigate the site.

```
window.$docsify = {
  vueComponents: {
    'button-counter': {
      template: `
        <button @click="count += 1">
          You clicked me {{ count }} times
        </button>
      `,
      data() {
        return {
          count: 0,
        };
      },
    },
  },
};
```

```
<button-counter></button-counter>
<button-counter></button-counter>
```

You clicked me 0 timesYou clicked me 0 times

Markdown script
-------------------------------------------

Vue content can mounted using a `<script>` tag in your markdown pages.

Only the first `<script>` tag in a markdown file is executed. If you wish to mount multiple Vue instances using a script tag, all instances must be mounted within the first script tag in your markdown.

```
<script>
  Vue.createApp({
    // Options...
  }).mount('#example');
</script>
```

Technical Notes
-------------------------------------------

* Docsify processes Vue content in the following order on each page load:
  1. Execute markdown `<script>`
  2. Register global `vueComponents`
  3. Mount `vueMounts`
  4. Auto-mount unmounted `vueComponents`
  5. Auto-mount unmounted Vue template syntax using `vueGlobalOptions`
* When auto-mounting Vue content, docsify will mount each top-level element in your markdown that contains template syntax or a component. For example, in the following HTML the top-level `<p>`, `<my-component />`, and `<div>` elements will be mounted.

  ```
  <p>{{ foo }}</p>
  <my-component />
  <div>
    <span>{{ bar }}</span>
    <some-other-component />
  </div>
  ```
* Docsify will not mount an existing Vue instance or an element that contains an existing Vue instance.
* Docsify will automatically destroy/unmount all Vue instances it creates before each page load.

---
