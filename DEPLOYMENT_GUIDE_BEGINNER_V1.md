# Beginner Deployment Guide v1

## 这份文档解决什么问题
这是一份给完全没部署经验的人用的上站说明。
目标不是讲原理，而是让你把当前静态站先发上去。

当前可发布目录：
- `projects/english-template-site/site`

## 最推荐方案
先用 **Cloudflare Pages**。
原因：
- 对静态站最简单
- 免费层够用
- 不需要先学服务器
- 后面绑域名也顺

## 你现在手里已经有什么
当前项目已经有可发布静态文件：
- `site/index.html`
- `site/status.html`
- `site/styles.css`
- `site/pages/*.html`

这意味着：
- 现在不需要先写后端
- 不需要先买服务器
- 先把 `site/` 发上去就能看到网页

## 上站前检查
先确认这 4 件事：

1. `site/pages/` 下有 4 个 html
2. `site/index.html` 存在
3. `site/styles.css` 存在
4. 首页里导航能点到 4 个页面

如果这 4 条都满足，就可以上。

## Cloudflare Pages 操作顺序

### 第 1 步：登录 Cloudflare
- 打开 Cloudflare
- 登录账号
- 没账号就注册一个

### 第 2 步：进入 Pages
- 进入左侧 `Workers & Pages`
- 点 `Create`
- 选 `Pages`

### 第 3 步：决定怎么上传
你有两种方式：

#### 方式 A：直接上传目录
适合现在，最快。

#### 方式 B：连接 Git 仓库
适合后面持续更新。

这轮先用 **方式 A**，别复杂化。

### 第 4 步：上传目录
- 选择上传本地文件/目录
- 上传目录指向：
  - `projects/english-template-site/site`

注意：
- 上传的是 `site` 目录里的内容
- 不是整个 `english-template-site`

### 第 5 步：等待构建完成
静态站一般很快。
如果 Pages 问构建命令：
- 可以先留空
- 或选择“无构建命令”

因为你现在上传的是已经生成好的静态文件。

### 第 6 步：打开分配的网址
发布成功后，Cloudflare 会给你一个默认域名。
打开后检查：
- 首页能不能打开
- 4 个页面能不能点开
- 样式有没有丢

## 如果样式丢了怎么办
先检查：
- `styles.css` 有没有一起上传
- 页面里是不是引用 `/styles.css`

如果首页能开但没样式，通常就是：
- 上传目录错了
- 或 `styles.css` 没带上

## 如果页面点不开怎么办
先检查：
- `site/pages/` 目录下的 4 个 html 有没有一起上传
- 首页里的链接是不是 `/pages/xxx.html`

## 域名什么时候再绑
先别急。
顺序应该是：
1. 先把默认域名跑通
2. 确认网页能正常访问
3. 再绑自定义域名

这样最稳。

## 这轮先不做的事
- 不先接 analytics
- 不先接 Search Console
- 不先做 sitemap
- 不先做自动部署

原因：
- 现在最重要的是先把站点真正发出去
- 不是一开始就把所有外围配置堆满

## 发布成功后的下一步
发布成功后，再补这三件事：
1. 自定义域名
2. Search Console
3. sitemap / robots / 基础追踪

## 一句话流程
- 先上传 `site/`
- 先跑通默认域名
- 页面正常后再做域名和收录配置
