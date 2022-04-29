import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
# from whattocookfrom import whattocookfrom, whattocookfrom_command
# from howtoprepare import howtoprepare, howtoprepare_command
# from randommeal import randommeal, randommeal_command
from help import help
from data import db_session, __all_models
from command_structure import AddMeal

# ALL_KEYS = [howtoprepare_command.get_keys(), whattocookfrom_command.get_keys(), randommeal_command.get_keys()]


def send_mes(vk, chat, text):
    random_id = random.randint(0, 2 ** 64)
    vk.method('messages.send', {'chat_id': chat, 'message': text, 'random_id': random_id})


class CookingBot:
    def __init__(self, token):
        self.token = token
        # self.commands = commands
        self.init()

    def init(self):
        db_session.global_init("db/test_cooking.db")
        vk_session = vk_api.VkApi(
            token=self.token)
        add_m = AddMeal(self, 'add_meal', 'добавление блюда в базу данных')
        longpoll = VkLongPoll(vk_session)
        print('работаем')
        self.work_bot(longpoll, vk_session, add_m)
        # for event in longpoll.listen():
        #     print(event.type)
        #     if event.type == VkEventType.MESSAGE_NEW:
        #         if event.to_me:
        #             if event.from_chat:
        #                 print(event.type)
        #                 print('Новое сообщение:')
        #                 print('Для меня от:', event.chat_id)
        #                 print('Текст:', event.text)
                        # for i in ALL_KEYS:
                        #     for j in i:
                        #         if j in event.text and j in ALL_KEYS[0]:
                        #             send_mes(vk_session, event.chat_id, howtoprepare(event.text[len(j):]))
                        #         elif j in event.text and j in ALL_KEYS[1]:
                        #             send_mes(vk_session, event.chat_id, whattocookfrom(event.text[len(j):]))
                        #         elif j in event.text and event.text in ALL_KEYS[2]:
                        #             send_mes(vk_session, event.chat_id, randommeal())
                        #         elif "помощь" in event.text:
                        #             send_mes(vk_session, event.chat_id, help())
    #         if event.type == VkEventType.CHAT_UPDATE:
    #             text = '''Приветствую вас! Я Бот Кулинарная книга.
    # Я смогу (когда-нибудь) написать определённый рецепт блюда,
    # написать список блюд, у которых есть рецепт в книге,
    # добавлять в список новые блюда и прочие действия.'''
    #             send_mes(vk_session, event.chat_id, text)

    def work_bot(self, longpoll, vk_session, *commands):
        for event in longpoll.listen():
            print(event.type)
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    if event.from_chat:
                        print(event.type)
                        print('Новое сообщение:')
                        print('Для меня от:', event.chat_id)
                        print('Текст:', event.text)
                        splitted_event_text = event.text.split('; ')
                        print(splitted_event_text)
                        for command in commands:
                            if command.get_name() in splitted_event_text:
                                result = command.execute(*splitted_event_text[1:])
                                send_mes(vk_session, event.chat_id, result)
            if event.type == VkEventType.CHAT_UPDATE:
                text = '''Приветствую вас! Я Бот Кулинарная книга.
    Я смогу (когда-нибудь) написать определённый рецепт блюда, 
    написать список блюд, у которых есть рецепт в книге,
    добавлять в список новые блюда и прочие действия.'''
                send_mes(vk_session, event.chat_id, text)


if __name__ == '__main__':
    bot = CookingBot(token='1960805a354085e3eff3b7604706f98fb505669be7f68e3564080a4b19c5efb032c8de2530676593c891f')


