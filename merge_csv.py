import pandas as pd
import os
import argparse

# 创建解析器对象
parser = argparse.ArgumentParser()

# 添加 -i 参数，用于指定输入目录
parser.add_argument('-i', '--input_dir', type=str, required=True,
                    help='Input directory path')

# 添加 -o 参数，用于指定输出文件
parser.add_argument('-o', '--output_file', type=str, required=True,
                    help='Output file path')

# 解析命令行参数
args = parser.parse_args()

# 通过命令行参数获取文件夹路径和输出文件名
folder_path = args.input_dir
output_file = args.output_file

# 列出所有以"output_"开头的csv文件
files = [f for f in os.listdir(folder_path) if f.startswith("output_") and f.endswith(".csv")]

# 读取所有csv文件并将它们合并到一个数据框中
dfs = []
for file in files:
    path = os.path.join(folder_path, file)
    df = pd.read_csv(path)
    dfs.append(df)
merged_df = pd.concat(dfs, ignore_index=True)

# 将合并后的数据保存到输出文件中
merged_df.to_csv(output_file, index=False)
print(f"Merged {len(dfs)} CSV files into {output_file}.")
