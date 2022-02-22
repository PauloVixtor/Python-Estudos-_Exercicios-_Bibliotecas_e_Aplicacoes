from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import json
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pandas
from openpyxl import Workbook, load_workbook, cell
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


i = pd.read_excel('testepy.xlsx')
b = pd.read_excel('testepy.xlsx', dtype=str)
wb = load_workbook(r'testepy.xlsx')

planilha = wb.worksheets[0]

count_row = i.shape[0]
driver = webdriver.Chrome(executable_path=r'C:\Users\paulo.v.oliveira\Downloads\chromedriver.exe')



driver.get('https://nfse.salvador.ba.gov.br/site/contribuinte/nota/nota.aspx')

driver.find_element_by_id("lnkCertificadoDigital").send_keys(Keys.RETURN)
sleep(20)

# Clique manualmente no certificado

driver.find_element_by_name('btAcesso').send_keys(Keys.RETURN)

for c in range(0, count_row, 1):
    if (i['NOTA'][c]) == 0:
        sleep(0)
    else:
        driver.find_element_by_link_text("Consulta NFS-e").click()
        driver.find_element_by_name('ctl00$MainContent$tbNFe').send_keys('{}'.format(i['NOTA'][c]))
        driver.find_element_by_name('ctl00$MainContent$btNFe').send_keys(Keys.RETURN)
        sleep(2)
        driver.find_element_by_name('ctl00$MainContent$btImprimir').send_keys(Keys.RETURN)
        driver.switch_to.window()
        driver.find_element_by_xpath("//select[@class='md-select']/option[text()='Salvar como PDF']").click()
        driver.find_element_by_link_text("Imprimir").click()

driver.close()