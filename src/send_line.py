import requests


class send_line:
    def __init__(self):
        pass

    @staticmethod
    def send_line(message: str):
        line_token = ''
        endpoint = 'https://notify-api.line.me/api/notify'
        message = "\n{}".format(message)
        payload = {'message': message}
        header = {'Authorization': 'Bearer {}'.format(line_token)}
        requests.post(endpoint, data=payload, headers=header)
