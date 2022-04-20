import sqlite3
import command_structure


def whattocookfrom(ingridients):
    ingridients = ingridients.split('; ')
    connection = sqlite3.connect('cooking.db')
    cursor = connection.cursor()
    text1 = '%" AND ingridients LIKE "%'.join(ingridients)
    list_of_meals = cursor.execute(f'''SELECT meal_type, name FROM meal_types 
    JOIN cereal ON meal_types.id = cereal.id
    WHERE ingridients LIKE "%{text1}%"''').fetchall()
    if list_of_meals:
        return "вы можете приготовить: " + ';\n'.join(map(lambda x: ' '.join(x), list_of_meals))
    else:
        return 'вы ничего не можете с этими ингредиентами приготовить'


whattocookfrom_command = command_structure.Command()
whattocookfrom_command.add_keys(['что приготовить из', 'что сделать из', 'блюдо из'])
whattocookfrom_command.process = whattocookfrom
whattocookfrom_command.set_description('блюдо из предоставленных ингридиентов')

