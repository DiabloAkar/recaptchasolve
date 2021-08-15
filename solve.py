from selenium import webdriver
import requests, time
import threading
from pip._vendor.colorama import Fore
import subprocess
'import layn'

subprocess.call('start https://discord.gg/akargang', shell=True)
subprocess.call('start https://github.com/DiabloAkar', shell=True)

bammer = '''

████████▄   ▄█     ▄████████ ▀█████████▄   ▄█        ▄██████▄  
███   ▀███ ███    ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███  ▄███▄▄▄██▀  ███       ███    ███ 
███    ███ ███▌ ▀███████████ ▀▀███▀▀▀██▄  ███       ███    ███ 
███    ███ ███    ███    ███   ███    ██▄ ███       ███    ███ 
███   ▄███ ███    ███    ███   ███    ███ ███▌    ▄ ███    ███ 
████████▀  █▀     ███    █▀  ▄█████████▀  █████▄▄██  ▀██████▀  
                                          ▀                    

'''
print(Fore.YELLOW+bammer)
print(Fore.YELLOW)
print(Fore.YELLOW+"Instagram = diabloakar")
print(Fore.YELLOW+"Github = https://github.com/DiabloAkar")
print(Fore.YELLOW+"Sistem Hazırlanıyor")
time.sleep(1)
print('%1 [=                                       ]')
time.sleep(1)
print('%3 [===                                     ]')
time.sleep(1)
print('%10 [======                                  ]')
time.sleep(1)
print('%20 [========                                ]')
time.sleep(1)
print('%30 [=================                       ]')
time.sleep(1)
print('%40 [======================                  ]')
time.sleep(1)
print('%60 [=============================           ]')
time.sleep(1)
print('%70 [================================        ]')
time.sleep(1)
print('%90 [======================================  ]')
time.sleep(1)
print('%100 [========================================]')
time.sleep(1)

API_KEY = '' #Buraya api key koyunuz
data_sitekey = '6Le-mvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx?mJ-'
page_url = 'https://www.google.com/recaptcha/api2/demo'

def Solver():
    driver = webdriver.Chrome()
    driver.get(page_url)
    u1 = f"https://2captcha.com/rex.php?key={API_KEY}&method=usercaptcha&googleley={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
    r1 = requests.get(u1)
    print(r1.json())
    rid = r1.json().get("request")
    u2 = f"https://2captcha.com/rex.php?key={API_KEY}&action?get&id={int(rid)}&json=1"
    time.sleep(5)
    while True:
        r2 = requests.get(u2)
        print(r2.json())
        if r2.json().get("status") == 1:
            form_token = r2.json().get("request")
            break
        time.sleep(5)
    write_token_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_token}";'
    sbumit_js = 'document.getElementById("recaptcha-demo-form").submit();'
    driver.execute_script(write_token_js)
    time.sleep(3)
    driver.execute_script(sbumit_js)
    time.sleep(10)


if __name__== '__main__':
    Solver()