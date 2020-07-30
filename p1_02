#https://engkimbs.tistory.com/896
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.headless = True
#driverPath = 'D:\DogFoot\IEDriverServer_Win32_3.150.1\IEDriverServer.exe'
driverPath = 'D:\DogFoot\chromedriver.exe'
#browser = webdriver.Ie(driverPath)
browser = webdriver.Chrome(executable_path=driverPath, options=options)
browser.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

time.sleep(3)
tag_names=browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
for tag in tag_names:
    print(tag.text.split("\n"))
