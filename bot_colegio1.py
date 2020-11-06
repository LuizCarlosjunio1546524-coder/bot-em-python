from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class botcolegio:
    def __init__(self, instituicao, login, senha):
        self.instituicao = instituicao
        self.login = login
        self.senha = senha
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Luiz\Desktop\drivebot\chromedriver.exe')
        time.sleep(3)

    def logon(self):
        driver = self.driver
        driver.get('https://alunos.gr8.com.br/')
        time.sleep(2)
        inst_element = driver.find_element_by_xpath("//input[@name='inst']")
        inst_element.clear()
        inst_element.send_keys(self.instituicao)
        log_element = driver.find_element_by_xpath("//input[@name='login']")
        log_element.clear()
        log_element.send_keys(self.login)
        senha_element = driver.find_element_by_xpath("//input[@name='senha']")
        senha_element.clear()
        senha_element.send_keys(self.senha)
        senha_element.send_keys(Keys.RETURN)
        time.sleep(5)

bot = botcolegio('0','0','0')
bot.login()
