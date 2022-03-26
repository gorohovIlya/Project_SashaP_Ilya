from random import choice
import sqlite3
from howtoprepare import howtoprepare


def randommeal():
    connection = sqlite3.connect('cooking.db')
    cursor = connection.cursor()
    # meals = list(map(lambda x: ''.join(x), cursor.execute('SELECT meal_type FROM meal_types').fetchall()))
    # meal = choice(meals)
    meal = 'каша'
    mtype = cursor.execute(f'SELECT meals FROM meal_types WHERE meal_type = "{meal}"').fetchall()
    mtype = choice(mtype[0][0].split(', '))
    return f"{meal} {mtype}\n{howtoprepare(' '.join([meal, mtype]))}"


if __name__ == '__main__':
    print(randommeal())
