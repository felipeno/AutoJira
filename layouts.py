import PySimpleGUI as sg


def home_screen():
    sg.theme('DarkAmber')
    layout = [
        [sg.Button('CONFIG', key='configuration_button')],
        [sg.Checkbox('HOJE'), sg.Checkbox('CONFIGURAÇÃO')],
        [sg.Button('BATER PONTO')],
        [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')]
    ]
    return sg.Window('Home screen', layout=layout, finalize=True)


def configuration_screen():
    sg.theme('DarkAmber')
    column_to_be_centred = [
        [sg.Text('SeniorX')],
        [sg.Text('Login'), sg.Input()],
        [sg.Text('Senha'), sg.Input()],
        [sg.Text('Jira')],
        [sg.Text('Login'), sg.Input()],
        [sg.Text('Senha'), sg.Input()],
        [sg.Checkbox('SALVAR LOGINS')],
    ]

    layout = [
        [sg.Button('VOLTAR', key='back_button')],
        [sg.Column(column_to_be_centred, element_justification='center')]
    ]
    return sg.Window('Configuration screen', layout=layout, finalize=True)
