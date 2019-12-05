from git import *
import subprocess
from src import file_operation, get
import json


# 環境によってlabかmyか変更必須

class calc_metrics:
    tags = []
    target = ''

    def __init__(self, target):
        self.target = target

    def play_jxMetrics(self):
        # parameter.iniから参照
        get_basic_param = get('basic')
        home = get_basic_param.get_Parameter('my_home')

        # tagで検索
        get_target_param = get(self.target)
        target_file_path = get_target_param('path')
        tags = get_target_param('tags')
        tags = json.loads(tags)

        # jar起動
        jar_cmd = ["java", "-jar", home + "jxmetrics/org.jtool.jxmetrics/build/libs/jxmetrics-1.0-all.jar", "-target",
                   home + target_file_path + "/", "-name", "metric"]

        # release毎にcloneして計算
        file_operate = file_operation()
        for i in tags:
            file_operate.remove_directory(home + target_file_path)
            Repo.clone_from('https://github.com/apache/ant',
                            home + target_file_path,
                            branch=i)
            subprocess.run(jar_cmd)
            if file_operate.rename_file(home, i, target_file_path):
                print(i + ' files done')
