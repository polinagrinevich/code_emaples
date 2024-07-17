import argparse
import ast


def process(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            if len(line) == 0:
                continue

            path_1, path_2 = line.split()

            with open(path_1, 'r') as file_1:
                text_1 = ast.unparse(ast.parse(file_1.read()))

            with open(path_2, 'r') as file_2:
                text_2 = ast.unparse(ast.parse(file_2.read()))

            n = len(text_1)
            m = len(text_2)

        current_row = list(range(n + 1))
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [0] * (n + 1)
            for j in range(1, n + 1):
                add = previous_row[j] + 1
                delete = current_row[j - 1] + 1
                change = previous_row[j - 1]
                if text_1[j - 1] != text_2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        f_out.write(f'{1 - current_row[n] / max(n, m)}\n')


parser = argparse.ArgumentParser(
    prog='Custom Antiplagiat Tool',
    description='Finds the percentage of similarities between 2 files with Levenstein distance',
)
parser.add_argument('input', help='path to input file')
parser.add_argument('output', help='path to output file')

args = parser.parse_args()
input_file, output_file = args.input, args.output

process(input_file, output_file)
