class Model_Kon:
    def __init__(self,kon):
        self.__kon = kon

    @property
    def kon(self):
        return self.__kon

    @kon.setter
    def kon(self,kon):
        self.__kon = kon
