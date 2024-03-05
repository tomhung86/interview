from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json





driver = webdriver.Chrome()

actions = ActionChains(driver)

driver.get("https://24h.pchome.com.tw/")
time.sleep(3)
with open('pchome.json', 'r') as f:
    data = json.loads(f.read())
for c in data:
    #print(c)
    driver.add_cookie(c)
time.sleep(2)    
driver.refresh()
input("登入以繼續")

while True:
    driver.get("https://24h.pchome.com.tw/prod/DGAD0N-A900BSZ0V")
    #driver.refresh()
    try:
        buy = WebDriverWait(driver, 0.7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-blockCombine.c-blockCombine--addToCart > div > div.c-addToCartBtn > div:nth-child(3) > button > span')))
                                                              
#加購商品
        
        dis = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProdBriefing"]/div/div/div/div[2]/div[5]/ul/li/div/div[3]/button/span'))).click()         
        time.sleep(0.3)
        dis1 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div > label:nth-child(2) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click()                                                               
        dis2 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div > label:nth-child(3) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click() 
        dis3 = WebDriverWait(driver, 3).until(
           EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__foot > ul > li > button > span '))).click()
        '''
        dis = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProdBriefing"]/div/div/div/div[2]/div[5]/ul/li[2]/div/div[3]/button/span/span'))).click()         
        time.sleep(0.3)
        dis1 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div:nth-child(2) > label:nth-child(2) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click()                                                               
        dis2 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div:nth-child(2) > label:nth-child(3) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click() 
        dis3 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__foot > ul > li > button > span '))).click() 
        '''
       
    
             
        if buy :
            time_start = time.time()
            buy.click()
            linepay = WebDriverWait(driver, 5).until(
                       EC.presence_of_element_located((By.LINK_TEXT, 'LINE Pay')))
            if linepay : 
                linepay.click()
                print("已加入購物車")
                break
    except:
        print("重試")
    
    driver.get("https://24h.pchome.com.tw/prod/DGAD0N-A900BSZ0V")
   # driver.get("https://24h.pchome.com.tw/prod/DGAD0N-A900FNB10")
    try:
        buy = WebDriverWait(driver, 0.7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-blockCombine.c-blockCombine--addToCart > div > div.c-addToCartBtn > div:nth-child(3) > button > span')))

#加購商品
        
        dis = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProdBriefing"]/div/div/div/div[2]/div[5]/ul/li/div/div[3]/button/span'))).click()         
        time.sleep(0.3)
        dis1 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div > label:nth-child(2) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click()                                                               
        dis2 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div > label:nth-child(3) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click() 
        dis3 = WebDriverWait(driver, 3).until(
           EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__foot > ul > li > button > span '))).click()
        '''
        dis = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProdBriefing"]/div/div/div/div[2]/div[5]/ul/li[2]/div/div[3]/button/span/span'))).click()         
        time.sleep(0.3)
        dis1 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div:nth-child(2) > label:nth-child(2) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click()                                                               
        dis2 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div:nth-child(2) > label:nth-child(3) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click() 
        dis3 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__foot > ul > li > button > span '))).click() 
        '''
    
    
             
        if buy :
            buy.click()
            time_start = time.time()
            linepay = WebDriverWait(driver, 5).until(
                       EC.presence_of_element_located((By.LINK_TEXT, 'LINE Pay')))
            if linepay : 
                linepay.click()
                print("已加入購物車")
                break
    except:
        print("重試")
    
   # driver.get("https://24h.pchome.com.tw/prod/DGADJN-A900GG2AJ")
    driver.get("https://24h.pchome.com.tw/prod/DGAD0N-A900BSZ0V")
    try:
        buy = WebDriverWait(driver, 0.7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-blockCombine.c-blockCombine--addToCart > div > div.c-addToCartBtn > div:nth-child(3) > button > span')))

#加購商品
        
        dis = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProdBriefing"]/div/div/div/div[2]/div[5]/ul/li/div/div[3]/button/span'))).click()         
        time.sleep(0.3)
        dis1 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div > label:nth-child(2) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click()                                                               
        dis2 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div > label:nth-child(3) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click() 
        dis3 = WebDriverWait(driver, 3).until(
           EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__foot > ul > li > button > span '))).click()
        '''
        dis = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProdBriefing"]/div/div/div/div[2]/div[5]/ul/li[2]/div/div[3]/button/span/span'))).click()         
        time.sleep(0.3)
        dis1 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div:nth-child(2) > label:nth-child(2) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click()                                                               
        dis2 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__body > div > div:nth-child(2) > label:nth-child(3) > div.c-prodInfoV2.is-row.c-prodInfoV2--giftAway'))).click() 
        dis3 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ProdBriefing > div > div > div > div.c-boxGrid__item.c-boxGrid__item--prodBriefingArea > div.c-popUp.is-visible.gtmClickV2.c-popUp--sheet > div > div > div.c-popUp__foot > ul > li > button > span '))).click() 
        '''                                          
    
    
    
             
        if buy :
            buy.click()
            time_start = time.time()
            linepay = WebDriverWait(driver, 5).until(
                       EC.presence_of_element_located((By.LINK_TEXT, 'LINE Pay')))
            if linepay : 
                linepay.click()
                print("已加入購物車")
                break
    except:
        print("重試")
        
while True:              
    try:
        Send = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, '確定送出')))
        if Send :
#            check = WebDriverWait(driver, 3).until(
#                EC.presence_of_element_located((By.XPATH, '//*[@id="normal_chk"]/label'))).click()
            time.sleep(1)
            print("送出")
            Send.click()  
            time_end = time.time()
            time_c= time_end - time_start   #執行所花時間
            print('time cost', time_c, 's')      
            break
    except:
        print("重試")
        
url = 'https://notify-api.line.me/api/notify'
token = ''
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
data = {
    'message':'Pchome下單成功！請前往結帳'     # 設定要發送的訊息
}
data = requests.post(url, headers=headers, data=data)
data = requests.post(url, headers=headers, data=data)
data = requests.post(url, headers=headers, data=data)

