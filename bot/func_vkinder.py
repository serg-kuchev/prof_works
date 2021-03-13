import requests
import vk_api
from pprint import pprint
from init_constant import *
from datetime import datetime
from urllib.parse import urlencode
import json


vktoken = ""
vk = vk_api.VkApi(token=vktoken)
token = ""


class VkUser:
    def __init__(self):
        current_year = datetime.now().year
        info = vk.method('account.getProfileInfo')
        self.sex = 1 if info['sex'] == 2 else 2
        self.hometown = info['city']['title']
        self.status = info['relation']
        self.day, self.month, self.year = info['bdate'].split('.')
        self.age = current_year - int(self.year)
        self.age_from = self.age - 3
        self.age_to = self.age + 3

    def get_user_access(self):
        client_id = 7786539
        url = 'https://oauth.vk.com/authorize'
        params = {
            'client_id': client_id,
            'response_type': 'token',
            'display': 'page',
            'scope': ['groups', 'friends', 'photos'],
            'v': '5.103',
        }
        print('?'.join((url, urlencode(params))))
        self.token = input('Enter the token from the redirect link: ')

    def search_people(self):
        search = vk.method('users.search', {'sex': self.sex, 'sort': 0, 'v': 5.89, 'count': 2,
                                            'hometown': self.hometown, 'status': self.status,
                                            'has_photo': 1, 'age_to': self.age_to,
                                            'age_from': self.age_from, 'offset': 0
                                            })
        return search

    def list_people(self):
        people_list = list()
        new_people_list = list()

        for item in self.search_people()['items']:
            people_list.append(item)

        for i in range(len(people_list)):
            id = people_list[i]['id']
            url = "https://vk.com/id" + str(id)
            name = str(people_list[i]['first_name']) + ' ' + str(people_list[i]['last_name'])
            new_people_list.append({'name': name, 'url': url})
        pprint(new_people_list)
        return new_people_list

    def photos(self):
        photo_dict = list()

        for i in self.search_people()['items']:
            photos = vk.method('photos.get', {'v': 5.89,
                                              'access_token': token,
                                              'owner_id': i['id'],
                                              'album_id': 'profile',
                                              'extended': 1,
                                              'count': 3,
                                              })

            if len(photos['items']) > 1:
                for a in range(len(photos['items'])):
                    url = photos['items'][a]['sizes'][len(photos['items'][a]['sizes'])-1]['url']
                    likes = photos['items'][a]['likes']['count']
                    photo_dict.append({'url': url, 'likes': likes})
            elif len(photos['items']) == 1:
                url = photos['items'][0]['sizes'][len(photos['items'][0]['sizes']) - 1]['url']
                likes = photos['items'][0]['likes']['count']
                photo_dict.append({'url': url, 'likes': likes})
        my_dict = sorted(photo_dict, key=lambda x: x['likes'], reverse=True)

        if len(photo_dict) > 3:
            photo_dict = my_dict[:3]
        else:
            photo_dict = my_dict

        pprint(photo_dict)
        return photo_dict

    def json_write(self):
        data = self.photos() + self.list_people()
        with open('info.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=1)


b = VkUser().photos()
# print(b)
#
a = VkUser().list_people()
# pprint(b)
