# 学习时间账本 · 第 1 天
# 运行：python start.py
import pandas as pd

# ---------- 1. 先把数据读进来，看清它长什么样 ----------
df = pd.read_csv("data/study_log.csv")
print("行数、列数：", df.shape)
print(df.head())

# 先认识数据：有哪些科目、哪些类型
print("\n科目列表：", df["科目"].unique())
print("\n类型分布：\n", df["类型"].value_counts())

# ---------- Q1：每个科目各花了多少分钟？排出前 5 ----------
# 提示：df.groupby("科目")["分钟"].sum() 之后再 .sort_values(ascending=False).head()
# TODO 在这里写你的代码
subject_total=df.groupby("科目")["分钟"].sum().sort_values(ascending=False).head(5)
print(subject_total)

# ---------- Q2：每天总学习时长？哪天低于 120 分钟？ ----------
# 提示：先剔掉"其他"类型 -> df[df["类型"] != "其他"]
#       再 groupby("日期")["分钟"].sum()
#       最后用布尔筛选找出 < 120 的日子
# TODO 在这里写你的代码
df_study=df[df["类型"]!="其他"]
daily_total=df_study.groupby("日期")["分钟"].sum()
print('\n每日总学习时长（已剔除「其他」）：\n', daily_total)
less_120_day=daily_total[daily_total<120]
print("\n低于 120 分钟的日子：\n", less_120_day)

# ---------- 今天的新记录（每天加一行，格式照抄）----------
# 2026-10-30,晚上,高数,输出,70,3,第二章课后题第一组
