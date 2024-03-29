import glob
import pandas as pd
from src.main.operation import get, file_operation
import os


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

            dir_path = home + get_param.get_parameter('change_csv')

            file_operation.file_operation.make_directory(dir_path)

            df.to_csv(dir_path + file.split('/')[-1], sep='@', index=False)

    def code_smell_flag(self, validation_path, metrics_path):
        df_vali = pd.read_csv(validation_path, sep='@')
        df_met = pd.read_csv(metrics_path, sep='@')

        # 初期化
        df_met['Long_Method_flag'] = 0

        for m_index, (m_path, m_LOC, m_name) in enumerate(zip(df_met['path'], df_met['LOC'], df_met['m_name'])):
            for index, method in df_vali.iterrows():
                if method['path'] in m_path and method['file'] in m_path and\
                        method['method'] in m_name and method['LoC'] == m_LOC:
                    df_met.at[m_index, 'Long_Method_flag'] = 1

        df_met.to_csv(get.get('basic').get_parameter('my_home')
                       + get.get(self.target).get_parameter('save_data_path')
                       + os.path.splitext(validation_path)[0].split('/')[-2] + '/'
                       + os.path.splitext(validation_path)[0].split('/')[-1]
                       + '_flag.csv', sep='@', index=False)
