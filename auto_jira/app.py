import PySimpleGUI as sg

from auto_jira.controller.controller import Controller
from auto_jira.model.service.validators import EmailValidator, PasswordValidator
from auto_jira.view.layouts import home_screen, configuration_screen


controller_obj = Controller

if __name__ == '__main__':
    home, configuration = home_screen(), None

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break

        if window == home and event == 'configuration_button':
            home.hide()
            configuration = configuration_screen()

        if window == configuration and event == 'back_button':
            check_emails = controller_obj.emails_validator([values.get('seniorx_email'), values.get('jira_email')])
            check_pass = controller_obj.passwords_validator([values.get('seniorx_pass'), values.get('jira_pass')])

            if not check_emails or not check_pass:
                window.Element('atualization_text').Update('Senha(s) ou email(s) inválido(s).')
            else:
                configuration.hide()
                home.un_hide()

    window.close()
