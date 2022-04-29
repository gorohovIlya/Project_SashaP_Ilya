# import sqlite3
# import command_structure
#
#
# def howtoprepare(meal):
#     try:
#         connection = sqlite3.connect('cooking.db')
#         cursor = connection.cursor()
#         meal = meal.split()
#         mtype = meal[0]
#         name = meal[1]
#         request_1 = cursor.execute(f"""SELECT meals FROM meal_types WHERE meal_type = '{mtype}'""").fetchall()
#         meal_list = ', '.join((list(request_1[0]))).split(', ')
#         for el in meal_list:
#             if el == name and mtype == 'каша':
#                 request_2 = cursor.execute(f"""SELECT ingridients, cooking_method FROM cereal WHERE name = '{el}'""").fetchall()
#                 ings = request_2[0][0].split(', ')
#                 cook = request_2[0][1].split('; ')
#                 return 'Ингридиенты:' + "\n" + "\n".join(ings) + "\n" + 'Способ приготовления:' + "\n" + "\n".join(cook)
#     except Exception as e:
#         print('ошибка')
#
#
# howtoprepare_command = command_structure.Command()
# howtoprepare_command.add_keys(['как приготовить', 'как сделать', 'рецепт'])
# howtoprepare_command.process = howtoprepare
# howtoprepare_command.set_description('рецепт блюда')

