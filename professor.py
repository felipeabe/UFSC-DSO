from funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, departamento,cpf):
        self.dias_de_emprestimo=20
        super().__init__(departamento,cpf,self.__dias_de_emprestimo)


    def emprestar(self,titulo_livro:str):
        if isinstance(titulo_livro, str):
            return f'Professor'+super().emprestar(titulo_livro)

    def devolver(self,titulo_livro:str):
        if isinstance(titulo_livro, str):
            return f'Professor'+super().devolver(titulo_livro)

a=Professor('ctc',123)
print(a.emprestar('capitao cueca'))

