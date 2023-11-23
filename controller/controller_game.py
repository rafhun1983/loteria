from controller.controller_numbers import Controller_Numbers
from controller.controller_20_list_numbers import Controller_20_List_Numbers
from controller.controller_kon import Controller_Kon
from controller.controller_input_balance import Controller_Input_Balance
from controller.controller_constant import Controller_Constant
from model.model_balance import Model_Balance


class Controller_Game:

    def fun(self):
        t = Controller_Constant().fun().pirat_off_on
        min_balance = max_balance = 0
        first_balance = Controller_Constant().fun().first_balance
        if first_balance:
            print()
            print(f'for first time your balance is {first_balance}')
            print()
        Model_Balance(first_balance)

        game = input('if you want game input yes: ').lower()

        while game == 'yes':
            balance = Controller_Input_Balance().fun().balance
            balance += first_balance
            Model_Balance(balance)
            print(f'your balance is {balance}')

            if t == 1:
                max_balance = balance + balance * Controller_Constant().fun().winner_procent / 100
                min_balance = balance - balance * Controller_Constant().fun().loser_procent / 100
                t = '1'

            if balance == 0:
                print()
                print('with balance = 0 you can not continue, sorry')
                print()
                break


            number_1, number_2 = Controller_Numbers().fun()
            kon = Controller_Kon().fun(balance).kon
            new_balance = balance - kon

            print()
            print(f'your balance is {new_balance} ')
            print()

            Model_Balance(new_balance)


            if t == '1':
                if first_balance > max_balance:
                    off_on = False
                if first_balance <= min_balance:
                    off_on = True
            else:
                off_on = True


            list_numbers_20 = Controller_20_List_Numbers().fun(number_1, number_2, off_on).list_numbers_20


            if len(list_numbers_20) == 0:
                print()
                print('STOP !!! STOP !!! STOP !!!')
                print()
                print('proizoshla oshibka v sisteme, back kon')
                print()
                print(f'your balance is {new_balance+kon} ')
                Model_Balance(new_balance+kon)
                break

            winner = 0

            if number_1 in list_numbers_20 and number_2 in list_numbers_20:
                print()
                print('BINGOOOOO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(f'{number_1} and {number_2} in ',*list(list_numbers_20))
                print()
                winner = 10 * kon
            else:
                if number_1 in list_numbers_20:
                    print()
                    print(f'{number_1} in ',*list(list_numbers_20))
                    print()
                    winner = kon
                elif number_2 in list_numbers_20:
                    print()
                    print(f'{number_2} in ',*list(list_numbers_20))
                    print()
                    winner = kon

            new_balance += winner
            first_balance = new_balance

            if winner:
                print(f'your winner is {winner}')
                print(f'your balance is {new_balance} ')
            else:
                print('you are loser')

            print()
            print()

            game = input('if you want to continue the game, please input yes: ').lower()




















# x, do 1,2x








