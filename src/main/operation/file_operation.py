import os
import glob
import shutil
import subprocess


class file_operation:
    home = ''

    def __init__(self, home: str):
        self.home = home

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
    def rename_file(self, target: str, target_file: str) -> bool:
        try:
            f_n = glob.glob(self.home + target_file + "/metric*")
            file_name = self.home + target_file + "_data/xml/" + self.replace_file_name(target) + ".xml"
            rename = "mv " + f_n[0] + " " + file_name
            subprocess.run(rename, shell=True)
            return True
        except:
            return False

    # Metricsファイルを判別しやすくする目的(e.g. rel/...をapache_....に変更)
    @staticmethod
    def replace_file_name(original: str, before: str, after: str) -> str:
        return original.replace(before, after)

