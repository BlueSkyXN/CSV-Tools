import pandas as pd
import configparser
import os
import argparse



def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser()
    # 添加 "-c" 或 "--config" 参数，用于指定配置文件的路径
    parser.add_argument("-c", "--config", help="Specify the path of the configuration file.")
    # 解析命令行参数
    args = parser.parse_args()
    # 如果没有提供配置文件路径，则使用默认路径
    if args.config is None:
        args.config = 'Table_Extractor.conf'  # 请替换为你的默认配置文件路径

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(args.config, encoding='utf-8')

    # 从配置文件中获取所需信息
    input_file = config.get('File', 'input_file', fallback=os.path.join(os.getcwd(), 'input.csv'))
    output_file = config.get('File', 'output_file', fallback=os.path.join(os.getcwd(), 'output.csv'))
    input_encoding = config.get('File', 'input_encoding', fallback='utf-8')
    output_encoding = config.get('File', 'output_encoding', fallback='utf-8')
    column = config.get('Filter', 'column')
    values = [x.strip() for x in config.get('Filter', 'values').split(',')]
    
    # 获取不匹配数据的输出文件信息
    output_file_other = config.get('File', 'output_file_other', fallback=output_file.rsplit('.', 1)[0] + '_other.csv')
    output_encoding_other = config.get('File', 'output_encoding_other', fallback=output_encoding)

    print('开始读取数据...')
    # 读取输入文件
    df = pd.read_csv(input_file, encoding=input_encoding)
    print('数据读取完成.')

    print('开始筛选数据...')
    # 筛选数据
    df_filtered = df[df[column].isin(values)]
    print('数据筛选完成.')

    print('开始写入匹配的数据...')
    # 将筛选后的数据写入输出文件
    df_filtered.to_csv(output_file, index=False, encoding=output_encoding)
    print('匹配的数据写入完成.')

    print('开始写入不匹配的数据...')
    # 将不匹配的数据写入另一个输出文件
    df_filtered_other = df[~df[column].isin(values)]
    df_filtered_other.to_csv(output_file_other, index=False, encoding=output_encoding_other)
    print('不匹配的数据写入完成.')

if __name__ == "__main__":

    main()
