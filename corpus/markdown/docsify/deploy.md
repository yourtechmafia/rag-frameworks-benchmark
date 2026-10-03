Skip to main content

* Translations

  + [English](#/ "English")
  + [简体中文](#/zh-cn/ "简体中文")

Clear search

`/`
`⌃K`

[docsify](#/)
=============

[![ads via Carbon](https://srv.carbonads.net/static/30242/f3dc6d2c4c4ea6771977d883b7a49937b048390f)](https://srv.carbonads.net/ads/click/x/GTND4277C6YD42QLCKBLYKQUF6YIP27NCWSD4Z3JCAAI427JC6YICKJKC6YILK3MFT7D453UCEBDE53JCYADTKQMHEYI55QJCTYIEK3ECTNCYBZ52K)
[Get the Drop. Weekly front-end tools, tips, and resources.
Plus a free icon pack to get you started.](https://srv.carbonads.net/ads/click/x/GTND4277C6YD42QLCKBLYKQUF6YIP27NCWSD4Z3JCAAI427JC6YICKJKC6YILK3MFT7D453UCEBDE53JCYADTKQMHEYI55QJCTYIEK3ECTNCYBZ52K)
[ads via Carbon](http://carbonads.net/?utm_source=docsifyjsorg&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![ads via Carbon](https://insight.adsrvr.org/track/pxl/?adv=t3k9qrj&ct=0:djrfa1z&fmt=3&orderid=&v=)![ads via Carbon](https://ad.doubleclick.net/ddm/activity/src=15643656;type=sales;cat=408690;qty=1;cost=[Revenue];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;npa=;gdpr=$;gdpr_consent=$;ord=[OrderID]?)![ads via Carbon](https://sp.analytics.yahoo.com/spp.pl?a=10000&.yp=10207075&he=&hph=&gv=[ORDER_VALUE]&orderId=[ORDER_ID]&ec=[EVENT_CATEGORY]&ea=fire&el=[EVENT_LABEL])![ads via Carbon](https://secure.adnxs.com/seg?add=37012073&t=2)![ads via Carbon](https://secure.adnxs.com/px?id=1777282&t=2)![ads via Carbon](https://segment.prod.bidr.io/associate-segment?buzz_key=dsp&segment_key=dsp-19102)![ads via Carbon](https://cnv.event.prod.bidr.io/log/cnv?tag_id=3503&buzz_key=dsp&value=&account_id=79&order=[ORDER]&ord=[CACHEBUSTER])

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
    - [GitHub Pages](#/deploy?id=github-pages "GitHub Pages")
    - [GitLab Pages](#/deploy?id=gitlab-pages "GitLab Pages")
    - [Firebase Hosting](#/deploy?id=firebase-hosting "Firebase Hosting")
    - [Nginx](#/deploy?id=nginx "Nginx")
    - [Netlify](#/deploy?id=netlify "Netlify")
    - [Vercel](#/deploy?id=vercel "Vercel")
    - [AWS Amplify](#/deploy?id=aws-amplify "AWS Amplify")
    - [Stormkit](#/deploy?id=stormkit "Stormkit")
    - [Docker](#/deploy?id=docker "Docker")
    - [Kinsta Static Site Hosting](#/deploy?id=kinsta-static-site-hosting "Kinsta Static Site Hosting")
    - [DeployHQ](#/deploy?id=deployhq "DeployHQ")
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

[Deploy](#/deploy?id=deploy)
============================

Similar to [GitBook](https://www.gitbook.com), you can deploy files to GitHub Pages, GitLab Pages or VPS.

[GitHub Pages](#/deploy?id=github-pages)
----------------------------------------

There are three places to populate your docs for your GitHub repository:

* `docs/` folder
* main branch
* gh-pages branch

It is recommended that you save your files to the `./docs` subfolder of the `main` branch of your repository. Then select `main branch /docs folder` as your GitHub Pages source in your repository's settings page.

![GitHub Pages](/_images/deploy-github-pages.png)

You can also save files in the root directory and select `main branch`.
You'll need to place a `.nojekyll` file in the deploy location (such as `/docs` or the gh-pages branch)

[GitLab Pages](#/deploy?id=gitlab-pages)
----------------------------------------

If you are deploying your master branch, create a `.gitlab-ci.yml` with the following script:

The `.public` workaround is so `cp` doesn't also copy `public/` to itself in an infinite loop.

```
pages:
  stage: deploy
  script:
  - mkdir .public
  - cp -r * .public
  - mv .public public
  artifacts:
    paths:
    - public
  only:
  - master
```

You can replace script with `- cp -r docs/. public`, if `./docs` is your Docsify subfolder.

[Firebase Hosting](#/deploy?id=firebase-hosting)
------------------------------------------------

You'll need to install the Firebase CLI using `npm i -g firebase-tools` after signing into the [Firebase Console](https://console.firebase.google.com) using a Google Account.

Using a terminal, determine and navigate to the directory for your Firebase Project. This could be `~/Projects/Docs`, etc. From there, run `firebase init` and choose `Hosting` from the menu (use **space** to select, **arrow keys** to change options and **enter** to confirm). Follow the setup instructions.

Your `firebase.json` file should look similar to this (I changed the deployment directory from `public` to `site`):

```
{
  "hosting": {
    "public": "site",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"]
  }
}
```

Once finished, build the starting template by running `docsify init ./site` (replacing site with the deployment directory you determined when running `firebase init` - public by default). Add/edit the documentation, then run `firebase deploy` from the root project directory.

[Nginx](#/deploy?id=nginx)
--------------------------

Use the following Nginx configuration.

```
server {
  listen 80;
  server_name your.domain.com;

  location / {
    alias /path/to/dir/of/docs/;
    index index.html;
  }
}
```

If [`routerMode`](#/configuration?id=routermode) is set to `history`, use this configuration instead:

```
server {
  listen 80;
  server_name your.domain.com;

  root /path/to/dir/of/docs;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

[Netlify](#/deploy?id=netlify)
------------------------------

1. Login to your [Netlify](https://www.netlify.com/) account.
2. In the [dashboard](https://app.netlify.com/) page, click **Add New Site**.
3. Select GitHub.
4. Choose the repository where you store your docs, in the **Base Directory** add the subfolder where the files are stored. For example, it should be `docs`.
5. In the **Build Command** area leave it blank.
6. In the **Publish directory** area, if you have added the `docs` in the **Base Directory** you will see the publish directory populated with `docs/`
7. Netlify is smart enough to look for the the `index.html` file inside the `docs/` folder.

### [HTML5 router](#/deploy?id=html5-router)

When using the HTML5 router, you need to set up redirect rules that redirect all requests to your `index.html`. It's pretty simple when you're using Netlify. Just create a file named `_redirects` in the docs directory, add this snippet to the file, and you're all set:

```
/*    /index.html   200
```

[Vercel](#/deploy?id=vercel)
----------------------------

1. Install [Vercel CLI](https://vercel.com/download), `npm i -g vercel`
2. Change directory to your docsify website, for example `cd docs`
3. Deploy with a single command, `vercel`

[AWS Amplify](#/deploy?id=aws-amplify)
--------------------------------------

1. Set the routerMode in the Docsify project `index.html` to *history* mode.

```
<script>
  window.$docsify = {
    loadSidebar: true,
    routerMode: 'history',
  };
</script>
```

2. Login to your [AWS Console](https://aws.amazon.com).
3. Go to the [AWS Amplify Dashboard](https://aws.amazon.com/amplify).
4. Choose the **Deploy** route to setup your project.
5. When prompted, keep the build settings empty if you're serving your docs within the root directory. If you're serving your docs from a different directory, customise your amplify.yml

```
version: 0.1
frontend:
  phases:
    build:
      commands:
        - echo "Nothing to build"
  artifacts:
    baseDirectory: /docs
    files:
      - '**/*'
  cache:
    paths: []
```

6. Add the following Redirect rules in their displayed order. Note that the second record is a PNG image where you can change it with any image format you are using.

| Source address | Target address | Type |
| --- | --- | --- |
| /<\*>.md | /<\*>.md | 200 (Rewrite) |
| /<\*>.png | /<\*>.png | 200 (Rewrite) |
| /<\*> | /index.html | 200 (Rewrite) |

[Stormkit](#/deploy?id=stormkit)
--------------------------------

1. Login to your [Stormkit](https://www.stormkit.io) account.
2. Using the user interface, import your docsify project from one of the three supported Git providers (GitHub, GitLab, or Bitbucket).
3. Navigate to the project’s production environment in Stormkit or create a new environment if needed.
4. Verify the build command in your Stormkit configuration. By default, Stormkit CI will run `npm run build` but you can specify a custom build command on this page.
5. Set output folder to `docs`
6. Click the “Deploy Now” button to deploy your site.

Read more in the [Stormkit Documentation](https://stormkit.io/docs).

[Docker](#/deploy?id=docker)
----------------------------

* Create docsify files

  You need prepare the initial files instead of making them inside the container.
  See the [Quickstart](https://docsify.js.org/#/quickstart) section for instructions on how to create these files manually or using [docsify-cli](https://github.com/docsifyjs/docsify-cli).

  ```
  index.html
  README.md
  ```
* Create Dockerfile

  ```
    FROM node:latest
    LABEL description="A demo Dockerfile for build Docsify."
    WORKDIR /docs
    RUN npm install -g docsify-cli@latest
    EXPOSE 3000/tcp
    ENTRYPOINT docsify serve .
  ```

  The current directory structure should be this:

  ```
   index.html
   README.md
   Dockerfile
  ```
* Build docker image

  ```
  docker build -f Dockerfile -t docsify/demo .
  ```
* Run docker image

  ```
  docker run -itp 3000:3000 --name=docsify -v $(pwd):/docs docsify/demo
  ```

[Kinsta Static Site Hosting](#/deploy?id=kinsta-static-site-hosting)
--------------------------------------------------------------------

You can deploy **Docsify** as a Static Site on [Kinsta](https://kinsta.com/static-site-hosting/).

1. Login or create an account to view your [MyKinsta](https://my.kinsta.com/) dashboard.
2. Authorize Kinsta with your Git provider.
3. Select **Static Sites** from the left sidebar and press **Add sites**.
4. Select the repository and branch you want to deploy.
5. During the build settings, Kinsta will automatically try to fill out the **Build command**, **Node version**, and **Publish directory**. If it won't, fill out the following:

   * Build command: leave empty
   * Node version: leave on default selection or a specific version (e.g. `18.16.0`)
   * Publish directory: `docs`
6. Click the **Create site**.

[DeployHQ](#/deploy?id=deployhq)
--------------------------------

[DeployHQ](https://www.deployhq.com/) is a deployment automation platform that deploys your code to SSH/SFTP servers, FTP servers, cloud storage (Amazon S3, Cloudflare R2), and modern hosting platforms (Netlify, Heroku).

DeployHQ does not host your site. It automates deploying your Docsify files to your chosen hosting provider or server.

To deploy your Docsify site using DeployHQ:

1. Sign up for a [DeployHQ account](https://www.deployhq.com/) and verify your email.
2. Create your first project by clicking on **Projects** and **New Project**. Connect your Git repository (GitHub, GitLab, Bitbucket, or any private repository). Authorize DeployHQ to access your repository.
3. Add a server and enter your server details:

   * Give your server a name
   * Select your protocol (SSH/SFTP, FTP, or cloud platform)
   * Enter your server hostname, username, and password/SSH key
   * Set **Deployment Path** to your web root (e.g., `public_html/`)
4. Since Docsify doesn't require a build step, you can deploy your files directly. If your Docsify files are in a `docs/` folder, configure the **Source Path** in your server settings to `docs/`.
5. Click **Deploy Project**, then select your server and click **Deploy** to start your first deployment.

Your Docsify site will be deployed to your server. You can enable automatic deployments to deploy on every Git push, or schedule deployments for specific times.

For more information on advanced deployment features, see [DeployHQ's documentation](https://www.deployhq.com/support).

---

Powered by [Docsify.js](/)
[![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png?v8.png) Edit Page](https://github.com/docsifyjs/docsify/blob/develop/docs/deploy.md)