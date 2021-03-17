from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
Класс для работы с веб-драйвером
'''

class DriverManager:
    @staticmethod
    def webDrvierRun(path):
        driver = webdriver.Chrome(executable_path=path)
        assert Options.headless
        driver.maximize_window()
        print(driver.title)
        return driver
