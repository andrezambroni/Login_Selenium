from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(r"C:\Users\devAZ\QA\Selenium\Login\login.html")

sleep(1)

navegador.find_element("xpath", '//*[@id="formulario"]/div/input[1]').send_keys(
    "andre@teste.com"
)
sleep(1)

navegador.find_element("xpath", '//*[@id="formulario"]/div/input[2]').send_keys(
    "123qwe"
)
sleep(1)

navegador.find_element("xpath", '//*[@id="formulario"]/div/a/button').click()

sleep(1)

navegador.find_element("xpath", '//*[@id="formulario"]/div/input[1]').send_keys(
    "Andre Zambroni"
)

sleep(1)

navegador.find_element("xpath", '//*[@id="formulario"]/div/input[2]').send_keys(
    "Campinas"
)

sleep(1)

navegador.find_element("xpath", '//*[@id="formulario"]/div/input[3]').send_keys("SP")

sleep(1)

navegador.find_element("xpath", '//*[@id="formulario"]/div/input[4]').send_keys(
    "Brasil"
)

sleep(1)

navegador.find_element("xpath", '//*[@id="download"]').click()


sleep(5)
