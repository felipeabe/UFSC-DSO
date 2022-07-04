from imposto import Imposto


'''
O calculo da Aliquota do IPI (percentual do imposto) leva em conta
se existe "aliquota_adicional".
Se existir aliquota_adicional, a aliquota e aumentada em 10%.
Por exemplo, se a aliquota informada no construtor for 10.0
e existe "aliquota_adicional", entao a aliquota calculada sera de 11.0.
'''


class IPI(Imposto):
    def __init__(self, aliquota, incidencia_imposto, aliquota_adicional: bool):
        super().__init__(aliquota, incidencia_imposto)
        self.__aliquota = aliquota
        self.__incidencia_imposto=incidencia_imposto
        if isinstance(aliquota_adicional, bool) and \
                aliquota_adicional is not None:
            self.__aliquota_adicional = aliquota_adicional

    def calcula_aliquota(self) -> float:
        if self.__aliquota_adicional is True:
            return self.__aliquota * 1.1
        else:
            return self.__aliquota




