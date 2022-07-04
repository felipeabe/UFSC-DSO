from imposto import Imposto


class ICMS(Imposto):
    def __init__(self, aliquota, incidencia_impsoto, diferenca_estado: float):
        super().__init__(aliquota, incidencia_impsoto)
        self.__aliquota = aliquota
        self.__diferenca_estado = diferenca_estado

    @property
    def diferenca_estado(self):
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, diferenca_estado):
        if isinstance(diferenca_estado, float) and diferenca_estado:
            self.__diferenca_estado = diferenca_estado

    def calcula_aliquota(self) -> float:
        return self.__aliquota + self.__diferenca_estado

