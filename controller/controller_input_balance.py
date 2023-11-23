from model.model_balance import Model_Balance


class Controller_Input_Balance:

    def fun(self):

        x = input('if you want to top up your balance , enter yes: ').lower()
        while x == 'yes':

            try:
                print()
                balance = input('input your balance: ')
                if isinstance(float(balance), float) and float(balance) > 0 or balance == '0':
                    balance = float(balance)

                    break
            except ValueError:
                print('Please input your balance correct: ')
        else:
            balance = 0
        print()
        return Model_Balance(balance)
