import pandas as pd
import configparser
import argparse

# 从配置文件中读取参数
def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    file1_path = config.get('File1', 'path')
    file1_encoding = config.get('File1', 'encoding')
    file1_key = config.get('File1', 'key')

    file2_path = config.get('File2', 'path')
    file2_encoding = config.get('File2', 'encoding')
    file2_key = config.get('File2', 'key')

    output_path = config.get('Output', 'path')
    output_encoding = config.get('Output', 'encoding')

    return file1_path, file1_encoding, file1_key, file2_path, file2_encoding, file2_key, output_path, output_encoding

# 使用 argparse 处理命令行参数
parser = argparse.ArgumentParser(description='比较两个 CSV 文件。')
parser.add_argument('-c', '--config', type=str, default='CSV_Data_Compare.conf', help='配置文件的路径。')
args = parser.parse_args()

# 使用命令行参数指定的配置文件，如果没有指定，则使用默认的配置文件
config_file = args.config

file1_path, file1_encoding, file1_key, file2_path, file2_encoding, file2_key, output_path, output_encoding = read_config(config_file)

df1 = pd.read_csv(file1_path, encoding=file1_encoding)
df2 = pd.read_csv(file2_path, encoding=file2_encoding)

df1 = df1.drop_duplicates(subset=file1_key)
df2 = df2.drop_duplicates(subset=file2_key)

df = pd.concat([df1, df2])
df = df.drop_duplicates(subset=file1_key, keep=False)

df.to_csv(output_path, encoding=output_encoding, index=False)
