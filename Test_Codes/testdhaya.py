from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import dhaya_data
from Test_Locators.Locators import dhaya_locators
import pytest


class Test_Dhaya:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close() 
      
    def test_login_1(self, boot):
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(10)
        
        self.driver.find_element(by=By.NAME, value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.NAME, value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH, value=dhaya_locators().submitbutton).click()
        message = self.driver.find_elements(By.CLASS_NAME,"orangehrm-login-error")
        if any('Invalid credentials'in e.text for e in message):
            print('Invalid credentials')
        else:
            print('login sucess')
        dashboard=self.driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')
        assert dashboard

    def test_login_2(self, boot):
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(10)

        self.driver.find_element(by=By.NAME, value=dhaya_locators().username_inputbox).send_keys('dhaya')
        self.driver.find_element(by=By.NAME, value=dhaya_locators().password_inputbox).send_keys('dhaya123')
        self.driver.find_element(by=By.XPATH, value=dhaya_locators().submitbutton).click()
        message = self.driver.find_elements(By.CLASS_NAME,"orangehrm-login-error")
        if any('Invalid credentials'in e.text for e in message):
            print('Invalid credentials')
        else:
            print('login sucess')
        dashboard=self.driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')
        assert dashboard

    def test_add_data(self, boot):
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(10)

        self.driver.find_element(by=By.NAME,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.NAME,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().pim_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().add_locator).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().firstname_inputbox).send_keys('demo')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().lastname_inputbox).send_keys('2356')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().id_inputbox).send_keys('2356')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().save_button).click()

        add_success=self.driver.find_elements(By.XPATH,value='//*[@id="oxd-toaster_1"]')
        assert add_success

    def test_edit_data(self, boot):
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(10)

        self.driver.find_element(by=By.NAME,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.NAME,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()
       
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().pim_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().sort_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().sort_ascending).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().edit_button).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().edit_name).send_keys('demo1234567890')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().edit_save).click()
    
        edit_success=self.driver.find_elements(By.XPATH,value='//*[@id="oxd-toaster_1"]')
        assert edit_success

    def test_delete_data(self, boot):
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(10)

        self.driver.find_element(by=By.NAME,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.NAME,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().pim_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().sort_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().sort_ascending).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().delete_button).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().confirm_button).click() 

        delete_success=self.driver.find_elements(By.XPATH,value='//*[@id="oxd-toaster_1"]')
        assert delete_success