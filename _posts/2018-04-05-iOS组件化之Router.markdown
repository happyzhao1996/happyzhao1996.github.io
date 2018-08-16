---
layout: post
title:  "iOS组件化之Router"
date:   2018-07-11 16:20:33 +0800
categories: iOS开发
tags: 路由 组件化 Router
---

随着用户的需求越来越多，对App的用户体验也变的要求越来越高。为了更好的应对各种需求，开发人员从软件工程的角度，将App架构由原来简单的MVC变成MVVM，VIPER等复杂架构。更换适合业务的架构，是为了后期能更好的维护项目。

但是用户依旧不满意，继续对开发人员提出了更多更高的要求，不仅需要高质量的用户体验，还要求快速迭代，最好一天出一个新功能，而且用户还要求不更新就能体验到新功能。为了满足用户需求，于是开发人员就用H5，ReactNative，Weex等技术对已有的项目进行改造。项目架构也变得更加的复杂，纵向的会进行分层，网络层，UI层，数据持久层。每一层横向的也会根据业务进行组件化。尽管这样做了以后会让开发更加有效率，更加好维护，但是如何解耦各层，解耦各个界面和各个组件，降低各个组件之间的耦合度，如何能让整个系统不管多么复杂的情况下都能保持“高内聚，低耦合”的特点？这一系列的问题都摆在开发人员面前，亟待解决。今天就来谈谈解决这个问题的一些思路。



在 universal links 出现之前的很长一段时间里，iOS 上主要通过 custom URL scheme 来实现 deep linking，以及 app 间的通信。在处理复杂的业务逻辑时，需要维护URL handler，这里就需要引入router 来分发请求。关于 router 已经有很多文章涉及，GitHub 上也有很多开源代码可供参考或使用，比如：

- [DeepLinkKit](https://github.com/usebutton/DeepLinkKit)
- [JLRoutes](https://github.com/joeldev/JLRoutes)
- [Routable](https://github.com/clayallsopp/routable-ios)
- [HHRouter](https://github.com/Huohua/HHRouter)



### **Universal Links**

Apple 在 iOS 9 上引入了 universal links，相较 custom URL scheme，universal links 有以下好处：

- Custom URL scheme 因为是自定义的协议，所以在没有安装 app 的情况下是无法直接打开的，而 universal links 本身是一个 HTTP/HTTPS 链接，所以有更好的兼容性。
- 不同的 app 是可以定义相同的 custom URL scheme 的，所以会存在抢占或冲突的问题，而 universal links 是从 server 查询由哪个 app 打开的，所以不存在上述问题。
- Universal links 支持从其他 app 的 MKWebView 或 UIWebView 中跳转到目标 app。
- Universal links 本身可以被搜索引擎索引。

Universal links 的具体实现可以参考官方文档：[Support Universal Links](https://developer.apple.com/library/ios/documentation/General/Conceptual/AppSearch/UniversalLinks.html#//apple_ref/doc/uid/TP40016308-CH12-SW1)。简单来说你需要：

- 添加一个 `apple-app-site-association` 文件到你的网站来描述 URL 和 app 的关联。
- 添加 `com.apple.developer.associated-domains` entitlement 来指定要从哪些域名查询 universal links support。
- 在 app delegate 的 `application:continueUserActivity:restorationHandler:` 方法中 handle `userActivity.webpageURL`。

处理 URL 本身的方法跟前面处理 custom URL 类似，不再赘述。