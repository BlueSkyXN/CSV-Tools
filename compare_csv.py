import pandas as pd
import argparse

# 创建解析器
parser = argparse.ArgumentParser()

# 添加参数
parser.add_argument('-a', default='A.csv', help='Path to the first input CSV file')
parser.add_argument('-b', default='B.csv', help='Path to the second input CSV file')
parser.add_argument('-c', default='Output.csv', help='Path to the output CSV file')
parser.add_argument('-d', default='name', help='Column to be matched')

# 解析参数
args = parser.parse_args()

# 读取 CSV 文件
df_A = pd.read_csv(args.a)
df_B = pd.read_csv(args.b)

# 执行匹配
df = df_A.merge(df_B, how='outer', left_on=args.d, right_on=args.d, indicator=True)

# 提取不匹配的行
output = df[df['_merge'] != 'both']

# 写入新的 CSV 文件
output.to_csv(args.c, index=False)
