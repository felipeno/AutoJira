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

# Criar janelas iniciais


if __name__ == '__main__':
    tela_inicial()
    while True:
        a,b,c = sg.read_all_windows()
