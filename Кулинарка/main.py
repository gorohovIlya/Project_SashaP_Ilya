import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import sqlite3
from whattocookfrom import whattocookfrom
from howtoprepare import howtoprepare
from randommeal import randommeal
from help import help
# from pprint import pprint


TOKEN = '1960805a354085e3eff3b7604706f98fb505669be7f68e3564080a4b19c5efb032c8de2530676593c891f'


def send_mes(vk, chat, text):
    random_id = random.randint(0, 2 ** 64)
    vk.method('messages.send', {'chat_id': chat, 'message': text, 'random_id': random_id})


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    # longpoll = VkBotLongPoll(vk_session, 210739018, wait=1)
    longpoll = VkLongPoll(vk_session)
    print('работаем')
    for event in longpoll.listen():
        print(event.type)
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if event.from_chat:
                    print(event.type)
                    print('Новое сообщение:')
                    print('Для меня от:', event.chat_id)
                    print('Текст:', event.text)
                    # send_mes(vk_session, event.chat_id, event.text)
                    if event.text[0:14] == "какприготовить":
                        send_mes(vk_session, event.chat_id, howtoprepare(event.text[14:]))
                    elif event.text == "чтоприготовитьиз":
                        send_mes(vk_session, event.chat_id, whattocookfrom(event.text))
                    elif event.text == "случайноеблюдо":
                        send_mes(vk_session, event.chat_id, randommeal())
                    elif event.text == "помощь":
                        send_mes(vk_session, event.chat_id, help())
        if event.type == VkEventType.CHAT_UPDATE:
            text = '''Приветствую вас! Я Бот Кулинарная книга.
Я смогу (когда-нибудь) написать определённый рецепт блюда, 
написать список блюд, у которых есть рецепт в книге,
добавлять в список новые блюда и прочие действия.'''
            send_mes(vk_session, event.chat_id, text)
            # vk = vk_session.get_api()
            # vk.messages.send(user_id=event.obj.message['from_id'],
            #                  message="Спасибо, что написали нам. Мы обязательно ответим",
            #                  random_id=random.randint(0, 2 ** 64))
            # pprint(vars(event))


if __name__ == '__main__':
    main()
