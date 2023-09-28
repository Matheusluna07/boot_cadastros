# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Importar base de dados do produto 
# Passo 4: Cadastrar o primeiro produto
# Passo 5: Loop até o último produto  

import pyautogui
from time import sleep
#pyautogui.press -> apertar uma tecla
#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.hotkey -> ataho (combinar teclas - EX: Ctrl + V)


# Passo 1

pyautogui.press("win")         #clicar na tecla windows.
sleep(3)                       #Para evitar encavalar o processo.

pyautogui.write("Chrome")
pyautogui.press("enter")

#Navegador com mais de um perfil Chrome: descobrir localização do perfil.
#sleep(5)
#print(pyautogui.position())
sleep(5)                      #Para evitar delei ao abrir o perfil
pyautogui.click(x=1235, y=444)  #Para abrir o perfil escolhido para executar a tarefa.
#Se só tiver um perfil Chrome -> pyautogui.press("enter")

# Passo 2
sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") 
pyautogui.press("enter")
sleep(5)
pyautogui.click(x=2394, y=368) 
pyautogui.write("matheusgl180@gmail.com")
pyautogui.press("tab")
pyautogui.write("Matheus7748?")
pyautogui.press("tab")
pyautogui.press("enter")
sleep(3)
# Passo 3 
#importar tabela
import pandas as pd

cadastros = pd.read_csv("produtos.csv")  #tabela de produtos cadastrados salvo, essa tabela foi salvo em csv.
pyautogui.click(x=2326, y=252)


# Passo 4 e 5
for linha in cadastros.index:
    # clicar no campo de código
    pyautogui.click(x=2326, y=252)
    pyautogui.write(str(cadastros.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(cadastros.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(cadastros.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(cadastros.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(cadastros.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(cadastros.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = cadastros.loc[linha, "obs"] #Caso o produto esteja vázio, irá ser ignorado.
    
    if not pd.isna(obs):
        pyautogui.write(str(cadastros.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(50000) #Para rolar a páguina pra cima.