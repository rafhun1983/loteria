class Model_Numbers:

    def __init__(self,number_1,number_2):
        self.__number_1 = number_1
        self.__number_2 = number_2

    @property
    def number_1(self):
        return self.__number_1

    @number_1.setter
    def number_1(self,number_1):
        self.__number_1 = number_1

    @property
    def number_2(self):
        return self.__number_2

    @number_2.setter
    def number_2(self,number_2):
        self.__number_2 = number_2
