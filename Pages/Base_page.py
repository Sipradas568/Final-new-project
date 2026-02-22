
class BasePage:
        
        

        def __init__(self,driver):
            self.driver = driver


        def open(self,url):
              self.driver.get(url)

        def click(self,locator):
              self.driver.find_element(*locator).click()

        def enterText(self,locator,text):
              self.driver.find_element(*locator).send_keys(text)


        def window_handle(self):
              wins = self.driver.window_handles
              for i in wins:
                    if i != self.driver.current_window_handle:
                          self.driver.switch_to.window(i)
                          break
                    
        
        def alert_accept(self):
              alert = self.driver.switch_to.alert
              alert.accept()
         

        def alert_text(self):
              alert = self.driver.switch_to.alert
              return alert.text
         