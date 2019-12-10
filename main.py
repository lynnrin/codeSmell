import sys

from src.main.option import option_selection

if __name__ == '__main__':
    print('main')
    args = sys.argv

    op_selection = option_selection.option_selection(args)
    op_selection.selection()

