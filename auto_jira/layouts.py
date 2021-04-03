import PySimpleGUI as sg


def home_screen():
    sg.theme('DarkAmber')
    column_to_be_centred = [
        [sg.Button('BATER PONTO', key='run')],
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
        [sg.Text('Email', size=(5, 1)), sg.Input(size=(30, 1), key='seniorx_email')],
        [sg.Text(size=(5, 1)), sg.Text('', size=(30, 1), text_color='red', key='seniorx_email_error')],
        [sg.Text('Senha', size=(5, 1)), sg.Input(size=(30, 1), key='seniorx_pass')],
        [sg.Text(size=(5, 1)), sg.Text('', size=(30, 1), text_color='red', key='seniorx_pass_error')],
        [sg.Text('Jira')],
        [sg.Text('Email', size=(5, 1)), sg.Input(size=(30, 1), key='jira_email')],
        [sg.Text(size=(5, 1)), sg.Text('', size=(30, 1), text_color='red', key='jira_email_error')],
        [sg.Text('Senha', size=(5, 1)), sg.Input(size=(30, 1), key='jira_pass')],
        [sg.Text(size=(5, 1)), sg.Text('', size=(30, 1), text_color='red', key='jira_pass_error')],
        [sg.Checkbox('Salvar usuários')],
    ]

    layout = [
        [sg.Button('VOLTAR', key='back_button'), sg.Text(key='atualization_text')],
        [sg.Column(column_to_be_centred, element_justification='center')]
    ]
    return sg.Window('AutoJIRA - Configuração', layout=layout, finalize=True)
