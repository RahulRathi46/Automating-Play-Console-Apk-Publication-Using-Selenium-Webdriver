from selenium import webdriver
from os import system
from googletrans import Translator
from time import sleep

service_urls=['translate.google.com','translate.google.co.kr']
translator = Translator(service_urls)

count = 0
with open("title.txt","r") as title,open("short.txt","r") as short:
    title = title.read()
    short = short.read()
    long = open("long.txt","r")

PLAYSTORE = {
'en':'en-IN',
'af':'af',
'am':'am',
'ar':'ar',
'hy':'hy-AN',
'az':'az-AZ',
'bn':'bn-BD',
'eu':'eu-ES',
'be':'be',
'bg':'bg',
'my':'my-MM',
'ca':'ca',
'zh-cn':'zh-HK',
'zh-cn':'zh-CN',
'zh-tw':'zh-TW',
'hr':'hr',
'cs':'cs-CZ',
'da':'da-DK',
'nl':'nl-NL',
'en':'en-AU',
'en':'en-SG',
'en': 'en-ZA',
'en': 'en-CA',
'en':'en-GB',
'en': 'en-US',
'et':'et',
'tl':'fil',
'fi':'fi-FI',
'fr':'fr-FR',
'fr': 'fr-CA',
'gl':'gl-ES',
'ka':'ka-GE',
'de':'de-DE',
'el':'el-GR',
'iw':'iw-IL',
'hi':'hi-IN',
'hu':'hu-HU',
'is':'is-IS',
'id':'id',
'it':'it-IT',
'ja':'ja-JP',
'kn':'kn-IN',
'km':'km-KH',
'ko':'ko-KR',
'ky':'ky-KG',
'lo':'lo-LA',
'la':'lv',
'lt':'lt',
'mk':'mk-MK',
'ms':'ms',
'ml':'ml-IN',
'mr':'mr-IN',
'mn':'mn-MN',
'ne':'ne-NP',
'no':'no-NO',
'fa':'fa',
'pl':'pl-PL',
'pt':'pt-BR',
'pt':'pt-PT',
'ro':'ro',
'ro':'rm',
'ru':'ru-RU',
'sr':'sr',
'si':'si-LK',
'sk':'sk',
'sl':'sl',
'es':'es-149',
'es':'es-ES',
'es':'es-US',
'sw':'sw',
'sv':'sv-SE',
'ta':'ta-IN',
'te':'te-IN',
'th':'th',
'tr':'tr-TR',
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
'zh-cn': 'chinese (simplified)',
'zh-tw': 'chinese (traditional)',
'hr': 'croatian',
'cs': 'czech',
'da': 'danish',
'nl': 'dutch',
'en': 'english',
'en': 'english',
'en': 'english',
'en': 'english',
'en': 'english',
'et': 'estonian',
'tl': 'filipino',
'fi': 'finnish',
'fr': 'french',
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
'pt': 'portuguese',
'ro': 'romanian',
'ro': 'romanian',
'ru': 'russian',
'sr': 'serbian',
'si': 'sinhala',
'sk': 'slovak',
'sl': 'slovenian',
'es': 'spanish',
'es': 'spanish',
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
URL = driver.get("https://play.google.com/apps/publish/?account=8885818345072357724")
Confirm = input("Login with User & Pass (Enter)")

New = driver.find_element_by_css_selector("button[class='JIM1JT-f-a JIM1JT-f-r']").click()
Confirm = input("Enter project name (Enter)")

New = driver.find_element_by_css_selector("button[class='JIM1JT-f-a JIM1JT-Nh-j JIM1JT-Q-c JIM1JT-k-mb']").click()
Confirm = input("Select add languages (Enter)")

language_button = driver.find_element_by_css_selector("button[class='JIM1JT-f-a JIM1JT-f-p JIM1JT-f-n JIM1JT-f-b JIM1JT-f-c JIM1JT-f-s']")

title_box = driver.find_element_by_css_selector("input[class='gwt-TextBox JIM1JT-fn-d']")
short_box = driver.find_element_by_css_selector("textarea[class='gwt-TextArea JIM1JT-Zh-d JIM1JT-fn-d']")
long_box = driver.find_element_by_css_selector("textarea[class='gwt-TextArea JIM1JT-fn-d']")

system('cls')
print("SR." + " |  " + "LANGUAGES" + " - " + "Encode" + " | Function Processing" + "................... [Status]")

for l in PLAYSTORE:
    count=count+1
    long.seek(0)
    sleep(1)
    
    update_language = driver.execute_script("arguments[0].setAttribute('data-lang-code','" + PLAYSTORE[l] + "')", language_button)
    script = driver.execute_script("arguments[0].setAttribute('aria-pressed','false')", language_button)
    sleep(5)
    language_button.click()
    
    title_box.clear()
    short_box.clear()
    long_box.clear()
    
    translate_title = translator.translate(title, dest=l).text
    translate_short = translator.translate(short, dest=l).text
    translate_long = translator.translate(long.read(), dest=l).text
    
    if l=='bg': translate_short=translate_title
    if l=='mk': translate_short=translate_title

    title_box.send_keys(translate_title[:50])
    sleep(1)
    short_box.send_keys(translate_short[:80])
    sleep(1)
    long_box.send_keys(translate_long[:4000])
    sleep(2)
    
    print(str(count) + " |  " + LANGUAGES[l] + " - " + l + " | Init Operation Sleep Time 10 Seconds" + "...................[Done]")
 
Verfiy = input("Verify inputs")
long.close()
driver.quit()
