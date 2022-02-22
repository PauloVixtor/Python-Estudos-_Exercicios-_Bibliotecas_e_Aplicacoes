import PySimpleGUI as sg

c = 0
sg.theme('Reddit')

layout = [[sg.Text(' Login'), sg.Input('',key='login')],
          [sg.Text('Senha'), sg.Input('',key='senha')],
          [sg.Button('OK'), sg.Button('Exit')]]
layout2 = [[sg.Print(c)]]

window = sg.Window('Login', layout)
window2 = sg.Window('Progresso', layout2)

while True:
    eventos, values = window.read()

    if eventos in (None, 'Exit'):
        break
    if eventos == 'OK':
            eventos, valores = window2.read()
            for cont in range(c, 20):
                eventos, valores = window2.read()
                if eventos in (None, 'Exit'):
                    break


