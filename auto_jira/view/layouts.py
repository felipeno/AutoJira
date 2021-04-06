"""
This module contains the layout's definitions.
"""
import PySimpleGUI as sg


def home_screen():
    """
    This function defines the home screen organization layout.
    :return: window
    """
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
    """
    This function defines the configuration screen organization layout.
    :return: window
    """
    sg.theme('DarkAmber')
    column_to_be_centred = [
        [sg.Text('SeniorX')],
        [sg.Text('Email', size=(5, 1)), sg.Input(size=(30, 1), key='seniorx_email')],
        [sg.Text('Senha', size=(5, 1)), sg.Input(size=(30, 1), key='seniorx_pass')],
        [sg.Text('Jira')],
        [sg.Text('Email', size=(5, 1)), sg.Input(size=(30, 1), key='jira_email')],
        [sg.Text('Senha', size=(5, 1)), sg.Input(size=(30, 1), key='jira_pass')],
        [sg.Checkbox('Salvar usuários', key='save_users')],
    ]

    layout = [
        [sg.Button('VOLTAR', key='back_button'), sg.Text(key='atualization_text', size=(30, 1), text_color='red')],
        [sg.Column(column_to_be_centred, element_justification='center')]
    ]
    return sg.Window('AutoJIRA - Configuração', layout=layout, finalize=True)
