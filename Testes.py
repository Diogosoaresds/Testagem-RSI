from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')
driver = webdriver.Chrome(service=service)


def CT_000():
    
    #entrando na conta
    driver.get('https://robertsspaceindustries.com/')
    
    time.sleep(5)
    
    elem = driver.find_element(By.XPATH, '//*[@id="overlay_close"]')
    elem.click()
    
    time.sleep(5)
    
    elem = driver.find_element(By.XPATH, '//*[@id="platform-bar"]/section/div/nav/ul[2]/li[3]/a')
    elem.click()
    time.sleep(5)

    elem = driver.find_element(By.NAME, 'email')
    elem.send_keys('diogozedau@gmail.com') 
    
    elem = driver.find_element(By.NAME, 'password')
    elem.send_keys('senhaqualquer')
    
    time.sleep(5)

    elem = driver.find_element(By.XPATH, '//*[@id="enlist-root"]/div/div/div[1]/form/div/button/div')
    elem.click()
    time.sleep(10)

    
def CT_004():
    
    #Tentando resgatar codigo
    driver.get('https://robertsspaceindustries.com/pledge/redeem-code')
    
    time.sleep(10)

    elem = driver.find_element(By.NAME, 'RedeemCode')
    elem.send_keys('2791027492017549') 
    
    time.sleep(5)
    
    elem = driver.find_element(By.XPATH, '//*[@id="d697887e-a055-4c7f-9572-e6b33b949e59"]/div/section/div/div/form/button')
    elem.click()
    
    time.sleep(5)

    assert "This code is not valid because it's expired, invalid or already claimed. If you believe this is an error, please contact RSI Customer Support." in driver.page_source
    
    
def CT_001():
    
    #tentando mudar nome da conta
    driver.get('https://robertsspaceindustries.com/account/settings')

    elem = driver.find_element(By.XPATH, '//*[@id="settings"]/div[1]/div[2]/div[4]/div/div/a')
    elem.click()
    
    time.sleep(10)

    elem = driver.find_element(By.XPATH, '//*[@id="settings_input_nickname"]')
    elem.send_keys('Karkuzz') 
    
    elem = driver.find_element(By.XPATH, '//*[@id="settings_input_password_nickname"]')
    elem.send_keys('senhaqualquer')
    
    time.sleep(5)
    
    elem = driver.find_element(By.XPATH, '//*[@id="settings"]/div[1]/div[2]/div[4]/div/div/div[2]/form/fieldset/a')
    elem.click()
    time.sleep(5)
    
    assert 'This handle is not available.' in driver.page_source
    
    
def CT_002():
    
    #tentar criar uma organização sem ter um pacote de jogo
    driver.get('https://robertsspaceindustries.com/community/orgs/create')
    
    #escolher nome da organização
    elem = driver.find_element(By.NAME, 'name')
    elem.send_keys('Pedro27') 

    elem = driver.find_element(By.NAME, 'symbol')
    elem.send_keys('asdbhaksd') 

    time.sleep(5)
    
    #Selecionar tipo de organização
    elem = driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[2]/div/div/div[1]/div[1]/div[1]')
    elem.click()
    
    time.sleep(3)
    
    #Selecionar linguagem
    elem = driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[3]/div/div[2]/a')
    elem.click()
    
    time.sleep(2)
    
    
    elem=driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[3]/div/div[2]/a/div[2]/div[2]/div/ul/li[2]')
    elem.click()
    
    time.sleep(3)
    
    #Selecionar atividade primaria
    elem = driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[3]/div/div[4]/div[1]/a')
    elem.click()
    
    time.sleep(2)

    elem = driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[3]/div/div[4]/div[1]/a/ul/li[2]')
    elem.click()    
    
    time.sleep(3)
    
    #Selecionar atividade secundaria
    elem = driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[3]/div/div[4]/div[2]/a')
    elem.click()
    
    time.sleep(2)

    elem = driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[3]/div/div[4]/div[2]/a/ul/li[2]')
    elem.click()    
    
    time.sleep(3)
    
    #Escrever introdução
    elem = driver.find_element(By.NAME, 'introduction')
    elem.send_keys('isso aqui não importa pq vai dar errado')
    
    time.sleep(3)
    
    #Clickar em criar
    elem = driver.find_element(By.XPATH, '//*[@id="create-organization"]/fieldset[3]/div/a/span[1]')
    elem.click()
    
    time.sleep(2)

    assert 'This account does not currently have a game package and cannot be part of an organization' in driver.page_source
    
    
