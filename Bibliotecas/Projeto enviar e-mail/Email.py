import PySimpleGUI as sg
import win32com.client as win32
from time import sleep


lista = list()
sg.theme('DarkTeal9')

layout = [
    [sg.Text('Digite seu e-mail: '), sg.Input(key='email_send', size=(30, 1)), sg.Button('limpar')],
    [sg.Button('Adicionar'), sg.Button('Enviar')]
]

janela = sg.Window('Enviar email', layout=layout)

while True:
    cadastrados = ''
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Adicionar':
        if valores['email_send'] == '':
            sg.popup('O e-mail não foi informado. Por favor digite novamente!')
            continue
        lista.append(valores['email_send'])
        janela['email_send'].Update('')
        sg.popup('Adicionado ao email!')
    if eventos == 'limpar':
        janela['email_send'].Update('')
        continue
    if eventos == 'Enviar':
        if str(valores['email_send']) != '':
            lista.append(valores['email_send'])
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)
        for c in lista:
            cadastrados += f'{c}' + '; '
        email.To = r'{}'.format(cadastrados)
        if email.To == '' and lista == []:
            sg.popup('O e-mail não foi informado. Por favor digite novamente!')
            continue
        email.Subject = 'Teste Python'
        email.HTMLBody = f"""
        <p>Olá, esse é um teste python!</p>

        <p>Sou um programador e estudo a linguagem de programação Python!</p>
        
        <p>Estou testando minhas habilidades.</p>

        <p>Abs,</p>

        <p>Programador em Python</p>
        """
        email.Send()
        sleep(2)
        sg.popup('Email enviado!')
        break