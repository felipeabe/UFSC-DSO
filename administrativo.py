from funcionario import Funcionario

class Administarivo(Funcionario):
    def __init__(self, departamento,cpf):
        self.dias_de_emprestimo=10
        super().__init__(departamento,cpf,self.__dias_de_emprestimo)

    def emprestar(self,titulo_livro):
        if isinstance(titulo_livro, str):
            return f'Funcionário administrativo'+super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            return f'Funcionario administrativo'+super().devolver(titulo_livro)
