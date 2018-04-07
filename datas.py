
class Data:

    def __init__(self, dia = 1, mes = 1, ano = 2018):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.__dia, self.__mes, self.__ano))