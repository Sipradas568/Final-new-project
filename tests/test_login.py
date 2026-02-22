from Pages.Login_page import LoginPage
from resources.data_read import get_data
import pytest
import os



base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(base_dir)
excel_path = os.path.join(base_dir,"resources","Test_data.xlsx")
print("path: ", excel_path)
print("exists: ", os.path.exists(excel_path))
testdata = get_data(excel_path,"Sheet1")
print("testdata:  ", testdata)


class Testlogin:
        
    @pytest.fixture
    def setup_class(self,driver):
        self.login = LoginPage(driver)
        self.login.open_url()
        return self.login
    
  

 
    
    @pytest.mark.parametrize("data",testdata)
    def test_alert(self,setup_class,data):
        
        self.login.alert_enter_name(data["Name"])
        self.login.click_alert()
        actual_alert_text = self.login.alert_text()
        assert data["Expected_Result"] == actual_alert_text
        self.login.alert_accept()










