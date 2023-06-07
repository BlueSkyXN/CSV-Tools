import csv
import sys
import argparse

def convert_utf8_to_ansi(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_content:
        content = input_content.read()

    # 将内容从UTF-8转换为ANSI编码
    ansi_content = content.encode('ansi', 'ignore').decode('ansi')

    with open(output_file, 'w', encoding='ansi') as output_content:
        output_content.write(ansi_content)

def main():
    parser = argparse.ArgumentParser(description='Convert UTF-8 encoded file to ANSI encoded file')
    parser.add_argument('-i', '--input', type=str, help='input file path')
    parser.add_argument('-o', '--output', type=str, help='output file path')

    args = parser.parse_args()

    if not args.input or not args.output:
        parser.print_help(sys.stderr)
        sys.exit(1)

    input_file = args.input
    output_file = args.output

    convert_utf8_to_ansi(input_file, output_file)

if __name__ == '__main__':
    main()
