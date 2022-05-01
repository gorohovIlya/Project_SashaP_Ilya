import data.db_session as db_session
from data.recipes import Recipe
import json
from random import choice

class Command:
    def __init__(self, my_bot, name, description):
        self.my_bot = my_bot
        self.name = name
        self.description = description

    def execute(self, *args):
        pass

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description


class HowToPrepare(Command):
    """
    This command accepts the name of the dish from the user and returns the ingredients and cooking method
    """
    def __init__(self, my_bot, name, description):
        super().__init__(my_bot, name, description)

    def execute(self, *args):
        db_sess = db_session.create_session()
        meal = args[0]
        my_query = db_sess.query(Recipe).filter(Recipe.name == meal)
        for elem in my_query:
            splitted_elem_ingridients = elem.ingridients.split(" ,")
            splitted_cooking_method = elem.cooking_method.split(" ,")
            return 'Ингридиенты:' + "\n" + "\n".join(splitted_elem_ingridients) + "\n" + 'Способ приготовления:' + "\n"\
                   + "\n".join(splitted_cooking_method)


class WhatToCookFrom(Command):
    """
    This command gets a list of ingredients from the user and returns the names of dishes that can be prepared from them
    """
    def __init__(self, my_bot, name, description):
        super().__init__(my_bot, name, description)

    def execute(self, *args):
        result = set()
        db_sess = db_session.create_session()
        user_ings = args[0].split('/')
        all_recipe_info = db_sess.query(Recipe).all()
        for elem in all_recipe_info:
            recipe_ings = elem.ingridients
            for ing in user_ings:
                if ing in recipe_ings:
                    result.add(elem.name)
        if result:
            return "Вы можете приготовить" + "\n" + "\n".join(list(result))

        else:
            return 'вы ничего не можете с этими ингредиентами приготовить'


class RandomMeal(Command):
    def __init__(self, my_bot, name, description):
        super().__init__(my_bot, name, description)

    def execute(self):
        db_sess = db_session.create_session()
        elem = choice(db_sess.query(Recipe).all())
        if elem != None:
            return f'Я выбрал случайное блюдо: {elem.name}' + '\n' + 'Ингридиенты:' + "\n" + "\n".join(elem.ingridients.split(' ,')) + "\n" + 'Способ приготовления:' + "\n"\
                   + "\n".join(elem.cooking_method.split(' ,'))
        else:
            return self.execute()


class AddMeal(Command):
    """
    This command accepts from the user the name of the dish, the list of ingredients, the method of preparation and adds
    a new recipe to the database
    """
    def __init__(self, my_bot, name, description):
        super().__init__(my_bot, name, description)
        self.execute_all()

    def create_recipe(self, name, ingridients, cooking_method):
        new_recipe = Recipe()
        new_recipe.name = name
        new_recipe.ingridients = ingridients
        new_recipe.cooking_method = cooking_method
        return new_recipe

    def execute_all(self):
        db_sess = db_session.create_session()
        with open('data/meals.json', 'r', encoding='UTF-8') as meals:
            data = json.load(meals)
        for key, value in data.items():
            recipe = db_sess.query(Recipe).filter(Recipe.name == key).first()
            print(recipe)
            if not recipe:
                new_recipe = self.create_recipe(key, " ,".join(value["ingridients"]), " ,".join(value["cooking_method"]))
                db_sess.add(new_recipe)
                db_sess.commit()
                print(new_recipe.name, new_recipe.ingridients, new_recipe.cooking_method)

    def execute(self, *args):
        db_sess = db_session.create_session()
        meal_name = args[0]
        meal_ingridients = args[1]
        meal_cooking_method = args[2]
        recipe = db_sess.query(Recipe).filter(Recipe.name == meal_name).first()
        if not recipe:
            new_recipe = self.create_recipe(meal_name, meal_ingridients, meal_cooking_method)
            db_sess.add(new_recipe)
            db_sess.commit()
            return "рецепт успешно добавлен"
        else:
            return "такой рецепт уже есть"


class AddUser(Command):
    pass






