def print_file_contents(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.replace('\n', '\\n').replace('\t', '\\t')
            print(line, end='')

print_file_contents('main.py')
