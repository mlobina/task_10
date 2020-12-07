import requests

token = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers={'authorization': token},
                                params={'path': 'example.txt', 'overwrite': 'true'})
        url = response.json()['href']

        with open('example.txt', 'rb') as f:
            response = requests.put(url, data={'example.txt': f})

            if response.status_code != 201:
                return "Возможно, возникли проблемы с загрузкой"
            else:
                return "Загрузка успешно выполнена"


if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload('example.txt')
    print(result)
