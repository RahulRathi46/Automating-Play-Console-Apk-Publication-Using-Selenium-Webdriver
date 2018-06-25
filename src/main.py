import self as self
from selenium import webdriver
from os import system
from googletrans import Translator
from time import sleep
import json

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

service_urls=['translate.google.com','translate.google.co.kr']
translator = Translator(service_urls)

count = 0

with open(r"Context/title.txt","r") as title,open(r"Context/short.txt","r") as short:
    title = title.read()
    short = short.read()
    long = open(r"Context/long.txt","r")

with open(r'Config/playstore_language_config.json') as f:
    PLAYSTORE = json.load(f)

with open(r'Config/playstore_language_config.json') as f:
    LANGUAGES = json.load(f)


# create a new Firefox session
driver = webdriver.Firefox(executable_path=r'Runtime/geckodriver')
driver.maximize_window()


# navigate to the application home page
URL = driver.get("https://accounts.google.com/signin/v2/identifier?service=androiddeveloper&passive=1209600&continue=https%3A%2F%2Fplay.google.com%2Fapps%2Fpublish%2F%23&followup=https%3A%2F%2Fplay.google.com%2Fapps%2Fpublish%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
Confirm = input("Login with User & Pass (Enter)")

New = driver.find_element_by_css_selector("button[class='IF2W6TD-f-a IF2W6TD-f-r']").click()
command = 'echo ' + title.strip() + '| clip'
case = system(command)
Confirm = input("Paste project name : " + title + " (Enter)")

Confirm = input("Select add languages (Enter)")

language_button = driver.find_element_by_css_selector("button[class='IF2W6TD-f-a IF2W6TD-f-p IF2W6TD-f-n IF2W6TD-f-b IF2W6TD-f-c IF2W6TD-f-s']")

title_box = driver.find_element_by_css_selector("input[class='gwt-TextBox IF2W6TD-rn-d']")
short_box = driver.find_element_by_css_selector("textarea[class='gwt-TextArea IF2W6TD-di-d IF2W6TD-rn-d']")
long_box = driver.find_element_by_css_selector("textarea[class='gwt-TextArea IF2W6TD-rn-d']")

system('cls')
print("SR." + " |  " + "LANGUAGES" + " - " + "Encode" + " | Function Processing" + "................... [Status]")

for l in PLAYSTORE:
    count=count+1
    long.seek(0)
    sleep(1)

    update_language = driver.execute_script("arguments[0].setAttribute('data-lang-code','" + l + "')", language_button)
    script = driver.execute_script("arguments[0].setAttribute('aria-pressed','false')", language_button)
    sleep(5)
    language_button.click()

    title_box.clear()
    short_box.clear()
    long_box.clear()

    translate_title = translator.translate(title, dest=PLAYSTORE[l]).text
    translate_short = translator.translate(short, dest=PLAYSTORE[l]).text
    translate_long = translator.translate(long.read(), dest=PLAYSTORE[l]).text

    if PLAYSTORE[l]=='bg': translate_short=translate_title
    if PLAYSTORE[l]=='mk': translate_short=translate_title

    title_box.send_keys(translate_title[:50])
    sleep(1)
    short_box.send_keys(translate_short[:80])
    sleep(1)
    long_box.send_keys(translate_long[:4000])
    sleep(2)

    print(str(count) + " |  " + LANGUAGES[PLAYSTORE[l]] + " - " + l + " | Init Operation Sleep Time 10 Seconds" + "...................[Done]")

#Draft = driver.find_element_by_css_selector("button[class='JIM1JT-f-a JIM1JT-f-r JIM1JT-f-f']").click()
Verfiy = input("Verify inputs")
long.close()
driver.quit()
