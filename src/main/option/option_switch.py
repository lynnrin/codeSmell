from abc import *
from abc import ABC
from src.main.data_operation import *
from src.main.operation import get
import os, glob, pathlib


class Abstract_option(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def play(self):
        raise NotImplementedError()


class print_help(Abstract_option, ABC):
    def play(self):
        print("-h : print help")
        print("-met [target name] : calculate source code metrics")
        print("-px [target name] : parse xml to csv (metrics file)")
        print("-pt [target name] : parse txt to csv (validation file)")
        print("-add [target name] : add columns new metrics (metrics file)")
        print("-cr [target name] : correspond metrics and validation file")


class play_met(Abstract_option, ABC):
    target = ''

    def __init__(self, target):
        self.target = target

    def play(self):
        cm_obj = calc_metrics.calc_metrics(self.target)
        cm_obj.play_jxMetrics()


class play_px(Abstract_option, ABC):
    target = ''

    def __init__(self, target):
        self.target = target

    def play(self):
        parse_x = parse.parse(self.target)
        param_operate = get.get(self.target)
        # home切り替え
        xml_path = get.get('basic').get_parameter('my_home') + param_operate.get_parameter('path_xml')
        all_file = parse_x.pick_up_all_file(xml_path, 'xml')
        for file_name in all_file:
            parse_x.parse_XML(os.path.splitext(file_name)[0].split('/')[-1])


class play_pt(Abstract_option, ABC):
    target = ''

    def __init__(self, target):
        self.target = target

    def play(self):
        parse_txt = parse.parse(self.target)
        param_operate = get.get(self.target)
        dataset_dir = get.get('basic').get_parameter('my_home') + param_operate.get_parameter('dataset')

        # directory名のみ取得
        directories = os.listdir(dataset_dir)
        directories = [f for f in directories if os.path.isdir(os.path.join(dataset_dir, f))]

        # 対象のSmell
        target_smell = get.get('basic').get_parameter('smell_list')
        target_smell = [x.strip() for x in target_smell.strip("[]").split(',')]

        # file名取得
        for dir in directories:
            all_files = parse_txt.pick_up_all_file(os.path.join(dataset_dir, dir) + '/', 'txt')
            for file in all_files:
                for smell_name in target_smell:
                    if smell_name in os.path.basename(file):
                        parse_txt.parse_txt(file)


class play_add(Abstract_option, ABC):
    target = ''

    def __init__(self, target):
        self.target = target

    def play(self):
        tailor.tailor(self.target).tailor_validation_data()


class play_cr(Abstract_option, ABC):
    target = ''

    def __init__(self, target):
        self.target = target

    def play(self):
        home = get.get('basic').get_parameter('my_home')
        get_parm_ins = get.get(self.target)
        csv_list = glob.glob(home + get_parm_ins.get_parameter('save_data_path') + '**/*.csv')
        metrics_dir_list = glob.glob(home + get_parm_ins.get_parameter('change_csv') + '*.csv')

        for file in csv_list:
            # print(file)
            if 'flag' in os.path.basename(file):
                continue
            for met_file in metrics_dir_list:
                # print("{}    {}\n".format(met_file, file))
                if os.path.splitext(os.path.basename(met_file))[0] in file:
                    print("{}    {}\n".format(met_file, file))
                    tailor.tailor(self.target).code_smell_flag(file, met_file)

