from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
import time
lista = []
driver = webdriver.Firefox(executable_path='/Users/pantelis/Downloads/geckodriver.exe')
driver.get('https://play.typeracer.com/')
time.sleep(1.6)
driver.find_element_by_class_name('qc-cmp-button').click()
time.sleep(1.2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a').click()
time.sleep(3)
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res, 'html.parser')
texts = soup.find_all('span')
for i in texts:
    if('' == i.text)or('('in i.text)or('Auto-updating' in i.text):
        pass
    else:
        lista.append(i.text)
while (driver.find_element_by_class_name('txtInput').is_enabled()==False):
    time.sleep(0.3)
while len(lista)!=0:
    n = lista.pop(0)
    if(len(n)>=5):
        frash = n.split()
        for i in frash:
            print(" pano "+i)
            driver.find_element_by_class_name('txtInput').send_keys(" "+i)
            time.sleep(0.7)
    elif(n.isdigit())or(n[0].isdigit())or(n[0]==':'):
        pass
    else:        
        print(n)
        driver.find_element_by_class_name('txtInput').send_keys(n)
        time.sleep(0.1)
        
driver.quit()