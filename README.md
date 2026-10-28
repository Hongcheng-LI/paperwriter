# journal-adaptive-manuscript

用于科研论文写作、期刊风格学习、转刊与投稿包检查的 Codex skill。

从目标期刊的真实文章学习论证结构，再依据作者的研究证据组织稿件。参考文章用于学习写作，实验事实来自作者的项目材料；二者分开记录。

## 适用任务

- 初始化论文工作目录，整理期刊材料、研究证据与写作计划。
- 从目标期刊范文学习段落任务、信息顺序和证据组织。
- 构建论文主线、起草和修改英文稿件，并单独提供中文编辑说明。
- 基于作者最新 Word 稿进行转刊，保留其内容、公式和格式。
- 核对主稿、Supporting Information、图表、Cover Letter 等文件的一致性。
- 根据编辑的技术退回意见检查文章类型、实际字数与独立图表附件。

不用于替代原始实验核验，也不承诺投稿接收、科学正确性或查重结果。单句润色通常无需启用完整工作流。

## 安装

将本仓库目录放入 Codex 的 skills 目录，并命名为 `journal-adaptive-manuscript`。例如，在 Windows PowerShell 中首次安装：

```powershell
git clone https://github.com/Hongcheng-LI/journal-adaptive-manuscript.git "$env:USERPROFILE\.codex\skills\journal-adaptive-manuscript"
```

如果配置了 `CODEX_HOME`，使用该目录下的 `skills`。已有同名安装时，先保留本地定制内容，再同步更新，不直接覆盖。

## 使用示例

在论文项目目录中向 Codex 提出任务：

```text
使用 $journal-adaptive-manuscript，为这个论文项目初始化工作目录。
```

```text
使用 $journal-adaptive-manuscript，先学习我提供的目标期刊文章，
再结合我的研究结果提出论文主线和章节安排。
```

```text
使用 $journal-adaptive-manuscript，依据指定文件夹中的最新投稿文件，
处理编辑提出的字数统计和图表独立上传要求。
```

用户的任务范围、已确认决定和授权持续有效。Skill 不代表上传研究材料或实际提交稿件的授权。

## 工作原则

原始数据只读；优先保留作者最新版本；重要结论可追溯。区分期刊要求、范文习惯、研究事实与编辑判断。对未知参数保留核对事项，不从范文补造方法。

转刊时分别检查数据、正文信息和字符格式。技术重投时先统计实际字数，再判断是否需要删减，按适用要求拆分图表并校准主稿与 SI 引用。这里没有固定某个期刊的字数上限或通用的图表上传方式。

## 文件结构

- `SKILL.md`：入口、适用边界和工作流。
- `references/`：写作、证据、方法、Word 保真、投稿包及技术重投指引。
- `scripts/project_tools.py`：项目初始化、材料清单与占位符检查工具。
- `scripts/test_project_tools.py`：隔离临时目录中的功能测试。
- `assets/`：通用目录结构和证据记录模板。

本仓库不包含作者论文、实验记录、谱图、文献全文或访问凭据。

## 验证

在仓库根目录运行：

```text
python -m unittest discover -s scripts -p "test_*.py" -v
```

脚本测试检验初始化、文件保留、路径边界、材料清单及占位符检查等行为，不等于独立验证论文写作质量。
