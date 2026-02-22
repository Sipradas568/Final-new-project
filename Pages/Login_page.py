from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
  
    url = "https://rahulshettyacademy.com/AutomationPractice"
    title = (By.XPATH, "//h1[text()= 'Practice Page']")
    suggestion = (By.ID,"autocomplete")
    name = (By.NAME, "enter-name")
    alertButton = (By.ID,"alertbtn")
    openWindow = (By.ID,"openwindow")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver

    



    def open_url(self):
        self.open(self.url)

    def enter_suggestion(self,text):
        self.enterText(self.suggestion,text)


    def alert_enter_name(self,name):
        self.enterText(self.name,name)

    def click_alert(self):
        self.click(self.alertButton)

    
   


     


