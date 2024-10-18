import pyperclip

def print_file_contents(filename):
    code = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '\\n').replace('\t', '\\t')
            code += line
    return code

code = print_file_contents('test2.py')
pyperclip.copy(code)