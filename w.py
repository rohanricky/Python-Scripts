#implements selenium webdriver to log me into the website and fetch the rating

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://www.chess.com"
username = "xxxxx"#type your user name here
pas = "qwerty"#type your pass word

xpaths = {
'username' : "//input[@name='loginusername']",
'pass'     : "//input[@name='loginpassword']",
}
mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()

mydriver.find_element_by_xpath(xpaths['username']).clear()
mydriver.find_element_by_xpath(xpaths['username']).send_keys(username)
mydriver.find_element_by_xpath(xpaths['pass']).clear()
mydriver.find_element_by_xpath(xpaths['pass']).send_keys(pas)
mydriver.find_element_by_id('c2').click()
