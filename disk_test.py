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
    data = resp1.json()
    a = data['href']
    return a


class test_some_disk(unittest.TestCase):

    def test_disk_put(self):
        self.assertEqual('https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Ftest',
                         put_file(''))


if __name__ == '__main__':
    unittest.main()
