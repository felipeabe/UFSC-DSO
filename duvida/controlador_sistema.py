from trabalho_maneirao.view.tela_sistema import TelaSistema
from trabalho_maneirao.view.tela_login import TelaLogin
from trabalho_maneirao.controladores.controlador_usuario import ControladorUsuario
from trabalho_maneirao.controladores.controlador_admin import ControleTreinador
from trabalho_maneirao.view.tela_admin import TelaAdmin
from telass import Tela


class ControladorSistema:


    def __init__(self):
        self.__tela_sistema=TelaSistema()
        self.__tela_Login=TelaLogin()
        self.__tela_admin=TelaAdmin()
        self.__controlador_usuario=ControladorUsuario(self)
        self.__controlador_admin=ControleTreinador(self)
        self.__usuario_logado=None
        self.__tela=Tela()


    @property
    def usuario_logado(self):
        return self.__usuario_logado


    def inicializa_sistema(self):
        self.abre_tela()

    ###################################################
    def entrar(self):
        self.__usuario_logado=None
        situacao = False
        while situacao == False:
            dados_login = self.__tela.abrir()


            """ESSA É A DUVIDA"""
            if dados_login(valores['usuario'])=="admin":
                self.__controlador_admin.abre_tela()
                situacao=True
            #################################################



            else:
                self.__usuario_logado=self.__controlador_admin.valida_treinador(dados_login["usuario"],dados_login["idpokedex"])
                if not self.__usuario_logado:
                    print('Dados incorretos')
                else:
                    situacao = True
                    self.__controlador_usuario.abre_tela()


    def sair(self):
        self.__tela_admin.mostra_mensagem('Programa encerrado com sucesso, volte sempre!')
        exit(0)


    def abre_tela(self):
        lista_opcoes = {1: self.entrar, 2:self.sair}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()