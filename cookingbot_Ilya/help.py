def help():
    return '''
    Вот что я умею:
    what_to_cook_from – возвращает список блюд, в которых используются введенные пользователем ингредиенты.
    how_to_prepare – возвращает список ингредиентов и способ приготовления введенного пользователем блюда
    random_meal – возвращает список случайного ингредиентов и способ приготовления блюда из базы данных
    ПРИМЕРЫ: (пишите без ковычек)
    how_to_prepare; <название блюда (в именительном падеже)>
    "how_to_prepare; каша перловая"
    "what_to_cook_from; <ингредиенты, пишутся все через '; '>"
    "random_meal"
    '''