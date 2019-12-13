import os
import glob
import shutil
import subprocess
from src.main.operation import get


class file_operation:
    home = ''
    target = ''

    def __init__(self, home: str, target: str):
        self.home = home
        self.target = target

    # Metrics計算時，cloneしたものを削除目的
    @staticmethod
    def remove_directory(path: str):
        if not os.path.exists(path):
            return
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        else:
            shutil.rmtree(path)

    # Metricsファイルを移動(mvコマンド)する目的
    def rename_file(self, target_tag: str, target_file_path: str) -> bool:
        try:
            target_param_instanse = get.get(self.target)
            save_xml_path = target_param_instanse.get_parameter('path_xml')
            file_name_before = target_param_instanse.get_parameter('before')
            f_n = glob.glob(self.home + target_file_path + "/metric*")
            file_name = self.home + save_xml_path + \
                        self.replace_file_name(target_tag, file_name_before, self.target) + ".xml"
            rename = "mv " + f_n[0] + " " + file_name
            print(rename)
            subprocess.run(rename, shell=True)
            return True
        except:
            return False

    # Metricsファイルを判別しやすくする目的(e.g. rel/...をapache_....に変更)
    @staticmethod
    def replace_file_name(original: str, before: str, after: str) -> str:
        return original.replace(before, after)

    @staticmethod
    def make_directory(directory_name: str) -> bool:
        if not os.path.isdir(directory_name):
            os.makedirs(directory_name, exist_ok=True)
