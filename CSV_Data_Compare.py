
import pandas as pd
import configparser
import argparse

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    input_file_1_path = config.get('Input_File_1', 'path', fallback='input1.csv')
    input_file_1_encoding = config.get('Input_File_1', 'encoding', fallback='UTF-8')
    key_1 = config.get('Input_File_1', 'key')

    input_file_2_path = config.get('Input_File_2', 'path', fallback='input2.csv')
    input_file_2_encoding = config.get('Input_File_2', 'encoding', fallback='UTF-8')
    key_2 = config.get('Input_File_2', 'key')

    output_file_1_path = config.get('Output_File_1', 'path', fallback='output1.csv')
    output_file_1_encoding = config.get('Output_File_1', 'encoding', fallback='UTF-8')

    output_file_2_path = config.get('Output_File_2', 'path', fallback='output2.csv')
    output_file_2_encoding = config.get('Output_File_2', 'encoding', fallback='UTF-8')

    return input_file_1_path, input_file_1_encoding, key_1, input_file_2_path, input_file_2_encoding, key_2, output_file_1_path, output_file_1_encoding, output_file_2_path, output_file_2_encoding

parser = argparse.ArgumentParser(description='比较两个 CSV 文件的差异。')
parser.add_argument('-c', '--config', type=str, default='CSV_Data_Compare.conf', help='配置文件的路径。')
args = parser.parse_args()

config_file = args.config

input_file_1_path, input_file_1_encoding, key_1, input_file_2_path, input_file_2_encoding, key_2, output_file_1_path, output_file_1_encoding, output_file_2_path, output_file_2_encoding = read_config(config_file)

df1 = pd.read_csv(input_file_1_path, encoding=input_file_1_encoding)
df2 = pd.read_csv(input_file_2_path, encoding=input_file_2_encoding)

# For "未解决的记录", find the common keys in both files, and get the corresponding rows from File2
common_keys = pd.merge(df1, df2, on=key_1)[key_1]
unresolved_df = df2[df2[key_2].isin(common_keys)]
unresolved_df.to_csv(output_file_1_path, encoding=output_file_1_encoding, index=False)

# For "新增的记录", find the keys that are in File2 but not in File1, and get the corresponding rows from File2
new_keys = set(df2[key_2]) - set(df1[key_1])
new_df = df2[df2[key_2].isin(new_keys)]
new_df.to_csv(output_file_2_path, encoding=output_file_2_encoding, index=False)
