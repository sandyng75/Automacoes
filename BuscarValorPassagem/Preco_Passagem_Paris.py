#%% Buscar valor da passagem para São Paulo / Paris

#%% Importar pacotes

from selenium import webdriver
import time
from datetime import datetime
import schedule

#%% Abrir navegador 

navegador = webdriver.Chrome()

#%%  link da página com o valor da passagem

link = "https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI1LTEwLTAxag0IAhIJL20vMDIycGZtcgwIAxIIL20vMDVxdGoaKRIKMjAyNS0xMC0yNWoMCAMSCC9tLzA1cXRqcg0IAhIJL20vMDIycGZtQAFIAXABggELCP___________wGYAQE&hl=pt-BR&gl=BR"
navegador.get(link)

#%% pegar o elemento da passagem mais barata (inspecionar)

preco = str("{:%B %d, %Y}".format(datetime.now()) + 
            "  Preço: "  +  
            navegador.find_element("class name", "jLMuyc").text +
            "\n")

#%% Adicionar linha no arquivo todos os dias às 09 horas
   
def tarefa():
    
     with open("preco_paris.txt","a", newline="\n") as arquivo:
          arquivo.write((f"{preco}\n"))   
          arquivo.close() 

schedule.every().day.at("09:00").do(tarefa)        

while True: 
    schedule.run_pending()
    time.sleep(1)     

#%% Fim    





