import pandas as pd
import configparser
import os

def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('Table_Extractor.conf', encoding='utf-8')

    # 从配置文件中获取所需信息
    input_file = config.get('File', 'input_file', fallback=os.path.join(os.getcwd(), 'input.csv'))
    output_file = config.get('File', 'output_file', fallback=os.path.join(os.getcwd(), 'output.csv'))
    input_encoding = config.get('File', 'input_encoding', fallback='utf-8')
    output_encoding = config.get('File', 'output_encoding', fallback='utf-8')
    column = config.get('Filter', 'column')
    values = [x.strip() for x in config.get('Filter', 'values').split(',')]

    print('开始读取数据...')
    # 读取输入文件
    df = pd.read_csv(input_file, encoding=input_encoding)
    print('数据读取完成.')

    print('开始筛选数据...')
    # 筛选数据
    df_filtered = df[df[column].isin(values)]
    print('数据筛选完成.')

    print('开始写入数据...')
    # 将筛选后的数据写入输出文件
    df_filtered.to_csv(output_file, index=False, encoding=output_encoding)
    print('数据写入完成.')

if __name__ == "__main__":
    main()
