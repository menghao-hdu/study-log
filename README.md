# 项目 1 · 学习时间账本（Study Log Analyzer）

> 目标：用 pandas 把"我每天到底把时间花在哪了"算清楚，输出一张图 + 三条结论。
> 难度：pandas 入门级（只要会 `read_csv` / `groupby` / `sort_values`）。
> 为什么选它：① 数据你自己就能产，不用等别人给；② 直接喂给你的复盘系统；③ 是统计专业最对口的第一份作品集素材。

---

## 0. 数据说明

`data/study_log.csv` 是给你练手的样例（2026-10-19 至 10-30，约 60 行），字段：

| 字段 | 含义 | 取值 |
| --- | --- | --- |
| 日期 | 哪一天 | `2026-10-30` |
| 时段 | 上午 / 下午 / 晚上 | 3 类 |
| 科目 | 高数 / 线代 / 英语 / Python / 其他课程 / 运动 / 复盘 | 文本 |
| 类型 | **输入**（听课看书）/ **输出**（做题写代码）/ **其他** | 3 类 |
| 分钟 | 这段实际投入多少分钟 | 整数 |
| 完成度 | 自评 1–5（1=几乎没推进，3=按计划，5=超额） | 1–5 |
| 备注 | 一句话，允许空 | 文本 |

今晚开始，把这张表换成**你自己**的记录：每天睡前 3 分钟补当天几行（原本 10-19~10-29 的行删掉）。

## 1. 四次课路线（每次 60–75 分钟）

| 次 | 内容 | 学到的 pandas 能力 | 交付 |
| --- | --- | --- | --- |
| 第 1 次（今晚） | Q1 + Q2 | `read_csv`、`shape`、`unique`、`value_counts`、`groupby().sum()`、布尔筛选 | 终端能打印出"科目排行"和"每日时长" |
| 第 2 次 | Q3 + Q4 | `pivot_table`、`mean`、`agg`、`round` | "哪个时段效率最高"+"输出占比"两个数 |
| 第 3 次 | Q5 + 保存 | `sort_values`、`nsmallest`、`to_csv`、`.dt.dayofweek` | 生成 `output/汇总.csv` |
| 第 4 次 | 画图 + 写结论 | `matplotlib` 柱状图、`中文乱码` 处理、README 结论段 | 一张图 + 三条结论，能发给别人看 |

## 2. 今晚（第 1 次，75 分钟）只做两件事

**准备（10 min）**：确认 Python 环境里有 pandas。

```bash
pip install pandas matplotlib
```

**跑起来（15 min）**：在 `python项目/学习时间账本/` 目录下打开终端，运行

```bash
python start.py
```

看到"行数、列数 (58, 7)"和一张表头出来，说明环境通了。

> 如果终端里中文是乱码（`����`），那是 Windows 终端编码问题，不是代码错：在 VS Code 里打开 `start.py` 用它的终端跑，或者先执行 `chcp 65001`。

**写 Q1（25 min）**：每个科目各花了多少分钟？从多到少排，打印前 5。
提示：`df.groupby("科目")["分钟"].sum().sort_values(ascending=False).head()`

**写 Q2（25 min）**：每天总学习时长是多少？有哪几天低于 120 分钟？
提示：先剔掉"其他"类型 → `df[df["类型"] != "其他"]`，再 `groupby("日期")["分钟"].sum()`，最后用布尔筛选。

> 卡住超过 10 分钟就看报错信息本身——`KeyError` 基本是列名写错（注意是全角还是半角），`AttributeError` 多数是括号没配对。**先自己读报错，再问 AI，把 AI 的回答和自己的猜想对一遍。**

## 2.5 如果你用 PyCharm（推荐，比命令行省事）

1. 打开 PyCharm（`D:\appdownload\PyCharm 2026.2.3\bin\pycharm64.exe`，或开始菜单搜 PyCharm）。
2. **File → Open**，选 `D:\workbuddy\个人发展\python项目\学习时间账本` 这一层。
   ⚠️ 不要直接打开 `个人发展` 整个文件夹，否则 `data/study_log.csv` 这个相对路径会读不到。
3. 右下角看解释器。要选：`C:\Users\Lenovo\AppData\Local\Programs\Python\Python314\python.exe`
   （这个环境里 pandas 3.0.6、matplotlib 3.11.2 已经装好了，**不用再 pip install**）。
   如果 PyCharm 弹窗让你"新建虚拟环境"，选 **Existing interpreter**，别建新的——建了就得重装一遍 pandas。
4. 打开 `start.py`，右键 → **Run 'start'**（或点行号旁的绿色三角）。看到 `(58, 7)` 就通了。
5. 断点调试：点行号左侧打红点 → **Shift+F9**，Variables 面板里能展开 `df` 直接看数据。
   学 pandas 时这比 `print` 直观十倍，**这是 PyCharm 相对命令行最大的优势，要用起来**。
6. 中文乱码（一般不会）：Settings → Editor → File Encodings 全部设 UTF-8；Run 配置的
   Environment variables 里加一条 `PYTHONIOENCODING=utf-8`。

**三个常见报错**

| 报错 | 原因 | 解法 |
| --- | --- | --- |
| `No module named 'pandas'` | 解释器选到了新建的 venv | 换回上面那个 Python314 |
| `FileNotFoundError: data/study_log.csv` | 打开的项目层级不对 | 重新 Open `学习时间账本` 这一层 |
| 运行按钮是灰的 | 还在 Indexing | 等右下角进度条走完 |

## 3. 后面 3 次的问题（先别看答案）

- **Q3**：上午 / 下午 / 晚上，哪个时段的平均完成度最高？哪个时段投入分钟最多但完成度最低？（`pivot_table`）
- **Q4**：**输出**（做题/写代码）占总学习时间的百分之多少？（这一个是全项目最值钱的数字）
- **Q5**：完成度最低的 5 条记录分别在干什么？读一遍备注，找共性。

## 4. 验收标准（做完打勾）

- [ ] `start.py` 能跑通，无报错
- [ ] Q1 有输出：科目时长排行榜
- [ ] Q2 有输出：每日时长 + 低于 120 分钟的日子清单
- [ ] 今天的记录已经写进 `study_log.csv`
- [ ] 把 `start.py` 和 `data/study_log.csv` 传到一个 GitHub 仓库（仓库名 `study-log`）

## 5. 做完之后的升级方向（不用现在做）

1. 换成真实数据：校园卡流水、问卷星导出（`pd.read_excel`）、四六级成绩。
2. 加"目标线"：每周高数 ≥ 420 分钟，低于就标红。
3. 变成作品集文章：《我用 60 行 Python 量化了自己的学习时间》，配图发到知乎/GitHub Pages。
