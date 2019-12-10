import xml.etree.ElementTree as ET
import glob
import pandas as pd
from src.main.operation import get


class parse:
    target = ''

    def __init__(self, target: str):
        self.target = target

    @staticmethod
    def change_dict_key(d: str, old_key: str, new_key: str, default_value=None):
        d[new_key] = d.pop(old_key, default_value)

    # globで全てのxmlファイルを取得
    def pick_up_all_file(self, path_id, extension):
        getParam = get(self.target)
        try:
            target_directory = getParam.get_parameter(path_id)
            f_n = glob.glob(target_directory + '*.' + extension)
            return f_n

        except:
            print("err")
            return False

        # 実行部分
        # for f in f_n:
        #     self.parse_XML(os.path.splitext(f)[0].split('/')[-1])

    def parse_XML(self, input_file_name):
        getParam = get(self.target)
        xml_path = getParam.get_parameter('path_xml')
        save_csv_path = getParam.get_parameter('path_csv')
        tree = ET.parse(xml_path + input_file_name + '.xml')
        root = tree.getroot()
        # df_parse = pd.DataFrame()
        s_all = []

        # rootから順に情報取得
        for node in root:
            c_name = {}
            # m_name = {}
            for package_name in node:
                # s_v = {}
                m1 = {}
                # m2 = {}

                if package_name.tag == 'class':
                    c_name = {'path': package_name.get('path')}
                for class_name in package_name:
                    if class_name.tag == 'metrics':
                        m1 = class_name.attrib
                        keys = m1.keys()
                        for k in keys:
                            if 'class' not in k:
                                self.change_dict_key(m1, k, 'class' + k)

                    if class_name.tag == 'method':
                        m_name = {'m_name': class_name.get('name')}
                        for method in class_name:
                            s_v = {}
                            if method.tag == 'metrics':
                                m2 = method.attrib
                                s_v.update(c_name)
                                s_v.update(m_name)
                                s_v.update(m1)
                                s_v.update(m2)
                                s_all.append(s_v)

        df_parse = pd.io.json.json_normalize(s_all)

        # 邪魔なデータを削除し，csv出力
        df_parse = df_parse.drop_duplicates()
        df_parse = df_parse.dropna(how='any', axis=1)
        df_parse.to_csv(save_csv_path + input_file_name + '.csv', index=False, sep='@')
        del df_parse

    def parse_txt(self, input_file_name):
        # datasetの読み込み
        get_param = get(self.target)
        dataset_path = get_param.get_parameter('dataset')
        df_validate = pd.read_table(dataset_path + input_file_name + '.txt', sep=':', header=None)

        # ':'で分割出来ない部分を無理やり分割　FIX-ME
        df_validate_split = pd.concat([df_validate, df_validate[2].str.split(' ', expand=True)], axis=1)
        df_validate_split.columns = ['method', 'file', 'delete', 'delete', 'path', 'LoC']
        df_validate_split2 = df_validate_split.drop('delete', axis=1)

        # csvで保存 parameterいじってから
        # df_validate_split2.to_csv()

