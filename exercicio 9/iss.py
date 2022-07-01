from imposto import Imposto
from incidenciaImposto import IncidenciaImposto


'''
O calculo da Aliquota do ISS (percentual do imposto) leva
em conta a lista de Servicos
Para cada servico cadastrado na lista de Servicos do ISS,
eh reduzido 0,1 da Aliquota.
Por exemplo, se a aliquota informada no construtor for 10.0 e
tiverem sido incluidos 2 servicos na lista,
entao a aliquota calculada sera de 9.8
'''


class ISS(Imposto):
    def __init__(self,aliquota, incidencia_imposto: IncidenciaImposto):
        super().__init__(aliquota,incidencia_imposto)
        self.__servicos=[]


    def inclui_servico(self, nome: str):
        if isinstance(nome,str) and nome:
            self.__servicos.append(nome)

    def exclui_servico(self, nome: str):
        for item in self.__servicos:
            if item==nome:
                self.__servicos.remove(item)

    def calcula_aliquota(self):
        desconto=(100-len(self.__servicos))/100
        return self.aliquota*desconto

