from abc import ABC, abstractmethod
from incidenciaImposto import IncidenciaImposto


class Imposto(ABC):


    @abstractmethod
    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        if isinstance(aliquota, float) and aliquota:
            self.__aliquota = aliquota
        if isinstance(incidencia_imposto, IncidenciaImposto) and incidencia_imposto:
            self.__incidencia_imposto = incidencia_imposto

    @property
    def aliquota(self):
        return self.__aliquota


    @property
    def incidencia_imposto(self):
        return self.__incidencia_imposto

    @abstractmethod
    def calcula_aliquota(self) -> float:
        pass
'''
Operacao abstrata que ira calcular a aliquota
Cada classe que ira estender Imposto devera implementar o calculo de acordo 
com a sua regra  
'''



