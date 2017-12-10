from selenium import webdriver
import os
from googletrans import Translator
from time import sleep

service_urls=['translate.google.com','translate.google.co.kr']    
translator = Translator(service_urls)

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
driver = webdriver.Firefox(executable_path=r'C:\Users\VanGiex\Documents\Runtimes\geckodriver-v0.19.1-win64\geckodriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("https://play.google.com/apps/publish/?account=8885818345072357724#AppListPlace")
input("Login with User & Pass(Enter When Done)")
driver.find_element_by_id("gwt-uid-217").click()
input("Project Name (Press Enter when Done!)")
driver.get("https://play.google.com/apps/publish/?account=8885818345072357724#MarketListingPlace:p=com.players.touch_girl")
input("Authroize Project (Enter)")
select = driver.find_element_by_css_selector("button[class='HCXDKGD-f-a HCXDKGD-f-p HCXDKGD-f-n HCXDKGD-f-b HCXDKGD-f-c HCXDKGD-f-s']")
for l in PLAYSTORE:
        os.system('cls')
        print("\nInit Operation\nTime Wait 10 Second\nSelect Operation -> " + LANGUAGES[l] + " - " + l)
        sleep(10)
        driver.execute_script("arguments[0].setAttribute('data-lang-code','" + PLAYSTORE[l] + "')", select)
        driver.execute_script("arguments[0].setAttribute('aria-pressed','false')", select)
        sleep(10)
        select.click()
        tin = translator.translate("Touch on Girl: Girl Cloth scanner", dest=l).text
        if len(tin) > 50 : print("\n\t\t\tTake Precaucation Length Is More then Precribe !!")
        driver.find_element_by_css_selector("input[class='gwt-TextBox HCXDKGD-an-d']").clear()
        driver.find_element_by_css_selector("input[class='gwt-TextBox HCXDKGD-an-d']").send_keys(tin)
        tin = translator.translate("Touch screen on your mobile to sexy photos and fell the vibration.", dest=l).text
        if len(tin) > 80 : print("\n\t\t\tTake Precaucation Length Is More then Precribe !!")
        driver.find_element_by_css_selector("textarea[class='gwt-TextArea HCXDKGD-vi-d HCXDKGD-an-d']").clear()
        driver.find_element_by_css_selector("textarea[class='gwt-TextArea HCXDKGD-vi-d HCXDKGD-an-d']").send_keys(tin)
        fin = translator.translate(open("test.txt","r").read(), dest=l).text
        if len(tin) > 4000 : print("\n\t\t\tTake Precaucation Length Is More then Precribe !!")
        driver.find_element_by_css_selector("textarea[class='gwt-TextArea HCXDKGD-an-d']").clear()
        driver.find_element_by_css_selector("textarea[class='gwt-TextArea HCXDKGD-an-d']").send_keys(fin)
        print("\n\t\t\tDone " + LANGUAGES[l] + " - " + l)
        input("Enter To Continue ......")
     
input("Verify inputs")
driver.quit()
