import pyautogui
import PySimpleGUI as sg

sg.theme('Reddit') # Tema escolhido


layout = [ # Criando layout
    [sg.Text('Usuario: '), sg.Input(key='usuario', size=(20, 1))], # Texto e informação a ser inserida com chave de localização, Tamanho
    [sg.Text('  Senha: '), sg.Input(key='senha', password_char='*', size=(20, 1))], # Texto, escrever, chave e proteção de dados, Tamanho
    [sg.Checkbox('Salvar o Login:')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout=layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Paulo' and valores['senha'] == '123':
            sg.popup('Seja Bem-vindo!')
            janela.close()
            pyautogui.alert('O codigo vai ser executado na sua maquina, por favor não mexer!')
            pyautogui.PAUSE = 1.8
            pyautogui.press('win')
            pyautogui.write('calculadora')
            pyautogui.press('enter')
            pyautogui.press('5')
            pyautogui.press('+')
            pyautogui.press('5')
            pyautogui.press('enter')
            pyautogui.hotkey('shift', 'f10')
            pyautogui.press('enter')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.press('win')
            pyautogui.write('bloco')
            pyautogui.press('enter')
            pyautogui.write('O resultado da conta é igual a : ')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pyautogui.write('Obrigado!')
            pyautogui.hotkey('ctrl', 's')
            pyautogui.write('Deu certo')
            pyautogui.press('enter')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.press('win')
            pyautogui.write('cmd')
            pyautogui.press('enter')
            pyautogui.press('f11')
            pyautogui.write(r'cd C:\Users\paulo.v.oliveira\Desktop')
            pyautogui.press('enter')
            pyautogui.write('dir')
            pyautogui.press('enter')
            # print(pyautogui.position())
            pyautogui.sleep(1)
            pyautogui.mouseDown(426, 439)
            pyautogui.mouseUp(426, 439)
            for c in range(0, 17):
                pyautogui.PAUSE = 0.5
                pyautogui.hotkey('shift', 'up')
            pyautogui.PAUSE = 1.8
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.press('win')
            pyautogui.write('deu certo')
            pyautogui.press('enter')
            pyautogui.press('down')
            for c in range(0, 2):
                pyautogui.press('enter')
            pyautogui.press('up')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('ctrl', 's')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.press('win')
            pyautogui.write('file')
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.write(r'C:\Users\paulo.v.oliveira\Desktop')
            pyautogui.press('enter')
            for c in range(0, 3):
                pyautogui.press('down')
            pyautogui.press('delete')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.alert('Finalizado!')
            # print(pyautogui.position())
        else:
            sg.popup('Senha ou Login incorreto. Por favor, informe novamente!')