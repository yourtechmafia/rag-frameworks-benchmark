Skip to main content




Clear search

`/`
`⌃K`

[go-echarts](/go-echarts/)
==========================

![](https://user-images.githubusercontent.com/19553554/52535979-c0d0e680-2d8f-11e9-85c8-2e9f659e7c6f.png)

go-echarts
==========

*🎨 The adorable charts library for Golang.*

[🔰 Installation](#/en-us/?id=%f0%9f%94%b0-installation)
=======================================================

[gomod](#/en-us/?id=gomod)
--------------------------

```
$ go get -u github.com/go-echarts/go-echarts/v2/...
```

OR

```
# go.mod

require github.com/go-echarts/go-echarts/v2
```

[classic to get go-echarts](#/en-us/?id=classic-to-get-go-echarts)
------------------------------------------------------------------

```
# this may be a crude way to use v2 go-echarts without gomod(GO111MODULE=off)

$ go get -u github.com/go-echarts/go-echarts/...
$ cd $go-echarts-project
$ mkdir v2 && mv charts components datasets opts render templates types v2
```

[⏳ Version Control](#/en-us/?id=%e2%8f%b3-version-control)
==========================================================

The go-echarts project is being developed under v2 version and the active codebase is on the master branch.

v1 and v2 are incompatible which means that you cannot upgrade go-echarts from v1 to v2 smoothly. But I think it is
worth trying that new version.

Especially, when there contains mino changes (usually in enhancement), we will release the `rc` version before a
standard
release.
So, if you upgrade your projects cross the `rc` versions, maybe
need little adjust.

[✨ Features](#/en-us/?id=%e2%9c%a8-features)
============================================

* Clean and comprehensive API.
* Visualize your data in 25+ different ways.
* Highly configurable chart options.
* Detailed documentation and a rich collection of examples.
* Visualize your geographical data with 400+ maps.

[💡 Contribution](#/en-us/?id=%f0%9f%92%a1-contribution)
=======================================================

go-echarts is an open source project and built on the top of other open-source projects.
Welcome all the kinds of contributions. No matter it is for typo fix, bug fix or big new features.
Please do not hesitate to ask a question or send a pull request.

We strongly value documentation and integration with other projects, so we are very glad to accept improvements for
these aspects.

---