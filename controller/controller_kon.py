from model.model_kon import Model_Kon
from controller.controller_balance import Controller_Balance


class Controller_Kon:

    def fun(self,x):
        print()
        self.x = x
        max_kon = Controller_Balance().fun(x).balance
        print(f'input your kon (0:{max_kon}]')

        while True:
            kon = input('input your kon: ')
            try:
                if isinstance(float(kon), float) and float(kon) > 0 and max_kon - float(kon) >= 0:
                    kon = float(kon)
                    break
            except ValueError:
                print(f'input your kon (0:{max_kon}]')
        print(f'{kon=}')
        print()


        return Model_Kon(kon)



