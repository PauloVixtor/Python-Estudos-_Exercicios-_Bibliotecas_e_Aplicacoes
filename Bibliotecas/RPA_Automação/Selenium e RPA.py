from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pyautogui


driver = webdriver.Chrome(ChromeDriverManager().install())

pyautogui.alert('Programa irá iniciar, por favor não mexer!')
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
driver.find_element_by_name('endereco').send_keys('Mauá')
driver.find_element_by_name('btn_pesquisar').click()
sleep(2)
elems = driver.find_elements_by_xpath("//td[@data-th]")
lista = list()
for elem in elems:
    arquivo = elem.text
    lista.append(arquivo)
print(lista)
sleep(2)
driver.close()
pyautogui.PAUSE = 1.5
pyautogui.press('win')
pyautogui.write('bloco')
pyautogui.press('enter')
sleep(2)
for c in range(0, len(lista), 4):
    pyautogui.PAUSE = 0.2
    pyautogui.write(f'{lista[c]} |{lista[c + 1]} | {lista[c + 2]} |{lista[c + 3]}')
    if str(lista[c]) == 'Rua Mauá':
        pyautogui.write('| Valido!')
    else:
        pyautogui.write('| Invalido!')
    pyautogui.press('enter')
sleep(2)
pyautogui.hotkey('ctrl', 's')
sleep(2)
pyautogui.write('enderecos')
pyautogui.press('enter')
pyautogui.hotkey('alt', 'f4')
pyautogui.alert('FIM!')