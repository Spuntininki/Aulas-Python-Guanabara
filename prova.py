import pyautogui
from time import sleep
import pandas as pd
import pyperclip

pyautogui.PAUSE = 1.5
pyautogui.press('win')
pyautogui.write('Bloco de Notas')
pyautogui.press('enter')
tabela = pd.read_excel(r'C:\Users\Lucas\Downloads\Vendas - Dez.xlsx')

text = f'''{tabela}
O faturamento total das vendas resulta em: {tabela["Valor Final"].sum():,.2f}
A quantidade de produtos é de: {tabela["Quantidade"].sum():,.2f}'''
pyperclip.copy(text)
pyautogui.hotkey('ctrl', 'v')




