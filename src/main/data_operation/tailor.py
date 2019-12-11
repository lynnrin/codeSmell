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
