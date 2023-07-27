import pandas as pd
import configparser
import os

def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('Table_Extractor.conf')

    # 从配置文件中获取所需信息
    input_file = config.get('File', 'input_file', fallback=os.path.join(os.getcwd(), 'input.csv'))
    output_file = config.get('File', 'output_file', fallback=os.path.join(os.getcwd(), 'output.csv'))
    input_encoding = config.get('File', 'input_encoding', fallback='utf-8')
    output_encoding = config.get('File', 'output_encoding', fallback='utf-8')
    column = config.get('Filter', 'column')
    values = [x.strip() for x in config.get('Filter', 'values').split(',')]

    # 读取输入文件
    df = pd.read_csv(input_file, encoding=input_encoding)

    # 筛选数据
    df_filtered = df[df[column].isin(values)]

    # 将筛选后的数据写入输出文件
    df_filtered.to_csv(output_file, index=False, encoding=output_encoding)

if __name__ == "__main__":
    main()
