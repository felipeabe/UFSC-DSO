from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        if isinstance(nome,str):
            self.__nome=nome
        if isinstance(codigo,int):
            self.__codigo=codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome