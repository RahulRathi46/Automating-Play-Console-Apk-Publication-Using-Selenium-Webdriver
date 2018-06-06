from selenium import webdriver
from os import system
from googletrans import Translator
from time import sleep

service_urls=['translate.google.com','translate.google.co.kr']
translator = Translator(service_urls)

count = 0
with open(r"Context\title.txt","r") as title,open(r"Context\short.txt","r") as short:
    title = title.read()
    short = short.read()
    long = open(r"Context\long.txt","r")

PLAYSTORE = {
'en-IN':'en',
'af':'af',
'am':'am',
'ar':'ar',
'hy-AM':'hy',
'az-AZ':'az',
'bn-BD':'bn',
'eu-ES':'eu',
'be':'be',
'bg':'bg',
'my-MM':'my',
'ca':'ca',
'zh-HK':'zh-cn',
'zh-cn':'zh-cn',
'zh-tw':'zh-tw',
'hr':'hr',
'cs-CZ':'cs',
'da-DK':'da',
'nl-NL':'nl',
'en-AU':'en',
'en-SG':'en',
'en-ZA':'en',
'en-CA':'en',
'en-GB':'en',
'en-US':'en',
'et':'et',
'fil':'tl',
'fi-FI':'fi',
'fr-FR':'fr',
'fr-CA':'fr',
'gl-ES':'gl',
'ka-GE':'ka',
'de-DE':'de',
'el-GR':'el',
'iw-IL':'iw',
'hi-IN':'hi',
'hu-HU':'hu',
'is-IS':'is',
'id':'id',
'it-IT':'it',
'ja-JP':'ja',
'kn-IN':'kn',
'km-KH':'km',
'ko-KR':'ko',
'ky-KG':'ky',
'lo-LA':'lo',
'lv':'la',
'lt':'lt',
'mk-MK':'mk',
'ms':'ms',
'ml-IN':'ml',
'mr-IN':'mr',
'mn-MN':'mn',
'ne-NP':'ne',
'no-NO':'no',
'fa':'fa',
'pl-PL':'pl',
'pt-BR':'pt',
'pt-PT':'pt',
'ro':'ro',
'rm':'ro',
'ru-RU':'ru',
'sr':'sr',
'si-LK':'si',
'sk':'sk',
'sl':'sl',
'es-419':'es',
'es-ES':'es',
'es-US':'es',
'sw':'sw',
'sv-SE':'sv',
'ta-IN':'ta',
'te-IN':'te',
'th':'th',
'tr-TR':'tr',
'uk':'uk',
'vi':'vi',
'zu':'zu'
}

LANGUAGES = {
    'en': 'english', 
    'af': 'afrikaans', 
    'am': 'amharic', 
    'ar': 'arabic', 
    'hy': 'armenian', 
    'az': 'azerbaijani', 
    'bn': 'bengali', 
    'eu': 'basque', 
    'be': 'belarusian',
    'bg': 'bulgarian', 
    'my': 'myanmar (burmese)', 
    'ca': 'catalan',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'it': 'italian',
    'ja': 'japanese',
    'kn': 'kannada',
    'km': 'khmer',
    'ko': 'korean',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ms': 'malay',
    'ml': 'malayalam',
    'mr': 'marathi',
    'mn': 'mongolian',
    'ne': 'nepali',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'vi': 'vietnamese',
    'zu': 'zulu'
    }

# create a new Firefox session
driver = webdriver.Firefox(executable_path=r'Runtime\geckodriver.exe')
driver.implicitly_wait(30)
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
