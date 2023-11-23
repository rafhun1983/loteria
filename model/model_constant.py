class Model_Constant:

    def __init__(self, first_balance, min_dig, max_dig,len_list_numbers_20,winner_procent,loser_procent,pirat_off_on):
        self.__first_balance = first_balance
        self.__min_dig = min_dig
        self.__max_dig = max_dig
        self.__len_list_numbers_20 = len_list_numbers_20
        self.__winner_procent = winner_procent
        self.__loser_procent = loser_procent
        self.__pirat_off_on = pirat_off_on


    @property
    def first_balance(self):
        return self.__first_balance

    @first_balance.setter
    def first_balance(self, first_balance):
        self.__first_balance = first_balance

    @property
    def min_dig(self):
        return self.__min_dig

    @min_dig.setter
    def min_dig(self, min_dig):
        self.__min_dig = min_dig

    @property
    def max_dig(self):
        return self.__max_dig

    @max_dig.setter
    def max_dig(self, max_dig):
        self.__max_dig = max_dig

    @property
    def len_list_numbers_20(self):
        return self.__len_list_numbers_20

    @len_list_numbers_20.setter
    def len_list_numbers_20(self,len_list_numbers_20):
        self.__len_list_numbers_20 = len_list_numbers_20

    @property
    def winner_procent(self):
        return self.__winner_procent

    @winner_procent.setter
    def winner_procent(self,winner_procent):
        self.__winner_procent = winner_procent

    @property
    def loser_procent(self):
        return self.__loser_procent

    @loser_procent.setter
    def loser_procent(self,loser_procent):
        self.__loser_procent = loser_procent

    @property
    def pirat_off_on(self):
        return self.__pirat_off_on

    @pirat_off_on.setter
    def pirat_off_on(self,pirat_off_on):
        self.__pirat_off_on = pirat_off_on














