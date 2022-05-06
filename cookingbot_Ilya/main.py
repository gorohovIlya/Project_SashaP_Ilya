import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from help import help
from data import db_session, __all_models
from command_structure import AddMeal, HowToPrepare, WhatToCookFrom, RandomMeal, Help


def send_mes(vk, chat, text):
    random_id = randint(0, 2 ** 64)
    print(vk, chat, text, random_id)
    vk.method('messages.send', {'peer_id': chat, 'message': text, 'random_id': random_id})


def work_bot(longpoll, vk_session, *commands):
    for event in longpoll.listen():
        print(event.type)
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if event.from_chat:
                    print('Новое сообщение:')
                    print('Для меня от чата', event.chat_id)
                    print('Текст:', event.text)
                    splitted_event_text = event.text.split('; ')
                    print(splitted_event_text)
                    for command in commands:
                        if command.get_name() == splitted_event_text[0] == 'random_meal':  # проверка на random_meal
                            result = command.execute()
                            send_mes(vk_session, event.peer_id, result)
                            break
                        elif command.get_name() == splitted_event_text[0] == 'add_meal':  # остальные команды
                            try:
                                result = command.execute(event.user_id, *splitted_event_text[1:])
                            except:
                                result = 'скорее всего нельзя получить информацию про пользователя'
                            finally:
                                send_mes(vk_session, event.peer_id, result)
                                break
                        elif command.get_name() == splitted_event_text[0]:
                            result = command.execute(*splitted_event_text[1:])
                            send_mes(vk_session, event.peer_id, result)
                            break
                elif event.from_user:
                    user = vk_session.get_api().users.get(user_id=event.user_id, fields='domain')[0]
                    print('лс')
                    print('Новое сообщение:')
                    print(user)
                    print('Для меня от:', f'{user["first_name"]} {user["last_name"]}: @{user["domain"]}')
                    print('Текст:', event.text)
                    print(event.peer_id)
                    splitted_event_text = event.text.split('; ')
                    print(splitted_event_text)
                    if splitted_event_text[0] in ['помощь', 'помогите', 'help']:
                        send_mes(vk_session, event.peer_id, help())
                    for command in commands:
                        if command.get_name() == splitted_event_text[0] == 'random_meal':  # проверка на random_meal
                            result = command.execute()
                            send_mes(vk_session, event.peer_id, result)
                            break
                        elif command.get_name() == splitted_event_text == 'add_meal':  # остальные команды
                            if splitted_event_text[1] == "set_admin":
                                result = command.set_admin(event.peer_id, splitted_event_text[2])
                                send_mes(vk_session, event.peer_id, result)
                                break
                            result = command.execute(event.peer_id, *splitted_event_text[1:])
                            send_mes(vk_session, event.peer_id, result)
                            break
                        elif command.get_name() == splitted_event_text[0]:
                            result = command.execute(*splitted_event_text[1:])
                            send_mes(vk_session, event.peer_id, result)
                            break
        if event.type == VkEventType.CHAT_UPDATE:
            text = '''Приветствую вас! Я Бот Кулинарная книга.
Я смогу (когда-нибудь) написать определённый рецепт блюда, 
написать список блюд, у которых есть рецепт в книге,
добавлять в список новые блюда и прочие действия.'''
            send_mes(vk_session, event.chat_id, text)


class CookingBot:
    def __init__(self, token):
        self.token = token
        # self.commands = [commands]
        self.init()

    def init(self):
        db_session.global_init("db/test_cooking.db")
        vk_session = vk_api.VkApi(
            token=self.token)
        add_m = AddMeal(self, 'add_meal', 'добавление блюда в базу данных')
        how_to_pr = HowToPrepare(self, 'how_to_prepare', 'получение рецепта блюда')
        what_to_cook = WhatToCookFrom(self, 'what_to_cook_from', 'получение названия блюда, которое можно сделать из \
                                                                 введенных ингридиентов')
        help = Help(self, 'help', 'информация о командах')
        rand_meal = RandomMeal(self, 'random_meal', 'получение названия случайного блюда из базы данных')
        longpoll = VkLongPoll(vk_session)
        print('работаем')
        work_bot(longpoll, vk_session, add_m, how_to_pr, what_to_cook, rand_meal, help)


if __name__ == '__main__':
    bot = CookingBot(token='1960805a354085e3eff3b7604706f98fb505669be7f68e3564080a4b19c5efb032c8de2530676593c891f')
