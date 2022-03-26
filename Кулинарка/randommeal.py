from random import choice
import sqlite3
from howtoprepare import howtoprepare


def randommeal():
    connection = sqlite3.connect('cooking.db')
    cursor = connection.cursor()
    mtype = cursor.execute(f'''SELECT meal_type, name FROM meal_types 
JOIN cereal ON meal_types.id = cereal.id''').fetchall()
    meal = ' '.join(list(choice(mtype)))
    return f"{meal}\n{howtoprepare(meal)}"


if __name__ == '__main__':
    print(randommeal())
