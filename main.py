from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
def wait(time_of_sleep):
    return  time.sleep(time_of_sleep)
print("Bienvenue dans bot twitch pour commencer il faut rejoindre le server discord vous devre rentrer le lien du salon bot ainsi que la chaine twitch les bots sont bloqué à 50 tout les 5 minutes faites en bonne usage ;)")
link = input("le liens du salon ;)")
chanel = input("la chaine twitch ;)")
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(link)
with open('infos.json') as json_data:
    data = json.load(json_data)
    driver.find_element_by_name("email").send_keys(data['email'])
    driver.find_element_by_name("password").send_keys(data['password'])

driver.find_element_by_css_selector(".contents-18-Yxp").click()
wait(10)
while True:
    message = driver.find_element(By.CSS_SELECTOR,".markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP")
    message.send_keys("/tfollow " + chanel)
    wait(1)
    message.send_keys(Keys.ENTER)
    message.send_keys(Keys.ENTER)
    wait(300)
    continue


