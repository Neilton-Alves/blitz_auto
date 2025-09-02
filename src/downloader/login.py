from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Abre o navegador
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://blitzrh.sydle.one/login/")

# Espera o campo de usuário aparecer
login = WebDriverWait(navegador, 30).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# Espera o campo de senha aparecer
password = WebDriverWait(navegador, 30).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

# Preenche usuário e senha
login.send_keys("neilton.cruz")
password.send_keys("neilton.cruz" + Keys.ENTER)

# Aguarda o login acontecer (URL mudar)
WebDriverWait(navegador, 30).until(
    EC.url_changes("https://blitzrh.sydle.one/login/")
)

print("✅ Login realizado com sucesso!")

time.sleep(30)