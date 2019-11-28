import requests


class send_line:
    def __init__(self):
        pass

    @staticmethod
    def send_line(message):
        line_token = 'nU7wXOhxtTSvpZI0HENbOJEIPAGXh4rp1oJufBt98GQ'
        endpoint = 'https://notify-api.line.me/api/notify'
        message = "\n{}".format(message)
        payload = {'message': message}
        header = {'Authorization': 'Bearer {}'.format(line_token)}
        requests.post(endpoint, data=payload, headers=header)
