import glob
import pandas as pd
from src.main.operation import get


class tailor:
    target = ''

    def __init__(self, target):
        self.target = target

    def tailor_validation_data(self):
        home = get.get('basic').get_parameter('my_home')
        get_param = get.get(self.target)
        file_list = glob.glob(home + get_param.get_parameter('save_csv') + '*.csv')

        for file in file_list:
            df = pd.read_csv(file, sep='@')
            df['LOC_per_Mean_LOC'] = df['LOC'] / df['LOC'].mean()
            df['classLOC_per_Mean_ClassLOC'] = df['classLOC'] / df['classLOC'].unique().mean()
            df = df.drop_duplicates()

            df.to_csv(home + get_param.get_parameter('change_csv') + file.split('/')[-1], sep='@', index=False)

    def code_smell_flag(self, validation_path, metrics_path):
        df_vali = pd.read_csv(validation_path, sep='@')
        df_met = pd.read_csv(metrics_path, sep='@')

        num = 0
        print(len(df_vali))
        for index, method in df_vali.iterrows():
            for m_path, m_LOC, m_name in zip(df_met['path'], df_met['LOC'], df_met['m_name']):
                if method['path'] in m_path and method['file'] in m_path and\
                        method['method'] in m_name and method['LoC'] == m_LOC:
                    # ここに1を挿入等の処理
                    num += 1
        print(num)
