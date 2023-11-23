from model.model_numbers import Model_Numbers
from controller.controller_constant import Controller_Constant

class Controller_Numbers:

    def fun(self):
        min_dig = Controller_Constant().fun().min_dig
        max_dig = Controller_Constant().fun().max_dig
        print()
        print(f'select 2 numbers from')
        print()
        k = 1
        for i in range(min_dig,max_dig+1):
            print(str(i).rjust(1*(len(str(max_dig))+1)), end=' ')
            if k % 10 == 0:
                print()
            k += 1
        print()
        print()

        while True:
            number_1 = input('input first number: ')
            if len(number_1) and all(i.isdigit() for i in number_1) and min_dig <= int(number_1) <= max_dig:
                number_1 = int(number_1)
                break
            else:
                print()
                print(f'please input digit [{min_dig}:{max_dig}]')
                print()

        while True:
            number_2 = input('input second number: ')
            if len(number_2) and all(i.isdigit() for i in number_2) and min_dig <= int(number_2) <= max_dig and int(number_2) != number_1:
                number_2 = int(number_2)
                break
            else:
                print()
                print(f'please input digit [{min_dig}:{max_dig}]')
                print()

        print(f'your numbers is {number_1} and {number_2}')
        number_1 = Model_Numbers(number_1,number_2).number_1
        number_2 = Model_Numbers(number_1,number_2).number_2

        return number_1,number_2




