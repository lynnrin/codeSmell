import glob
import pandas as pd
from src import get


class tailor:
    target = ''

    def __init__(self, target):
        self.target = target

    def tailor_validation_data(self):
        get_param = get(self.target)
        file_list = glob.glob(get_param.get_parameter('save_csv') + '*.csv')

        for file in file_list:
            df = pd.read_csv(file, sep='@')
            df['LOC_per_Mean_LOC'] = df['LOC'] / df['LOC'].mean()
            df['classLOC_per_Mean_ClassLOC'] = df['classLOC'] / df['classLOC'].unique().mean()
            df = df.drop_duplicates()

            df.to_csv('./ant_data/changeCSV/' + file.split('/')[-1], sep='@', index=False)