def CT_003():
    
    #acabei tendo que mudar esse caso de uso pra tentar concluir a compra sem informar os dados
    #ja que o programa não reconhecia o local para inserir os dados de nenhuma forma.
    #inserir dados do cartão
    driver.get('https://robertsspaceindustries.com/store/pledge/cart')
    time.sleep(10)

    #Clickar em place order
    elem = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div/section/section[2]/main/div/section/div/button')
    elem.click()
    
    time.sleep(10)
    
    
    #nesta etapa vai ser necessario descer a pagina do acordo ja que o botão so vai estar
    #funcional apos a rolagem até o final
    #clickar em aceitar
    elem = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/aside/div/section/div[2]/button[2]')
    elem.click()
    
    time.sleep(15)
      
    elem = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/section/section[3]/main/div/form/div[1]/div/div/div/div[2]/div/div/article/button')
    elem.click()
    time.sleep(3)
    
    assert 'O número do seu cartão está incompleto.' in driver.page_source
    
    
def CT_005():

    driver.get('https://robertsspaceindustries.com/store/pledge/cart')
    
    time.sleep(5)

    #Clickar no botão
    elem = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/aside/button')
    elem.click()
    
    time.sleep(5)

    #Escolher item para comprar
    elem = driver.find_element(By.XPATH, '//*[@id="store-wrapper"]/div[3]/section[1]/div/div[4]/div[2]/div[1]/a[2]/span[1]')
    elem.click()
    
    time.sleep(2)
    
    #Ir pra pagina do carrinho
    #elem.send_keys(Keys.RETURN)
    driver.get('https://robertsspaceindustries.com/store/pledge/cart')
    time.sleep(10)
    
    #clickar pra prosseguir com a compra
    elem = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/section/section[1]/main/div/section/div[2]/button')
    elem.click()
    
    time.sleep(10)
    
    #Nesta etapa é necessario subir um pouco a pagina até o botão aparecer, eu não consegui
    #fazer com que ele fosse até o botão, ent na hora que ele vai clicar (se n tiver subido a 
    #pagina manualmente) ele vai dar um erro de que a automação iria clickar em um local diferente
    #Clickar pra adicionar endereço de pagamento
    elem = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/section/section[2]/main/div/section/section/div/article/header/button')
    elem.click()
    
    time.sleep(10)
    
    #Colocando informações
    elem = driver.find_element(By.NAME, 'firstname')
    elem.send_keys('Diogo')
    
    elem = driver.find_element(By.NAME, 'lastname')
    elem.send_keys('Soares')
    
    elem = driver.find_element(By.NAME, 'company')
    elem.send_keys('seila')
    
    elem = driver.find_element(By.NAME, 'addressLine')
    elem.send_keys('Av. Cel. Colares Moreira, 443 - Jardim Renascença, São Luís - MA')
    
    elem = driver.find_element(By.NAME, 'city')
    elem.send_keys('São Luiz')
    
    time.sleep(5)
    
    but = driver.find_element(By.NAME, 'submit')
    but.click()
    
    time.sleep(10)
    
    assert 'Required' in driver.page_source

    
    
    
if __name__ == '__main__':
    
    #adicionei o CT_000 ja que seria necessario estar logado para realizar as outras ações
    #os casos de uso não estão em ordem 001, 002, 003... ja que eu considerei melhor agrupar assim
    #ja que os casos 005 e 003 são realizados na mesma pagina, então seria mais pratico testar 
    #um após o outro
    CT_000()
    CT_001()
    CT_002()
    CT_005()
    CT_003()
    CT_004()
    
    driver.close()
