class Command:
    def __init__(self, my_bot, name, description):
        self.my_bot = my_bot
        self.name = name
        self.description = description

    def execute(self, name):
        pass

    def get_info(self):
        return self.name, self.description

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