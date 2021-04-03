import PySimpleGUI as sg

from auto_jira.validators import EmailValidator
from layouts import home_screen, configuration_screen

if __name__ == '__main__':
    home, configuration = home_screen(), None

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break

        if event == 'configuration_button':
            home.hide()
            configuration = configuration_screen()

        if event == 'back_button':
            configuration.hide()
            home.un_hide()
