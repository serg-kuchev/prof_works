from random import randrange
from func_bot import VkBot
from func_vkinder import VkUser
import logging
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import datetime

logging.basicConfig(filename="sample.log", level=logging.INFO)

token = ""

log = logging.getLogger(' (' + str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + ') '))
log.info('')
log.info('\t === Начали работу === \t')
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7)})


def run():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text
                log.info('')
                log.info('\t ==='f'{request} - сообщение пользователя''=== \t')
                bot = VkBot(event.user_id)
                user = VkUser()

                if request == "люди":
                    write_msg(event.user_id, f'{user.list_people()}')
                    log.info('')
                    log.info('\t === Отправили список людей === \t')

                elif request == "фотографии":
                    write_msg(event.user_id, f'{user.photos()}')
                    log.info('')
                    log.info('\t === Отправили фотографии пользователей === \t')
                    # write_msg(event.user_id, f"Хай, {bot.get_user_name_from_vk_id(event.user_id)}")
                elif request == "пока":
                    write_msg(event.user_id, "Пока((")
                else:
                    write_msg(event.user_id, "Не поняла вашего ответа...")
