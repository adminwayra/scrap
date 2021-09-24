import numpy
import random
import pandas as pd
from time import sleep
from selenium import webdriver
web = 'https://www.olx.com.ec/autos_c378'
path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(web)
acupre=[]
acudesc=[]
boton=driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(5):
 try:
     boton.click()
     sleep(random.uniform(6.0,10.0))
     boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
 except:
     break

 # todos los anuncios de la lista
 autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for auto in autos:
    precio=auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print(precio)
    descripcion=auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(descripcion)
    acupre.append(precio)
    acudesc.append(descripcion)

df1=pd.DataFrame({'modelo':acudesc,'precio':acupre})
print(df1)
df1.to_csv('ejemplo.csv', index=False, encoding='utf-8')
#este es un comentario
#df1.to_excel('D:/ejemplo.xlsx',sheet_name='carro',engine='openpyxl')
   # datos=pd.read_excel('D:/ejemplo.xlsx',index_col=0,engine='openpyxl')




