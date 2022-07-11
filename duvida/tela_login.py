import PySimpleGUI as sg


class Tela:
    def __init__(self):
        layout=[
            [sg.Text('Usuario',size=10),sg.Input(key='usuario')],
            [sg.Text('IDpokedex',size=10),sg.Input(key='idpokedex')],
            [sg.Button('Login',key='login'), sg.Button('Sair',key='sair')]
        ]

        self.janela=sg.Window('Tela de login').layout(layout)

    def abrir(self):
        evento, valores=self.janela.Read()
        return evento, valores

