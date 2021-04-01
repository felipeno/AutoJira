import PySimpleGUI as sg


def home_screen():
    sg.theme('DarkAmber')
    column_to_be_centred = [
        [sg.Button('BATER PONTO')],
        [sg.Text(key='atualization_text')],
        [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')]
    ]

    layout = [
        [sg.Button('CONFIGURAÇÃO', key='configuration_button')],
        [sg.Column(column_to_be_centred, element_justification='center')]
    ]
    return sg.Window('AutoJIRA - Principal', layout=layout, finalize=True)


def configuration_screen():
    sg.theme('DarkAmber')
    column_to_be_centred = [
        [sg.Text('SeniorX')],
        [sg.Text('Login', size=(5, 1)), sg.Input(size=(30, 1))],
        [sg.Text('Senha', size=(5, 1)), sg.Input(size=(30, 1))],
        [sg.Text('Jira')],
        [sg.Text('Login', size=(5, 1)), sg.Input(size=(30, 1))],
        [sg.Text('Senha', size=(5, 1)), sg.Input(size=(30, 1))],
        [sg.Checkbox('Salvar usuários')],
    ]

    layout = [
        [sg.Button('VOLTAR', key='back_button')],
        [sg.Column(column_to_be_centred, element_justification='center')]
    ]
    return sg.Window('AutoJIRA - Configuração', layout=layout, finalize=True)
