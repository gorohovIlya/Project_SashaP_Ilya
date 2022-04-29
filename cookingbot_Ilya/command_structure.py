import data.db_session as db_session
from data.recipes import Recipe
import json


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
    #     self.__keys = []
    #     self.description = ''
    #     commands.append(self)
    #
    # def get_keys(self):
    #     return self.__keys
    #
    # def add_keys(self, keys):
    #     for key in keys:
    #         self.__keys.append(key)
    #
    # def set_description(self, description):
    #     self.description = description
    #
    # def process(self):
    #     pass


class HowToPrepare(Command):  # функция принимает название блюда и возвращает ингридиенты и способ приготовления
    def __init__(self, my_bot, name, description):
        super().__init__(my_bot, name, description)

    def execute(self, name):
        super().execute(name)


class AddMeal(Command):
    def __init__(self, my_bot, name, description):
        super().__init__(my_bot, name, description)
        self.execute_all()

    def create_reciepe(self, name, ingridients, cooking_method):
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
                new_recipe = self.create_reciepe(key, " ,".join(value["ingridients"]), " ,".join(value["cooking_method"]))
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
            new_recipe = self.create_reciepe(meal_name, meal_ingridients, meal_cooking_method)
            db_sess.add(new_recipe)
            db_sess.commit()
            return "рецепт успешно добавлен"
        else:
            return "такой рецепт уже есть"






