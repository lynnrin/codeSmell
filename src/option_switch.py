from abc import *
from abc import ABC


class Abstract_option(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def play(self):
        raise NotImplementedError()

    @abstractmethod
    def print_result(self):
        raise NotImplementedError()


class print_help(Abstract_option, ABC):
    def play(self):
        print("-h : print help")
        print("-met [target projects's full path] [save xml full path] : calculate source code metrics")
        print("-px [target xml directory full path] [save csv full path] : parse xml to csv (metrics file)")
        print("-pt [target validation text directory full path] [save csv full path] :"
              " parse txt to csv (validation file)")
        print("-add [target csv full path] [save csv full path] : add columns new metrics (metrics file)")
        print("-cr [target csv directory full path] [target validation directory] :"
              " correspond metrics and validation file")

    def print_result(self):
        pass


class play_met(Abstract_option, ABC):
    def __init__(self):
        pass

    def play(self):
        pass

    def print_result(self):
        pass


class play_px(Abstract_option, ABC):
    def __init__(self):
        pass

    def play(self):
        pass

    def print_result(self):
        pass


class play_pt(Abstract_option, ABC):
    def __init__(self):
        pass

    def play(self):
        pass

    def print_result(self):
        pass


class play_add(Abstract_option, ABC):
    def __init__(self):
        pass

    def play(self):
        pass

    def print_result(self):
        pass


class play_cr(Abstract_option, ABC):
    def __init__(self):
        pass

    def play(self):
        pass

    def print_result(self):
        pass
