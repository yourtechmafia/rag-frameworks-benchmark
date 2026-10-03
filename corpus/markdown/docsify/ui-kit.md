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
  + [UI Kit](#/ui-kit "UI Kit")
    - [Blockquotes](#/ui-kit?id=blockquotes "Blockquotes")
    - [Buttons](#/ui-kit?id=buttons "Buttons")
    - [Callouts](#/ui-kit?id=callouts "Callouts")
    - [Code](#/ui-kit?id=code "Code")
    - [Colors](#/ui-kit?id=colors "Colors")
    - [Details](#/ui-kit?id=details "Details")
    - [Form Elements](#/ui-kit?id=form-elements "Form Elements")
    - [Headings](#/ui-kit?id=headings "Headings")
    - [Horizontal Rule](#/ui-kit?id=horizontal-rule "Horizontal Rule")
    - [IFrame](#/ui-kit?id=iframe "IFrame")
    - [Images](#/ui-kit?id=images "Images")
    - [Keyboard](#/ui-kit?id=keyboard "Keyboard")
    - [Links](#/ui-kit?id=links "Links")
    - [Lists](#/ui-kit?id=lists "Lists")
    - [Output](#/ui-kit?id=output "Output")
    - [Tables](#/ui-kit?id=tables "Tables")
    - [Text Elements](#/ui-kit?id=text-elements "Text Elements")
    - [Text Styles](#/ui-kit?id=text-styles "Text Styles")
* Upgrading

  + [v4 to v5](#/v5-upgrade "v4 to v5")

* [Awesome docsify](#/awesome "Awesome docsify")
* [Changelog](#/changelog "Changelog")

[UI Kit](#/ui-kit?id=ui-kit)
============================

View the markdown source for this page

```
<!-- markdownlint-disable single-title no-duplicate-heading -->

# UI Kit

<details>
  <summary>View the markdown source for this page</summary>
  <div style="max-height: 50vh; overflow: auto;">

[ui-kit.md](ui-kit.md ':include :type=code')

  </div>
</details>

## Blockquotes

> Cras aliquet nulla quis metus tincidunt, sed placerat enim cursus. Etiam
> turpis nisl, posuere eu condimentum ut, interdum a risus. Sed non luctus mi.
> Quisque malesuada risus sit amet tortor aliquet, a posuere ex iaculis. Vivamus
> ultrices enim dui, eleifend porttitor elit aliquet sed.
>
> _- Quote Source_

#### Nested

<!-- prettier-ignore -->
> Level 1
> > Level 2
> > > Level 3

## Buttons

#### Default

<button>Button</button>

#### Basic

<button type="button">Button</button>
<a href="javascript:void(0);" class="button">Link Button</a>
<input type="button" value="Input Button" class="button">

#### Primary

<button type="button" class="primary">Button</button>
<a href="javascript:void(0);" class="button primary">Link Button</a>
<input type="button" value="Input Button" class="primary">

#### Secondary

<button type="button" class="secondary">Button</button>
<a href="javascript:void(0);" class="button secondary">Link Button</a>
<input type="button" value="Input Button" class="secondary">

## Callouts

<!-- prettier-ignore -->
> [!CAUTION]
> **Caution** callout with `inline code`.

<!-- prettier-ignore -->
> [!IMPORTANT]
> **Important** callout with `inline code`.

<!-- prettier-ignore -->
> [!NOTE]
> **Note** callout with `inline code`.

<!-- prettier-ignore -->
> [!TIP]
> **Tip** callout with `inline code`.

<!-- prettier-ignore -->
> [!WARNING]
> **Warning** callout with `inline code`.

**Multi Line**

<!-- prettier-ignore -->
> [!NOTE]
> - List item 1
> - List item 2
>
> Text
>
> ```html
> <p>Hello, World!</p>
> ```

**Nested**

<!-- prettier-ignore -->
> [!NOTE]
> Level 1
> > [!NOTE]
> > Level 2
> > > [!NOTE]
> > > Level 3

**Legacy Style**

!> Legacy **Important** callout with `inline code`.

?> Legacy **Tip** with `inline code`.

## Code

This is `inline code`

```javascript
const add = (num1, num2) => num1 + num2;
const total = add(1, 2);

console.log(total); // 3
```

```html
<body>
  <p>Hello</p>
</body>
```

## Colors

#### Theme

<div class="ui-kit-color">
  <figure>
    <div style="background: var(--theme-color-1);"></div>
    <figcaption>1<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color-2);"></div>
    <figcaption>2<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color-3);"></div>
    <figcaption>3<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color-4);"></div>
    <figcaption>4<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color);"></div>
    <figcaption>Theme Color<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color-5);"></div>
    <figcaption>5<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color-6);"></div>
    <figcaption>6<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color-7);"></div>
    <figcaption>7<figcaption>
  </figure>
  <figure>
    <div style="background: var(--theme-color-8);"></div>
    <figcaption>8<figcaption>
  </figure>
</div>

#### Monochromatic

<div class="ui-kit-color">
  <figure>
    <div style="background: var(--color-mono-min); border: 1px solid var(--color-mono-2);"></div>
    <figcaption>Min<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-1);"></div>
    <figcaption>1<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-2);"></div>
    <figcaption>2<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-3);"></div>
    <figcaption>3<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-4);"></div>
    <figcaption>4<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-5);"></div>
    <figcaption>5<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-6);"></div>
    <figcaption>6<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-7);"></div>
    <figcaption>7<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-8);"></div>
    <figcaption>8<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-9);"></div>
    <figcaption>9<figcaption>
  </figure>
  <figure>
    <div style="background: var(--color-mono-max);"></div>
    <figcaption>Max<figcaption>
  </figure>
</div>

## Details

<details>
  <summary>Details (click to open)</summary>

Suscipit nemo aut ex suscipit voluptatem laboriosam odio velit. Ipsum eveniet labore sequi non optio vel. Ut culpa ad accusantium est aut harum ipsam voluptatum. Velit eum incidunt non sint. Et molestiae veniam natus autem vel assumenda ut numquam esse. Non nisi id qui vero corrupti quos et.

</details>

<details open>
  <summary>Details (open by default)</summary>

Suscipit nemo aut ex suscipit voluptatem laboriosam odio velit. Ipsum eveniet labore sequi non optio vel. Ut culpa ad accusantium est aut harum ipsam voluptatum. Velit eum incidunt non sint. Et molestiae veniam natus autem vel assumenda ut numquam esse. Non nisi id qui vero corrupti quos et.

</details>

## Form Elements

### Fieldset

<form>
  <fieldset>
    <legend>Legend</legend>
    <p>
      <label>
        Label<br>
        <input type="text" placeholder="Placeholder">
      </label>
    </p>
  </fieldset>
</form>

### Input

#### Checkbox

<form>
  <label><input type="checkbox" value="HTML" checked> HTML</label><br>
  <label><input type="checkbox" value="CSS"> CSS</label><br>
  <label><input type="checkbox" value="JavaScript"> JavaScript</label>
</form>

#### Datalist

<form>
  <label>
    Label<br>
    <input list="planets">
    <datalist id="planets">
      <option value="Earth">Earth</option>
      <option value="Jupiter">Jupiter</option>
      <option value="Mars">Mars</option>
      <option value="Mercury">Mercury</option>
      <option value="Neptune">Neptune</option>
      <option value="Saturn">Saturn</option>
      <option value="Uranus">Uranus</option>
      <option value="Venus">Venus</option>
    </datalist>
  </label>
</form>

#### Radio

<form>
  <label><input type="radio" name="language" value="HTML" checked> HTML</label><br>
  <label><input type="radio" name="language" value="CSS"> CSS</label><br>
  <label><input type="radio" name="language" value="JavaScript"> JavaScript</label>
</form>

#### Text

<form>
  <label>
    First name<br>
    <input type="text" placeholder="Placeholder">
  </label>
</form>

#### Toggles

<form>
Checkbox (multi-select)

<label><input class="toggle" type="checkbox" checked> HTML</label><br>
<label><input class="toggle" type="checkbox"> CSS</label><br>
<label><input class="toggle" type="checkbox"> JavaScript</label>

Radio (single-select)

<label><input class="toggle" type="radio" name="toggle" checked> HTML</label><br>
<label><input class="toggle" type="radio" name="toggle"> CSS</label><br>
<label><input class="toggle" type="radio" name="toggle"> JavaScript</label>

</form>

### Select

<form>
  <label>
    Label<br>
    <select>
      <option value="Earth">Select a planet...</option>
      <option value="Earth">Earth</option>
      <option value="Jupiter">Jupiter</option>
      <option value="Mars">Mars</option>
      <option value="Mercury">Mercury</option>
      <option value="Neptune">Neptune</option>
      <option value="Saturn">Saturn</option>
      <option value="Uranus">Uranus</option>
      <option value="Venus">Venus</option>
    </select>
  </label>
</form>

### Textarea

<textarea rows="5" cols="40">
Ipsam totam tempora. Dolorum voluptas error tempore asperiores vitae error laboriosam autem possimus.
</textarea>

## Headings

# Heading 1 {docsify-ignore}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse luctus nulla eu ex varius, a varius elit tincidunt. Aenean arcu magna, gravida id purus a, interdum convallis turpis. Aenean id ipsum eu tortor sollicitudin scelerisque in quis elit.

## Heading 2 {docsify-ignore}

Vestibulum lobortis laoreet nunc vel vulputate. In et augue non lectus pellentesque molestie et ac justo. Sed sed turpis ut diam gravida sagittis nec at neque. Vivamus id tellus est. Nam ac dignissim mi. Vestibulum nec sem convallis, condimentum augue at, commodo diam.

### Heading 3 {docsify-ignore}

Suspendisse sit amet tincidunt nibh, ac interdum velit. Ut orci diam, dignissim at enim sit amet, placerat rutrum magna. Mauris consectetur nibh eget sem feugiat, sit amet congue quam laoreet. Curabitur sed massa metus.

#### Heading 4 {docsify-ignore}

Donec odio orci, facilisis ac vehicula in, vestibulum ut urna. Ut bibendum ullamcorper risus, ac euismod leo maximus sed. In pulvinar sagittis rutrum. Morbi quis cursus diam. Cras ac laoreet nulla, rhoncus sodales dui.

##### Heading 5 {docsify-ignore}

Commodo sit veniam nulla cillum labore ullamco aliquip quis. Consequat nulla fugiat consequat ex duis proident. Adipisicing excepteur tempor exercitation ad. Consectetur voluptate Lorem sint elit exercitation ullamco dolor.

###### Heading 6 {docsify-ignore}

Ipsum ea amet dolore mollit incididunt fugiat nulla laboris est sint voluptate. Ex culpa id amet ipsum amet pariatur ipsum officia sit laborum irure ullamco deserunt. Consequat qui tempor occaecat nostrud proident.

## Horizontal Rule

Text before rule.

---

Text after rule.

## IFrame

[Example](_media/example.html ':include height=200px')

## Images

#### Inline-style

![Docsify Logo](/_media/icon.svg 'This is the Docsify logo!')

#### Reference-style

![Docsify Logo][logo]

[logo]: /_media/icon.svg 'This is the Docsify logo!'

#### Light / Dark Theme

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="_media/moon.svg">
  <source media="(prefers-color-scheme: light)" srcset="_media/sun.svg">
  <img alt="BinaryTree" src="_media/sun.svg" width="122">
</picture>

## Keyboard

#### Default

<kbd>&#8963;</kbd><kbd>&#8997;</kbd><kbd>&#9003;</kbd>

<kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>Del</kbd>

<kbd>&#8963; Control</kbd><kbd>&#8997; Alt</kbd><kbd>&#9003; Delete</kbd>

#### Alternate

<kbd class="alt">&#8963;</kbd><kbd class="alt">&#8997;</kbd><kbd class="alt">&#9003;</kbd>

<kbd class="alt">Ctrl</kbd><kbd class="alt">Alt</kbd><kbd class="alt">Del</kbd>

<kbd class="alt">&#8963; Control</kbd><kbd class="alt">&#8997; Alt</kbd><kbd class="alt">&#9003; Delete</kbd>

#### Entities

<div style="display: grid; grid-template-columns: auto auto 1fr; gap: 1em 0.2em; align-items: end;">
  <div><kbd class="alt">↑</kbd></div>  <div><kbd>↑</kbd></div>  <div>Arrow Up</div>
  <div><kbd class="alt">↓</kbd></div>  <div><kbd>↓</kbd></div>  <div>Arrow Down</div>
  <div><kbd class="alt">←</kbd></div>  <div><kbd>←</kbd></div>  <div>Arrow Left</div>
  <div><kbd class="alt">→</kbd></div>  <div><kbd>→</kbd></div>  <div>Arrow Right</div>
  <div><kbd class="alt">&#8682;</kbd></div> <div><kbd>&#8682;</kbd></div> <div>Caps Lock</div>
  <div><kbd class="alt">&#8984;</kbd></div> <div><kbd>&#8984;</kbd></div> <div>Command</div>
  <div><kbd class="alt">&#8963;</kbd></div> <div><kbd>&#8963;</kbd></div> <div>Control</div>
  <div><kbd class="alt">&#9003;</kbd></div> <div><kbd>&#9003;</kbd></div> <div>Delete</div>
  <div><kbd class="alt">&#8998;</kbd></div> <div><kbd>&#8998;</kbd></div> <div>Delete (Forward)</div>
  <div><kbd class="alt">&#8600;</kbd></div> <div><kbd>&#8600;</kbd></div> <div>End</div>
  <div><kbd class="alt">&#8996;</kbd></div> <div><kbd>&#8996;</kbd></div> <div>Enter</div>
  <div><kbd class="alt">&#9099;</kbd></div> <div><kbd>&#9099;</kbd></div> <div>Escape</div>
  <div><kbd class="alt">&#8598;</kbd></div> <div><kbd>&#8598;</kbd></div> <div>Home</div>
  <div><kbd class="alt">&#8670;</kbd></div> <div><kbd>&#8670;</kbd></div> <div>Page Up</div>
  <div><kbd class="alt">&#8671;</kbd></div> <div><kbd>&#8671;</kbd></div> <div>Page Down</div>
  <div><kbd class="alt">&#8997;</kbd></div> <div><kbd>&#8997;</kbd></div> <div>Option, Alt</div>
  <div><kbd class="alt">&#8629;</kbd></div> <div><kbd>&#8629;</kbd></div> <div>Return</div>
  <div><kbd class="alt">&#8679;</kbd></div> <div><kbd>&#8679;</kbd></div> <div>Shift</div>
  <div><kbd class="alt">&#9251;</kbd></div> <div><kbd>&#9251;</kbd></div> <div>Space</div>
  <div><kbd class="alt">&#8677;</kbd></div> <div><kbd>&#8677;</kbd></div> <div>Tab</div>
  <div><kbd class="alt">&#8676;</kbd></div> <div><kbd>&#8676;</kbd></div> <div>Tab + Shift</div>
 </div>

## Links

[Inline link](https://google.com)

[Inline link with title](https://google.com 'Google')

[Reference link by name][link1]

[Reference link by number][1]

[Reference link by self]

[link1]: https://google.com
[1]: https://google.com
[Reference link by self]: https://google.com

## Lists

### Ordered List

1. Ordered
1. Ordered
   1. Nested
   1. Nested (Wrapping): Similique tempora et. Voluptatem consequuntur ut. Rerum minus et sed beatae. Consequatur ut nemo laboriosam quo architecto quia qui. Corrupti aut omnis velit.
1. Ordered (Wrapping): Error minima modi rem sequi facere voluptatem. Est nihil veritatis doloribus et corporis ipsam. Pariatur eos ipsam qui odit labore est voluptatem enim. Veritatis est qui ut pariatur inventore.

### Unordered List

- Unordered
- Unordered
  - Nested
  - Nested (Wrapping): Quia consectetur sint vel ut excepturi ipsa voluptatum suscipit hic. Ipsa error qui molestiae harum laboriosam. Rerum non amet illo voluptatem odio pariatur. Ut minus enim.
- Unordered (Wrapping): Fugiat qui tempore ratione amet repellendus repudiandae non. Rerum nisi officia enim. Itaque est alias voluptatibus id molestiae accusantium. Cupiditate sequi qui omnis sed facere aliquid quia ut.

### Task List

- [x] Task
- [ ] Task
  - [ ] Subtask
  - [ ] Subtask
  - [x] Subtask
- [ ] Task (Wrapping): Earum consequuntur itaque numquam sunt error omnis ipsum repudiandae. Est assumenda neque eum quia quisquam laborum beatae autem ad. Fuga fugiat perspiciatis harum quia dignissimos molestiae. Officia quo eveniet tempore modi voluptates consequatur. Eum odio adipisci labore.
  - [x] Subtask (Wrapping): Vel possimus eaque laborum. Voluptates qui debitis quaerat atque molestiae quia explicabo doloremque. Reprehenderit perspiciatis a aut impedit temporibus aut quasi quia. Incidunt sed recusandae vitae asperiores sit in.

## Output

<output data-lang="output">
  <p>Et cum fugiat nesciunt voluptates. A atque quos doloribus dolorem quo. Et dignissimos omnis nam. Recusandae voluptatem nam. Tenetur veniam et qui consequatur. Aut sequi atque fuga itaque iusto eum nihil quod iure.</p>
  <ol>
    <li>Item</li>
    <li>Item</li>
    <li>Item</li>
  </ol>
</output>

## Tables

### Alignment

| Left Align | Center Align | Right Align | Non&#8209;Breaking Header |
| ---------- | :----------: | ----------: | ------------------------------ |
| A1         |      A2      |          A3 | A4                             |
| B1         |      B2      |          B3 | B4                             |
| C1         |      C2      |          C3 | C4                             |

### Headerless

|     |     |     |     |
| --- | --- | --- | --- |
| A1  | A2  | A3  | A4  |
| B1  | B2  | B3  | B4  |
| C1  | C2  | C3  | C4  |

### Scrolling

| Header                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Dicta in nobis dolor adipisci qui. Accusantium voluptates est dolor laboriosam qui voluptatibus. Veritatis eos aspernatur iusto et dicta quas. Fugit voluptatem dolorum qui quisquam. nihil |
| Aut praesentium officia aut delectus. Quas atque reprehenderit saepe. Et voluptatibus qui dolores rem facere in dignissimos id aut. Debitis excepturi delectus et quos numquam magnam.      |
| Sed eum atque at laborum aut et repellendus ullam dolor. Cupiditate saepe voluptatibus odit est pariatur qui. Hic sunt nihil optio enim eum laudantium. Repellendus voluptate.              |

## Text Elements

<mark>Marked text</mark>

<pre>Preformatted text</pre>

<samp>Sample Output</samp>

<small>Small Text</small>

This is <sub>subscript</sub>

This is <sup>superscript</sup>

<ins>Underlined Text</ins>

## Text Styles

Body text

**Bold text**

_Italic text_

**_Bold and italic text_**

~~Strikethrough~~
```

[Blockquotes](#/ui-kit?id=blockquotes)
--------------------------------------

> Cras aliquet nulla quis metus tincidunt, sed placerat enim cursus. Etiam
> turpis nisl, posuere eu condimentum ut, interdum a risus. Sed non luctus mi.
> Quisque malesuada risus sit amet tortor aliquet, a posuere ex iaculis. Vivamus
> ultrices enim dui, eleifend porttitor elit aliquet sed.
>
> *- Quote Source*

#### [Nested](#/ui-kit?id=nested)

> Level 1
>
> > Level 2
> >
> > > Level 3

[Buttons](#/ui-kit?id=buttons)
------------------------------

#### [Default](#/ui-kit?id=default)

Button

#### [Basic](#/ui-kit?id=basic)

Button
Link Button

#### [Primary](#/ui-kit?id=primary)

Button
Link Button

#### [Secondary](#/ui-kit?id=secondary)

Button
Link Button

[Callouts](#/ui-kit?id=callouts)
--------------------------------

**Caution** callout with `inline code`.

**Important** callout with `inline code`.

**Note** callout with `inline code`.

**Tip** callout with `inline code`.

**Warning** callout with `inline code`.

**Multi Line**

* List item 1
* List item 2

Text

```
<p>Hello, World!</p>
```

**Nested**

Level 1

Level 2

Level 3

**Legacy Style**

Legacy **Important** callout with `inline code`.

Legacy **Tip** with `inline code`.

[Code](#/ui-kit?id=code)
------------------------

This is `inline code`

```
const add = (num1, num2) => num1 + num2;
const total = add(1, 2);

console.log(total); // 3
```

```
<body>
  <p>Hello</p>
</body>
```

[Colors](#/ui-kit?id=colors)
----------------------------

#### [Theme](#/ui-kit?id=theme)

1



2



3



4



Theme Color



5



6



7



8

#### [Monochromatic](#/ui-kit?id=monochromatic)

Min



1



2



3



4



5



6



7



8



9



Max

[Details](#/ui-kit?id=details)
------------------------------

Details (click to open)

Suscipit nemo aut ex suscipit voluptatem laboriosam odio velit. Ipsum eveniet labore sequi non optio vel. Ut culpa ad accusantium est aut harum ipsam voluptatum. Velit eum incidunt non sint. Et molestiae veniam natus autem vel assumenda ut numquam esse. Non nisi id qui vero corrupti quos et.

Details (open by default)

Suscipit nemo aut ex suscipit voluptatem laboriosam odio velit. Ipsum eveniet labore sequi non optio vel. Ut culpa ad accusantium est aut harum ipsam voluptatum. Velit eum incidunt non sint. Et molestiae veniam natus autem vel assumenda ut numquam esse. Non nisi id qui vero corrupti quos et.

[Form Elements](#/ui-kit?id=form-elements)
------------------------------------------

### [Fieldset](#/ui-kit?id=fieldset)

Legend

Label

### [Input](#/ui-kit?id=input)

#### [Checkbox](#/ui-kit?id=checkbox)

 HTML  
 CSS  
 JavaScript

#### [Datalist](#/ui-kit?id=datalist)

Label  


Earth
Jupiter
Mars
Mercury
Neptune
Saturn
Uranus
Venus

#### [Radio](#/ui-kit?id=radio)

 HTML  
 CSS  
 JavaScript

#### [Text](#/ui-kit?id=text)

First name  

#### [Toggles](#/ui-kit?id=toggles)

Checkbox (multi-select)

HTML  
 CSS  
 JavaScript

Radio (single-select)

HTML  
 CSS  
 JavaScript

### [Select](#/ui-kit?id=select)

Label  

Select a planet...
Earth
Jupiter
Mars
Mercury
Neptune
Saturn
Uranus
Venus

### [Textarea](#/ui-kit?id=textarea)

Ipsam totam tempora. Dolorum voluptas error tempore asperiores vitae error laboriosam autem possimus.

[Headings](#/ui-kit?id=headings)
--------------------------------

[Heading 1](#/ui-kit?id=heading-1-docsify-ignore)
=================================================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse luctus nulla eu ex varius, a varius elit tincidunt. Aenean arcu magna, gravida id purus a, interdum convallis turpis. Aenean id ipsum eu tortor sollicitudin scelerisque in quis elit.

[Heading 2](#/ui-kit?id=heading-2-docsify-ignore)
-------------------------------------------------

Vestibulum lobortis laoreet nunc vel vulputate. In et augue non lectus pellentesque molestie et ac justo. Sed sed turpis ut diam gravida sagittis nec at neque. Vivamus id tellus est. Nam ac dignissim mi. Vestibulum nec sem convallis, condimentum augue at, commodo diam.

### [Heading 3](#/ui-kit?id=heading-3-docsify-ignore)

Suspendisse sit amet tincidunt nibh, ac interdum velit. Ut orci diam, dignissim at enim sit amet, placerat rutrum magna. Mauris consectetur nibh eget sem feugiat, sit amet congue quam laoreet. Curabitur sed massa metus.

#### [Heading 4](#/ui-kit?id=heading-4-docsify-ignore)

Donec odio orci, facilisis ac vehicula in, vestibulum ut urna. Ut bibendum ullamcorper risus, ac euismod leo maximus sed. In pulvinar sagittis rutrum. Morbi quis cursus diam. Cras ac laoreet nulla, rhoncus sodales dui.

##### [Heading 5](#/ui-kit?id=heading-5-docsify-ignore)

Commodo sit veniam nulla cillum labore ullamco aliquip quis. Consequat nulla fugiat consequat ex duis proident. Adipisicing excepteur tempor exercitation ad. Consectetur voluptate Lorem sint elit exercitation ullamco dolor.

###### [Heading 6](#/ui-kit?id=heading-6-docsify-ignore)

Ipsum ea amet dolore mollit incididunt fugiat nulla laboris est sint voluptate. Ex culpa id amet ipsum amet pariatur ipsum officia sit laborum irure ullamco deserunt. Consequat qui tempor occaecat nostrud proident.

[Horizontal Rule](#/ui-kit?id=horizontal-rule)
----------------------------------------------

Text before rule.

---

Text after rule.

[IFrame](#/ui-kit?id=iframe)
----------------------------

[Images](#/ui-kit?id=images)
----------------------------

#### [Inline-style](#/ui-kit?id=inline-style)

![Docsify Logo](/_media/icon.svg "This is the Docsify logo!")

#### [Reference-style](#/ui-kit?id=reference-style)

![Docsify Logo](/_media/icon.svg "This is the Docsify logo!")

#### [Light / Dark Theme](#/ui-kit?id=light--dark-theme)

![BinaryTree](_media/sun.svg)

[Keyboard](#/ui-kit?id=keyboard)
--------------------------------

#### [Default](#/ui-kit?id=default-1)

`⌃``⌥``⌫`

`Ctrl``Alt``Del`

`⌃ Control``⌥ Alt``⌫ Delete`

#### [Alternate](#/ui-kit?id=alternate)

`⌃``⌥``⌫`

`Ctrl``Alt``Del`

`⌃ Control``⌥ Alt``⌫ Delete`

#### [Entities](#/ui-kit?id=entities)

`↑`

`↑`

Arrow Up

`↓`

`↓`

Arrow Down

`←`

`←`

Arrow Left

`→`

`→`

Arrow Right

`⇪`

`⇪`

Caps Lock

`⌘`

`⌘`

Command

`⌃`

`⌃`

Control

`⌫`

`⌫`

Delete

`⌦`

`⌦`

Delete (Forward)

`↘`

`↘`

End

`⌤`

`⌤`

Enter

`⎋`

`⎋`

Escape

`↖`

`↖`

Home

`⇞`

`⇞`

Page Up

`⇟`

`⇟`

Page Down

`⌥`

`⌥`

Option, Alt

`↵`

`↵`

Return

`⇧`

`⇧`

Shift

`␣`

`␣`

Space

`⇥`

`⇥`

Tab

`⇤`

`⇤`

Tab + Shift

[Links](#/ui-kit?id=links)
--------------------------

[Inline link](https://google.com)

[Inline link with title](https://google.com "Google")

[Reference link by name](https://google.com)

[Reference link by number](https://google.com)

[Reference link by self](https://google.com)

[Lists](#/ui-kit?id=lists)
--------------------------

### [Ordered List](#/ui-kit?id=ordered-list)

1. Ordered
2. Ordered
   1. Nested
   2. Nested (Wrapping): Similique tempora et. Voluptatem consequuntur ut. Rerum minus et sed beatae. Consequatur ut nemo laboriosam quo architecto quia qui. Corrupti aut omnis velit.
3. Ordered (Wrapping): Error minima modi rem sequi facere voluptatem. Est nihil veritatis doloribus et corporis ipsam. Pariatur eos ipsam qui odit labore est voluptatem enim. Veritatis est qui ut pariatur inventore.

### [Unordered List](#/ui-kit?id=unordered-list)

* Unordered
* Unordered
  + Nested
  + Nested (Wrapping): Quia consectetur sint vel ut excepturi ipsa voluptatum suscipit hic. Ipsa error qui molestiae harum laboriosam. Rerum non amet illo voluptatem odio pariatur. Ut minus enim.
* Unordered (Wrapping): Fugiat qui tempore ratione amet repellendus repudiandae non. Rerum nisi officia enim. Itaque est alias voluptatibus id molestiae accusantium. Cupiditate sequi qui omnis sed facere aliquid quia ut.

### [Task List](#/ui-kit?id=task-list)

* Task
* Task
  + Subtask
  + Subtask
  + Subtask
* Task (Wrapping): Earum consequuntur itaque numquam sunt error omnis ipsum repudiandae. Est assumenda neque eum quia quisquam laborum beatae autem ad. Fuga fugiat perspiciatis harum quia dignissimos molestiae. Officia quo eveniet tempore modi voluptates consequatur. Eum odio adipisci labore.
  + Subtask (Wrapping): Vel possimus eaque laborum. Voluptates qui debitis quaerat atque molestiae quia explicabo doloremque. Reprehenderit perspiciatis a aut impedit temporibus aut quasi quia. Incidunt sed recusandae vitae asperiores sit in.

[Output](#/ui-kit?id=output)
----------------------------

Et cum fugiat nesciunt voluptates. A atque quos doloribus dolorem quo. Et dignissimos omnis nam. Recusandae voluptatem nam. Tenetur veniam et qui consequatur. Aut sequi atque fuga itaque iusto eum nihil quod iure.

1. Item
2. Item
3. Item

[Tables](#/ui-kit?id=tables)
----------------------------

### [Alignment](#/ui-kit?id=alignment)

| Left Align | Center Align | Right Align | Non‑Breaking Header |
| --- | --- | --- | --- |
| A1 | A2 | A3 | A4 |
| B1 | B2 | B3 | B4 |
| C1 | C2 | C3 | C4 |

### [Headerless](#/ui-kit?id=headerless)

|  |  |  |  |
| --- | --- | --- | --- |
| A1 | A2 | A3 | A4 |
| B1 | B2 | B3 | B4 |
| C1 | C2 | C3 | C4 |

### [Scrolling](#/ui-kit?id=scrolling)

| Header |
| --- |
| Dicta in nobis dolor adipisci qui. Accusantium voluptates est dolor laboriosam qui voluptatibus. Veritatis eos aspernatur iusto et dicta quas. Fugit voluptatem dolorum qui quisquam. nihil |
| Aut praesentium officia aut delectus. Quas atque reprehenderit saepe. Et voluptatibus qui dolores rem facere in dignissimos id aut. Debitis excepturi delectus et quos numquam magnam. |
| Sed eum atque at laborum aut et repellendus ullam dolor. Cupiditate saepe voluptatibus odit est pariatur qui. Hic sunt nihil optio enim eum laudantium. Repellendus voluptate. |

[Text Elements](#/ui-kit?id=text-elements)
------------------------------------------

Marked text

```
Preformatted text
```

`Sample Output`

Small Text

This is subscript

This is superscript

Underlined Text

[Text Styles](#/ui-kit?id=text-styles)
--------------------------------------

Body text

**Bold text**

*Italic text*

***Bold and italic text***

~~Strikethrough~~

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/ui-kit.md)

Example HTML Page