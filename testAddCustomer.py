# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class testAddCustomer(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_testAddCustomer(self):
        success = True
        wd = self.wd

        self.openPage(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        ActionChains(wd).move_to_element(wd.find_element_by_id("LoginForm")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("pass")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("LoginForm")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]")).perform()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("strong")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("hr")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("searchform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("nav")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("li.all")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("add new")).perform()
        wd.find_element_by_link_text("add new").click()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("add new")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']//h1[.='Edit / add address book entry']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("firstname")).perform()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("test1")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("test2")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("test3")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys("\\9")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("test3")
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("middlename")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("nickname")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("photo")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("title")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("company")).perform()
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("\\undefined")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("tetst53")
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("address")).perform()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys("\\undefined")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("rwrwerwerwerwerwr")
        ActionChains(wd).move_to_element(wd.find_element_by_name("home")).perform()
        wd.find_element_by_name("home").click()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        wd.find_element_by_name("theform").click()
        ActionChains(wd).move_to_element(wd.find_element_by_name("home")).perform()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("rewrew")
        ActionChains(wd).move_to_element(wd.find_element_by_name("mobile")).perform()
        wd.find_element_by_name("mobile").click()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("home")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("mobile")).perform()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("231321")
        ActionChains(wd).move_to_element(wd.find_element_by_name("fax")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("email")).perform()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys("\\undefined")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test@onet.pl")
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("email3")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("homepage")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("new_group")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("bmonth")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("bday")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("homepage")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("homepage")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("bday")).perform()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys("\\undefined")
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']//option[.='15']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']//option[.='14']")).perform()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").click()
        ActionChains(wd).move_to_element(wd.find_element_by_name("email2")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("bmonth")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("bday")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("bmonth")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']//option[.='December']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']//option[.='September']")).perform()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").click()
        ActionChains(wd).move_to_element(wd.find_element_by_name("email3")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("homepage")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("byear")).perform()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("ayear")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("\\undefined")
        wd.find_element_by_name("theform").click()
        ActionChains(wd).move_to_element(wd.find_element_by_id("container")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("theform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']/form/input[21]")).perform()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("footer")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("container")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.msgbox")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("home page")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("maintable")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//table[@id='maintable']//td[.='test1']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//table[@id='maintable']//td[.='rwrwerwerwerwerwr']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("th.sortable.fd-column-4")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("nav")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("header")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Logout")).perform()
        wd.find_element_by_link_text("Logout").click()
        ActionChains(wd).move_to_element(wd.find_element_by_id("header")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("All e-mail")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("LoginForm")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        self.assertTrue(success)

    def openPage(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()