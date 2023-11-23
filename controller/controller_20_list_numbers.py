from model.model_20_list_numbers import Model_20_List_Numbers
from controller.controller_constant import Controller_Constant
import random


class Controller_20_List_Numbers:

    def fun(self, number_1, number_2, t):

        min_dig = Controller_Constant().fun().min_dig
        max_dig = Controller_Constant().fun().max_dig
        len_list_numbers_20 = Controller_Constant().fun().len_list_numbers_20

        list_numbers_20 = set()
        if len(list(range(min_dig, max_dig + 1))) > len_list_numbers_20:

            if t:
                while len(list_numbers_20) < len_list_numbers_20:
                    list_numbers_20.add(random.randint(min_dig, max_dig))

            else:

                x = random.randint(0, 1)

                if x:
                    while len(list_numbers_20) < len_list_numbers_20:
                        digit = random.randint(min_dig, max_dig)
                        if digit != number_2:
                            list_numbers_20.add(digit)

                else:
                    while len(list_numbers_20) < len_list_numbers_20:
                        digit = random.randint(min_dig, max_dig)
                        if digit not in (number_1, number_2):
                            list_numbers_20.add(digit)

            print()
            print(*sorted(list(list_numbers_20)))
            print()
        else:
            print()
            print('ERROR !!! ERROR !!! ERROR !!!')
            print()

        return Model_20_List_Numbers(list_numbers_20)
