#!/usr/bin/env python3

import requests, sys, signal, time, colorama,json, selenium,re,os,string,random
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
init()

def sig_handler(sig, frame):
    print(Fore.RED + "\n\n[!] Saliendo...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

#Variables Globales
mail_url= "https://api.mail.tm"
header={"Content-Type":"application/json"}
options = Options() #Importa las opciones de selenium
coins = 0

#Variables a modificar
password = "wuolahwuolah1234" #No es necesario modificar
invite_link= "https://www.wuolah.com/join-ur724737" #AQUÍ TU LINK DE INVITACIÓN
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' #AQUÍ EL PATH DE FIREFOX
driver_path=r'/home/m0b/WuolahMiner/geckodriver' #AQUÍ EL PATH DE TU DRIVER DE SELENIUM (Compatible con la versión de firefox)

#MAIN
session = requests.Session()
result = session.get(f"{mail_url}/domains") #Sacamos dominio de correo
result_dict= json.loads(result.text)
mail_domain = result_dict['hydra:member'][0]['domain']
while(True):
	os.system('cls;clear')
	print(Fore.GREEN + f"\n[+] WuolahCoins minadas esta sesión : {coins} \n")
	userID = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12)) #Creamos nombre random para usar en las cuentas
	#CREAR CUENTA MAIL
	mail= f"{userID}{mailNumber}@{mail_domain}"
	payload= {"address" : f"{mail}" , "password" : f"{password}"}
	result = session.post(f"{mail_url}/accounts", json=payload, headers=header ,timeout=5)
	if result.status_code == 201:
		print(Fore.YELLOW + "[1] Mail Desechable Creado")
	else:
		print(Fore.RED + "\n[!] Fallo al crear el Mail")
		sig_handler(None, None)

	#EXTRAER TOKEN
	result = session.post(f"{mail_url}/token",json=payload,headers=header,timeout=5)
	result_dict= json.loads(result.text) #Crea un diccionario con el resultado en formato json
	token= result_dict['token'] #Del diccionario selecciona el token
	if result.status_code == 200:
		print(Fore.YELLOW + "[2] Token Extraído")
	else:
		print(Fore.RED + "\n[!] Fallo al extraer el Token")
		sig_handler(None, None)

	#CREAR CUENTA WUOLAH
	options.headless = False ; service = Service(driver_path) ; driver = webdriver.Firefox(service=service,options=options) ; driver.get(invite_link)
	wait = WebDriverWait(driver, 1000) ; button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-1knxl3g"))); button.click() #Cookies
	wait = WebDriverWait(driver, 1000) ; button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-ai84mh"))) ; button.click() #Continue
	wait = WebDriverWait(driver, 1000) ; button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-e0l6jx"))) ; button.click() #Mail
	wait = WebDriverWait(driver, 1000) ; field = wait.until(EC.presence_of_element_located((By.ID, "email"))) ; field.send_keys(f"{mail}"); #Escribe Mail
	wait = WebDriverWait(driver, 1000) ; field = wait.until(EC.presence_of_element_located((By.ID, "password"))) ; field.send_keys(f"{password}"); field.submit() #Escribe contraseña
	#Ahora Resolver el captcha
	wait = WebDriverWait(driver, 1000) ; button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-17t3rxq"))) ; button.click() #Spain
	wait = WebDriverWait(driver, 1000) ; button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-160nu5g"))) ; button.click() #Aceptar
	time.sleep(5);driver.quit()
	print(Fore.YELLOW + "[3] Cuenta creada")

	#VERIFICACIÓN
	result = session.get(f"{mail_url}/messages",headers={"Content-Type":"application/json", "Authorization": f"Bearer {token}"},timeout=5)
	result_dict= json.loads(result.text)
	url_source = result_dict['hydra:member'][0]['downloadUrl'] #Accedemos al primer elemento de la lista hydra:member y extraemos downloadURL
	result = session.get(f"{mail_url}{url_source}",headers={"Content-Type":"application/json", "Authorization": f"Bearer {token}"},timeout=5)
	result = re.sub(r'=', '', result.text) ; result= re.findall(r'href3D"(.*?)"', result, re.DOTALL)
	url_verification = result[2].replace("\n", "").replace("\r", "") # Elimina saltos de línea y retornos de carro 
	options.headless = True ; service = Service(driver_path) ; driver = webdriver.Firefox(service=service,options=options) ; driver.get(url_verification)
	time.sleep(2)
	driver.quit() #Verifica Cuenta
	print(Fore.YELLOW + "[4] Cuenta verificada")
	coins=coins+3

