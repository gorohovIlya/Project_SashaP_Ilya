from random import choice
import sqlite3
from howtoprepare import howtoprepare
import command_structure


def randommeal():
    connection = sqlite3.connect('cooking.db')
    cursor = connection.cursor()
    mtype = cursor.execute(f'''SELECT meal_type, name FROM meal_types 
JOIN cereal ON meal_types.id = cereal.id''').fetchall()
    meal = ' '.join(list(choice(mtype)))
    return f"{meal}\n{howtoprepare(meal)}"


randommeal_command = command_structure.Command()
randommeal_command.add_keys(['случайное блюдо', 'рандомное блюдо', 'случайно', 'рандом'])
randommeal_command.process = randommeal
randommeal_command.set_description('случайное блюдо из базы данных бота')


if __name__ == '__main__':
    print(randommeal())
