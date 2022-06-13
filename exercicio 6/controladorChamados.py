from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        super().__init__()
        self.__chamados = []
        self.__tiposChamados = []

    # Retorna o total de chamados registrados para o TipoChamado recebido como parametro
    # @param tipo TipoChamado
    # @return int com a quantidade total dos chamados daquele tipo
    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        numero=0
        if isinstance(tipo,TipoChamado) and tipo is not None:
            for chamado in self.__chamados:
                if chamado.tipo==tipo:
                    numero+=1
        return numero


    # Permite incluir um novo chamado na lista de Chamados. O chamado incluido eh retornado como um Chamado
    # @param data data do chamado em formato Date
    # @param cliente referencia para o Cliente do chamado
    # @param tecnico referencia para o Tecnico do chamado
    # @param titulo titulo do chamado
    # @param descricao descricao do chamado
    # @param prioridade prioridade do chamado
    # @param tipo tipo do chamado (TipoChamado)
    # @return retorna o chamato cadastrado
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado) -> Chamado:

        if isinstance(data, Date) and data is not None\
            and isinstance(cliente,Cliente) and cliente is not None\
            and isinstance(tecnico,Tecnico) and tecnico is not None\
            and isinstance(titulo,str) and titulo is not None\
            and isinstance(descricao,str) and descricao is not None\
            and isinstance(prioridade,int) and prioridade is not None\
            and isinstance(tipo, TipoChamado) and tipo is not None:
            numero=0
            for chamado in self.__chamados:
                if chamado.cliente==cliente and chamado.data==data and chamado.tecnico==tecnico and chamado.tipo==tipo:
                    numero+=1
            if numero==0:
                chamado=Chamado(data,cliente,tecnico,titulo,descricao, prioridade, tipo)
                self.__chamados.append(chamado)
            return self.__chamados[-1]


    # Permite incluir um novo TipoChamado na lista de Tipos de Chamado. O TipoChamado incluido eh retornado como um TipoChamado
    # @param codigo codigo do Tipo Chamado
    # @param nome nome do Tipo Chamado
    # @param descricao descricao do Tipo Chamado
    # @return retorna o Tipo Chamado cadastrado
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        if isinstance(codigo,int) and codigo is not None\
            and isinstance(nome,str) and nome is not None\
            and isinstance(descricao,str) and descricao is not None:

            numero=0
            for tipochamado in self.__tiposChamados:
                if tipochamado.codigo == codigo:
                    numero+=1
            if numero==0:
                tipo=TipoChamado(codigo,nome,descricao)
                self.__tiposChamados.append(tipo)
            return self.__tiposChamados[-1]


    def tipos_chamados(self):
        return self.__tiposChamados



    # Retorna os tipos de chamado que foram cadastrados no controlador pelo metodo inclui_tipochamado




