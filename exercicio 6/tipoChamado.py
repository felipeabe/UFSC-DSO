from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        if isinstance(codigo, int):
            self.__codigo=codigo

        if isinstance(descricao,str):
            self.__descricao=descricao

        if isinstance(nome,str):
            self.__nome=nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def nome(self) -> str:
        return self.__nome

