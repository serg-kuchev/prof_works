import requests
import unittest


def put_file(token):
    HEADERS = {'Authorization': 'OAuth'+' '+str(token)}
    resp1 = requests.put(
        'https://cloud-api.yandex.net/v1/disk/resources',
        params={'path': '/test'},
        headers=HEADERS
    )
    resp1.raise_for_status()
    print(resp1.status_code)

token = ''

class YaTest(unittest.TestCase):

    def test_disk_put(self):
        self.assertEqual(201, put_file(token))
        print('Папка создана')

    def test_disk_errors(self):
        self.assertEqual(409, put_file(token))
        print('Такая папка уже есть')


if __name__ == '__main__':
    unittest.main()
