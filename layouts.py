import PySimpleGUI as sg


# Criar janelas e estilos
def tela_inicial():
    sg.theme('DarkAmber')
    layout = [
        [sg.Button('CONFIG')],
        [sg.Checkbox('HOJE'), sg.Checkbox('CONFIGURAÇÃO')],
        [sg.Button('BATER PONTO')],
        [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')]
    ]
    return sg.Window('Tela inicial', layout=layout, finalize=True)


def tela_configuracao():
    sg.theme('DarkAmber')
    column_to_be_centred = [
        [sg.Text('SeniorX')],
        [sg.Text('Login'), sg.Input()],
        [sg.Text('Senha'), sg.Input()],
        [sg.Text('Jira')],
        [sg.Text('Login'), sg.Input()],
        [sg.Text('Senha'), sg.Input()],
        [sg.Checkbox('SALVAR LOGINS')],
        [
            sg.Input(key='A', size=(20, 1)),
            sg.CalendarButton('CONFIGURAÇÃO DE DIAS A SEREM BATIDOS',
                              close_when_date_chosen=True,
                              target='A',
                              location=(0, 0),
                              no_titlebar=False)
        ]
    ]

    layout = [
        [sg.Button('VOLTAR')],
        [sg.Column(column_to_be_centred, element_justification='center')]
    ]
    return sg.Window('Tela de configuração', layout=layout, finalize=True)


# Criar janelas iniciais


if __name__ == '__main__':
    janela1 = tela_configuracao()
    while True:
        evento, valor = janela1.read()
        print(evento,'******', valor)
        if evento in (sg.WIN_CLOSED, 'Exit'):
            break
