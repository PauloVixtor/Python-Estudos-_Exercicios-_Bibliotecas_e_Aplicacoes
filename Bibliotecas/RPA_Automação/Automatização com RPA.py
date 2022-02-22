import pyautogui
from time import sleep

#### Processo 1 ####
"""
# Todas as teclas do teclado

# print(pyautogui.KEYBOARD_KEYS)
# pyautogui.press('Winleft') # aperta a teclado windows a esquerda


# Alerta para usuarioa saber

pyautogui.alert("O codígo está sendo executado, não use nada nessa maquina")
pyautogui.PAUSE = 0.5 # Espera meio segundo a cada linha do codigo, o tempo pode ser alterado

# Abrir o one drive ( essas 3 primeiras linhas servem para abrir qualquer programa )

pyautogui.press('Win') # Apertar tecla do Windows
pyautogui.write('chorme')
pyautogui.press('enter')

sleep(1)
pyautogui.write('https://myoffice.accenture.com/personal/paulo_v_oliveira_accenture_com/_layouts/15/onedrive.aspx')
pyautogui.press('enter')

# Entrar na minha area de trabalho

# Tecla para ir diretamente a area de trabalho WIN + D

pyautogui.hotkey('winleft', 'd') # Comando de combinações de teclas
sleep(1)

# print(pyautogui.position()) # Visualizar a posição do mouse atual
sleep(1)
pyautogui.move(702, 210) # Mover o mouse na direção
pyautogui.mouseDown(702, 210)# pressiona e segura o botão do mouse
sleep(2)
pyautogui.move(448, 281)
sleep(2)

# Enquanto eu estou arrastando, eu vou entrar no one drive

pyautogui.hotkey('alt', 'tab')
sleep(3)

# Larguei o arquivo o one drive

pyautogui.mouseUp(300, 281)
sleep(3)

# Esperar alguns segundos
pyautogui.alert("Processo finalizado!")"""

#### Processo 2 ####

# Salvar bloco de notas

pyautogui.alert("O codígo está sendo executado, não use nada nessa maquina")
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('bloco')
pyautogui.press('enter')
pyautogui.write('Ola mundo!')
pyautogui.hotkey('ctrl', 's')
pyautogui.write('testeRPA')
pyautogui.press('enter')
pyautogui.alert("Processo finalizado!")

# outra forma de dar alt + tab
"""
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')"""

