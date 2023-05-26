import pandas as pd
import os
import argparse
from tqdm import tqdm

def split_csv(input_file, output_dir, chunk_size):
    # 读取CSV文件
    df_reader = pd.read_csv(input_file, chunksize=chunk_size)

    # 循环遍历每个块并保存为单独的文件
    file_sizes = []
    file_names = []
    for i, chunk in enumerate(tqdm(df_reader, desc="Splitting")):
        # 确定输出文件路径
        output_path = os.path.join(os.path.expanduser(output_dir), f"output_{i}.csv")
        # 将块保存为CSV文件
        chunk.to_csv(output_path, index=False)
        # 记录生成文件名和大小
        file_names.append(output_path)
        file_sizes.append(os.path.getsize(output_path))

    print("\nGenerated files:")
    for i, fn in enumerate(file_names):
        size_mb = file_sizes[i] / (1024 * 1024)
        print(f"{fn} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split CSV file into smaller chunks')
    parser.add_argument('-i', '--input', type=str, default='~/Desktop/input.csv', help='Path to input CSV file (default: ~/Desktop/input.csv)')
    parser.add_argument('-o', '--output', type=str, default='~/Desktop/output/', help='Path to output directory (default: ~/Desktop/output/)')
    parser.add_argument('-s', '--chunk_size', type=int, default=200000, help='Chunk size (default: 1000000)')

    args = parser.parse_args()

    input_file = os.path.expanduser(args.input)
    output_dir = os.path.expanduser(args.output)
    chunk_size = args.chunk_size

    split_csv(input_file, output_dir, chunk_size)
