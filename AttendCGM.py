from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from datetime import datetime
from datetime import timedelta

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
opt.add_argument("--disable-extensions")
opt.add_argument('--remote-debugging-port=9222') 
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

email = 'your-email'
password='your-password'

classJSON = [
    {
        "link":"https://meet.google.com/ynm-kksj-okv",
        "days":['Tue','Thu','Sat'],
        "time":"08:28",
    }
]

while True:
    for class0 in classJSON:
        now0 = datetime.now()
        if now0.strftime("%a") in class0['days']:
            if now0.strftime("%H:%M") == class0['time']:
                endTime = now0 + timedelta(minutes=4)
                driver = webdriver.Chrome(options=opt)
                driver.get("https://meet.google.com")
                print("google meet opened")
                driver.execute_script("document.getElementsByClassName('primary-meet-cta')[0].getElementsByTagName('a')[0].click()")
                print("google auth opened")
                driver.execute_script("document.getElementsByTagName('input')[10].value = '"+email+"'")
                driver.execute_script("document.getElementsByTagName('input')[12].click()")
                driver.execute_script("document.getElementsByTagName('input')[8].value = '"+password+"'")
                driver.execute_script("document.getElementsByTagName('input')[9].click()")
                print("verified successfully")
                driver.get(class0['link'])
                time.sleep(10)
                driver.execute_script("document.getElementsByTagName('span')[15].click()")
                while True:   
                    if datetime.now() > endTime :
                        driver.execute_script("j=document.getElementsByTagName('div');for(var i=0;i<j.length;i++){if (j[i].attributes['aria-label']!=undefined){if(j[i].attributes['aria-label'].nodeValue == 'Leave call'){j[i].click();}}}")
                        driver.close()
                        break
                    time.sleep(10)
    time.sleep(30)