from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes=[]
        self.__tecnicos=[]
        super().__init__()

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self)-> list:
        return self.__tecnicos


    def inclui_cliente(self, codigo :int, nome :str) -> Cliente:
        if isinstance(codigo, int) and codigo is not None and isinstance(nome, str) and nome is not None:
            cliente_i=0
            for cliente in self.__clientes:
                if cliente.codigo==codigo:
                    cliente_i+=1
            if cliente_i==0:
                cliente=Cliente(nome,codigo)
                self.__clientes.append(cliente)
            return self.__clientes[-1]

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        if isinstance(codigo, int) and codigo is not None and isinstance(nome, str) and nome is not None:
            tecnico_i=0
            for tecnico in self.__tecnicos:
                if tecnico.codigo==codigo:
                    tecnico_i+=1
            if tecnico_i==0:
                tecnico=Tecnico(nome,codigo)
                self.__tecnicos.append(tecnico)
            return self.__tecnicos[-1]





