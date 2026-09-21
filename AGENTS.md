# AGENTS.md — AI 协作必读（任何窗口开工前先读这个文件）

> 本仓库由多个 AI 窗口并行维护。不遵守本文件规则会直接覆盖别人的工作或让构建失败。

## 1. 这个项目是什么

- 英文简历内容站 `resumepathlab.com`，托管在 Cloudflare Pages
- 目标：通过 Google AdSense 审核 + 联盟营销（Kickresume/ResumeGenius/Zety）
- 受众：美国 entry-level / 无经验求职者（ML、软件、数据方向）
- 内容全部英文；协作者之间的交流用中文

## 2. 技术结构与命令

```
pages/*.md      → 指南源稿（Markdown，11 篇）
legal/*.md      → 合规页源稿（about/contact/privacy-policy/terms/disclaimer）
build_site.py   → 构建脚本：Markdown → 静态 HTML
validate_build.py → 构建后校验（schema/FAQ/CTA/canonical）
site/           → 构建产物（已提交进仓库，Cloudflare Pages 发布的就是它）
site/downloads/ → Word 模板 docx
site/assets/og/ → OG 分享图（每页一张 1200x630 png，没有则自动回退 home.png）
```

```bash
python build_site.py       # 构建（改完任何 md 或 py 后必须跑）
python validate_build.py   # 校验
```

## 3. 部署机制（重要）

- **push 到 `main` 分支 ≈ 1 分钟后自动上线**（Cloudflare Pages 连着 GitHub）
- **不想上线就推到功能分支**：`git push origin window-X-主题`，不要 merge
- 上线前务必本地 `python build_site.py` 跑通并提交 `site/` 产物

## 4. 并行协作规则（防撞车）

1. **开工前先 `git pull origin main`**，拿到最新状态
2. 每个窗口一个功能分支，命名 `window-编号-主题`，如 `window-2-cover-letters`
3. 完工后：`git pull --rebase origin main` → 跑构建 → 再 push
4. push 被拒（non-fast-forward）= 有别人推了新东西，**不要 force push**，先 pull 合并
5. **一个主题只能有一页**。动笔前先看第 6 节的页面清单，撞主题就换题，不要写重复内容（Google 会判定关键词自相残杀，伤 SEO 和 AdSense）

## 5. 写新页面的硬性规范

构建脚本的 Markdown 解析器只支持：**`#`/`##`/`###` 标题、`-` 列表、`1.` 列表、`> ` 引用、`**粗体**`、`` `代码` ``**

支持链接 `[text](url)`（2026-09-22 起，渲染成 <a> 标签）。禁止（会原样显示成乱码）：表格 `|`、图片、`---` 分割线、HTML 标签

新页面 checklist：

- [ ] 在 `pages/` 建 `{slug}.md`，1500–1900 词，全英文
- [ ] 结构模仿 `pages/entry-level-machine-learning-engineer-resume.md`（开场 → Who this page is for → 完整示例 → 分步方法 → Common mistakes → Copy-ready 模板 → FAQ）
- [ ] 必须有 `## FAQ` 章节：一行 `## FAQ` + 4–5 个 `### 问题`，每个问题下一段回答（构建脚本按此格式提取 FAQPage 结构化数据，格式错了 schema 就没了）
- [ ] 在 `build_site.py` 的 `PAGES` 列表加条目：
  ```python
  {
      'slug': 'your-slug',            # 和文件名一致
      'title': '...',                  # 浏览器标题，60 字符内
      'nav': '...',                    # 短名（仅 pillar: True 的页面进顶部导航）
      'keyword': '主关键词',
      'description': '...',            # meta description，155 字符内
      'summary': '...',                # 首页/相关推荐卡片用语，1–2 句
      'template': 'entry-level-ml-engineer-resume-template.docx',  # 决定下载框显示哪个 docx
      'related': ['3-4个已存在的slug'],  # 必须真实存在，否则构建报错
  }
  ```
- [ ] 跑 `python build_site.py && python validate_build.py`，确认新页面有 `Article + FAQPage` schema、`cta=True`
- [ ] 更新 `build_status` 里的篇数/字数统计
- [ ] 承诺类话术禁用：不写"guaranteed interview"之类

## 6. 页面清单（撞题检查用）

| slug | 关键词 |
|---|---|
| entry-level-machine-learning-engineer-resume | entry level machine learning engineer resume（pillar） |
| how-to-write-machine-learning-resume-without-experience | how to write machine learning resume without experience |
| software-engineer-resume-no-experience | software engineer resume no experience |
| entry-level-data-science-resume | entry level data science resume |
| machine-learning-projects-for-resume | machine learning projects for resume beginner |
| machine-learning-resume-summary-examples | machine learning resume summary examples |
| kaggle-projects-for-resume | kaggle projects for resume |
| entry-level-data-analyst-resume | entry level data analyst resume |
| resume-with-no-work-experience | how to write a resume with no work experience |
| ats-friendly-resume-guide | ats friendly resume for tech jobs |
| machine-learning-engineer-cover-letter | machine learning engineer cover letter entry level |
| data-science-internship-resume | data science internship resume |
| python-projects-for-resume | python projects for resume |

合规页（在 `legal/`，不在 PAGES）：about / contact / privacy-policy / terms / disclaimer

### 建议的下一批主题（未被占用）

- `entry-level-software-developer-portfolio` — 作品集怎么配简历
- `data-science-cover-letter-entry-level` — DS 求职信
- `resume-skills-section-tech` — tech 简历技能区怎么写
- `internship-resume-computer-science` — CS 实习简历
- `how-to-list-projects-on-resume` — 项目区通用写法

## 7. 不能动的东西

- `<head>` 里的两个验证 meta：`google-site-verification`、`verify-yeahpromos`（动了 Search Console 和广告联盟验证会失效）
- `AFFILIATE` 链接结构（换链接可以，别删 `rel="sponsored"`）
- canonical / sitemap / robots 生成逻辑
