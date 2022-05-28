from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf,dias_de_emprestimo, matricula):
        super().__init__(cpf,dias_de_emprestimo,matricula)
        self.__elaborando_tese=False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self,boolean):
        if isinstance(boolean,bool):
            self.__elaborando_tese=boolean

    def emprestar(self, titulo_livro: str):

        if self.__elaborando_tese==True:
            self.dias_de_emprestimo*=2
        if isinstance(titulo_livro, str):
            return super().emprestar(titulo_livro)

gama=AlunoPosGraduacao(12345678911,10,2022)
print(gama.emprestar("capitao cueca"))

gama.elaborando_tese=True
print(gama.emprestar('fraldinha suja'))


