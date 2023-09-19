from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Coplan:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Abrir e Fechar
    def Open(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.gp.srv.br/rh_dpemt/servlet/login') # https://wf.coplan.inf.br/rh/servlet/login
        self.driver.maximize_window()
        # self.Select('//*[@id="vBANCO_DADOS"]', '39')
        self.Input('//*[@id="vUSUARIO_LOGIN"]', f'{self.username}')
        self.Input('//*[@id="vUSUARIO_SENHA"]', f'{self.password}')

    def Close(self):
        if hasattr(self, 'driver'):
            self.driver.close()

        # Funções Normais
    def Mouse(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        ActionChains(self.driver).move_to_element(element).perform()

    def Click(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.click()

    def Input(self, xpath, info):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        self.driver.execute_script(
            "arguments[0].value = arguments[1];"
            "arguments[0].dispatchEvent(new Event('input'))",
            element,
            info
        )
        element.send_keys(Keys.TAB)

    def Select(self, xpath, info):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        select = Select(element)
        select.select_by_value(str(info))

    def Read(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        data = element.text
        return data

    def Clear(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.clear()

    def CaixaTexto(self, xpath, info):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        info = "\n".join(info)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, info)

    def Tab(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.send_keys(Keys.TAB)

    def SelectI(self, xpath, texts):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        select = Select(element)
        o_ptions = select.options
        for option in o_ptions:
            text = option.text
            value = option.get_attribute('value')
            if text == texts:
                select.select_by_value(str(value))
                break

        # Funções Iframe
    def ClickIframe(self, xpath):
        iframe = (By.XPATH, '//*[@id="gxp0_ifrm"]')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        self.driver.switch_to.default_content()

    def InputIframe(self, xpath, info):
        iframe = (By.XPATH, '//*[@id="gxp0_ifrm"]')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];"
            "arguments[0].dispatchEvent(new Event('input'))",
            element,
            info
        )
        element.send_keys(Keys.TAB)
        self.driver.switch_to.default_content()

    def SelectIframe(self, xpath, info):
        iframe = (By.XPATH, '//*[@id="gxp0_ifrm"]')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        element = self.driver.find_element(By.XPATH, xpath)
        select = Select(element)
        select.select_by_value(str(info))
        self.driver.switch_to.default_content()

    def ReadIframe(self, xpath):
        iframe = (By.XPATH, '//*[@id="gxp0_ifrm"]')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        element = self.driver.find_element(By.XPATH, xpath)
        data = element.text
        self.driver.switch_to.default_content()
        return data

    def ClearIframe(self, xpath):
        iframe = (By.XPATH, '//*[@id="gxp0_ifrm"]')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        self.driver.switch_to.default_content()

    def TabIframe(self, xpath):
        iframe = (By.XPATH, '//*[@id="gxp0_ifrm"]')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        element = self.driver.find_element(By.XPATH, xpath)
        element.send_keys(Keys.TAB)
        self.driver.switch_to.default_content()

        # Janelas
    def OpenWindow(self):
        janela = self.driver.window_handles
        self.driver.switch_to.window(janela[-1])

    def CloseWindow(self):
        janela = self.driver.window_handles
        self.driver.switch_to.window(janela[0])