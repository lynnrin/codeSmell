import sys

from src.main.option import option_selection

if __name__ == '__main__':
    args = sys.argv

    option_list = ['-cr']

    for i in option_list:
        args[1] = i
        print(args)
        op_selection = option_selection.option_selection(args)
        op_selection.selection()

