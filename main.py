from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://linkedin.com")
browser.fullscreen_window()
time.sleep(5)
usernameS = "Your UserName"
usernameP = "Your Password"
login = browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(3)
email = browser.find_element_by_xpath("//*[@id='username']")
sifre = browser.find_element_by_xpath("//*[@id='password']")
email.send_keys(usernameS)
sifre.send_keys(usernameP)
time.sleep(2)
loginButton = browser.find_element_by_css_selector("#organic-div > form > div.login__form_action_container > button")
loginButton.click()
time.sleep(2)
search_bar = browser.find_element_by_xpath("//*[@id='global-nav-typeahead']/input")
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(2)
contacts = browser.find_element_by_xpath("//*[@id='ember20']/span")
contacts.click()
time.sleep(5)
baglanti = browser.find_element_by_partial_link_text("Bağlantı")
baglanti.click()
time.sleep(10)
for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#Sayfa kaydırma kodu
    time.sleep(2)
followers = browser.find_elements_by_class_name("mn-connection-card__details")
followerList = []
for follower in followers:
    followerList.append(follower.text)
print(followerList)
with open("followers.txt","w",encoding="utf-8") as file:
    for follower in followerList:
        file.write(follower+"\n")
        file.write("-----------------------------")
time.sleep(30)
browser.quit()
