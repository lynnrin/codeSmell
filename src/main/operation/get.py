import configparser


class get:
    target = ''

    def __init__(self, target):
        self.target = target

    # parameter.iniからData取得
    def get_parameter(self, param):
        config_data = configparser.ConfigParser()
        config_data.read('src/main/parameter.ini')
        target = config_data.get(self.target, param)
        return target
