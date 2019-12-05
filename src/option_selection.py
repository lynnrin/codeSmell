from src.option_switch import *


class option_selection:
    args = []

    def __init__(self, args):
        self.args = args

    def selection(self):
        if len(self.args) <= 2 or self.args[1] == '-h':
            print_help().play()

        elif len(self.args) == 3:
            if self.args[1] == '-met':
                pm_obj = play_met(self.args[2])
                pm_obj.play()

            elif self.args[1] == '-px':
                pass

            elif self.args[1] == '-pt':
                pass

            elif self.args[1] == '-add':
                pass

            elif self.args[1] == '-cr':
                pass
