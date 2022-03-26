import sqlite3


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
