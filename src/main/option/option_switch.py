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
        print("-met [target projects's full path] [save xml full path] : calculate source code metrics")
        print("-px [target xml directory full path] [save csv full path] : parse xml to csv (metrics file)")
        print("-pt [target validation text directory full path] [save csv full path] :"
              " parse txt to csv (validation file)")
        print("-add [target csv full path] [save csv full path] : add columns new metrics (metrics file)")
        print("-cr [target csv directory full path] [target validation directory] :"
              " correspond metrics and validation file")


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
        metrics_dir = pathlib.Path(home + get_parm_ins.get_parameter('change_csv'))
        csv_list = glob.glob(home + get_parm_ins.get_parameter('save_data_path') + '**/*.csv')
        metrics_dir_list = metrics_dir.glob('**/*.csv')
        for file in csv_list:
            if 'flag' in os.path.basename(file):
                continue
            for met_file in metrics_dir_list:
                if not os.path.splitext(os.path.basename(met_file))[0] in file:
                    continue
                tailor.tailor(self.target).tailor_validation_data(file, met_file)

