# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 04:37:21 2024

@author: tomhu
"""

import json
import requests
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
m = 0
goodsCode = ["10669315"]
account = ""
password = ""


driver = webdriver.Chrome()
driver.get("https://m.momoshop.com.tw/mymomo/login.momo")
loginAcc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="memId"]'))
    )
loginPWD = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="passwd"]'))
)
#輸入帳號
loginAcc.clear()
loginAcc.send_keys(account)        
loginPWD.send_keys(password)
entry = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > dl.btns > dd.loginBtn > a'))
)
entry.click()
time.sleep(1)
input(" ")
cookie = driver.get_cookies()
cookies = '; '.join(['{}={}'.format(item['name'], item['value']) for item in cookie])
head = {
        "Cookie":cookies,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

driver.close()

session = requests.Session()


url = "https://cart.momoshop.com.tw/api/shoppingcart/modify/addGoods"
goodsdata ={"host":"WEB","data":{"goShopCartYn":"1","goods":[{"goodsCode":goodsCode[0],"goodsdtCode":"001","goodsCount":"1","work":"first","recoverYn":"0","addtionalGoods":[],"setGoods":[],"nsGift":[],"applimitBuyYn":"0","applimitBuyfsCode":"","cn":"","defDely":"","limitBuy4MemberYn":"0","limitBuyQty":"0","negativeProfit":"0","promoNo":"","savegetAmt":"","canUseBuy1Get1FreeYn":"0","largeMachineMounting":"0","largeMachineMountingPromoNo":""}],"webCategoryCode":"","srcType":"00","cycleTimes":"2","cycleYn":"0","oc":True,"reduceQty":True,"outPlanDate":"","webArea":"","webCid":"","webCtype":"","webOid":"","whCode":"","postalCode":"","inputAddress":"","receiverSeq":"","needInsurance":False}}
#goodsdata = {"host":"WEB","data":{"goShopCartYn":"1","goods":[{"goodsCode":goodsCode,"goodsdtCode":"001","goodsCount":"1","work":"shopcart","recoverYn":"0","addtionalGoods":[],"setGoods":[],"nsGift":[],"applimitBuyYn":"0","applimitBuyfsCode":"","cn":"","defDely":"","limitBuy4MemberYn":"0","limitBuyQty":"0","negativeProfit":"0","promoNo":"","savegetAmt":"","canUseBuy1Get1FreeYn":"0","largeMachineMounting":"0","largeMachineMountingPromoNo":""}],"webCategoryCode":"","srcType":"00","cycleTimes":"2","cycleYn":"0","oc":True,"reduceQty":True,"outPlanDate":"","webArea":"","webCid":"","webCtype":"","webOid":"","whCode":"","postalCode":"","inputAddress":"","receiverSeq":"","needInsurance":False}}

while True:
    r = session.post(url,headers=head,json=goodsdata)
    print("")
    print(f"正在將{goodsCode[0]}加入購物車")
    getdata = json.loads(r.content)
    print(getdata) 
    if getdata['resultCode'] == '1':
        break
    elif getdata['resultCode'] == 'SCS010':
        print("配送方式錯誤，請再選擇一次 (SCS010)")
        goodsdata = {"host":"WEB","data":{"goShopCartYn":"1","goods":[{"goodsCode":goodsCode[0],"goodsdtCode":"001","goodsCount":"1","work":"shopcart","recoverYn":"0","addtionalGoods":[],"setGoods":[],"nsGift":[],"applimitBuyYn":"0","applimitBuyfsCode":"","cn":"","defDely":"","limitBuy4MemberYn":"0","limitBuyQty":"0","negativeProfit":"0","promoNo":"","savegetAmt":"","canUseBuy1Get1FreeYn":"0","largeMachineMounting":"0","largeMachineMountingPromoNo":""}],"webCategoryCode":"","srcType":"00","cycleTimes":"2","cycleYn":"0","oc":True,"reduceQty":True,"outPlanDate":"","webArea":"","webCid":"","webCtype":"","webOid":"","whCode":"","postalCode":"","inputAddress":"","receiverSeq":"","needInsurance":False}}
    elif getdata['resultCode'] == 'SCS113':
        m = m+1
        print("商品剩餘數量不足，置入購物車失敗，請重整網頁再試一次 (SCS113)"+str(m)) 
        goodsCode.append(goodsCode.pop(0))
        goodsdata ={"host":"WEB","data":{"goShopCartYn":"1","goods":[{"goodsCode":goodsCode[0],"goodsdtCode":"001","goodsCount":"1","work":"first","recoverYn":"0","addtionalGoods":[],"setGoods":[],"nsGift":[],"applimitBuyYn":"0","applimitBuyfsCode":"","cn":"","defDely":"","limitBuy4MemberYn":"0","limitBuyQty":"0","negativeProfit":"0","promoNo":"","savegetAmt":"","canUseBuy1Get1FreeYn":"0","largeMachineMounting":"0","largeMachineMountingPromoNo":""}],"webCategoryCode":"","srcType":"00","cycleTimes":"2","cycleYn":"0","oc":True,"reduceQty":True,"outPlanDate":"","webArea":"","webCid":"","webCtype":"","webOid":"","whCode":"","postalCode":"","inputAddress":"","receiverSeq":"","needInsurance":False}}
        rs = random.uniform(0.6, 1)
        time.sleep(rs)
    elif getdata['resultCode'] == 'SCS101':
        m = m+1
        print("商品尚未開賣 (SCS101)"+str(m)) 
        goodsCode.append(goodsCode.pop(0))
        goodsdata ={"host":"WEB","data":{"goShopCartYn":"1","goods":[{"goodsCode":goodsCode[0],"goodsdtCode":"001","goodsCount":"1","work":"first","recoverYn":"0","addtionalGoods":[],"setGoods":[],"nsGift":[],"applimitBuyYn":"0","applimitBuyfsCode":"","cn":"","defDely":"","limitBuy4MemberYn":"0","limitBuyQty":"0","negativeProfit":"0","promoNo":"","savegetAmt":"","canUseBuy1Get1FreeYn":"0","largeMachineMounting":"0","largeMachineMountingPromoNo":""}],"webCategoryCode":"","srcType":"00","cycleTimes":"2","cycleYn":"0","oc":True,"reduceQty":True,"outPlanDate":"","webArea":"","webCid":"","webCtype":"","webOid":"","whCode":"","postalCode":"","inputAddress":"","receiverSeq":"","needInsurance":False}}
        rs = random.uniform(0.6, 1)
        time.sleep(rs)
    elif getdata['resultCode'] == 'SCS076':
        path = 'C:\chrome_tixcraft\webdriver\chromedriver.exe'
        driver = webdriver.Chrome(path)
        driver.get("https://m.momoshop.com.tw/mymomo/login.momo")
        loginAcc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="memId"]'))
            )
        loginPWD = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="passwd"]'))
        )
        #輸入帳號
        loginAcc.clear()
        loginAcc.send_keys(account)        
        loginPWD.send_keys(password)
        entry = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > dl.btns > dd.loginBtn > a'))
        )
        entry.click()
        time.sleep(1)
        cookie = driver.get_cookies()
        cookies = '; '.join(['{}={}'.format(item['name'], item['value']) for item in cookie])
        head = {
                "Cookie":cookies,
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
                }
        driver.close()
    else:
        rs = random.uniform(0.6, 1)
        time.sleep(rs)
        
        
    


##

#url = "https://cart.momoshop.com.tw/api/shoppingcart/query/getEachCartPICount"
#r = session.post(url,headers=head,json={"host":"WEB"})

url = "https://cart.momoshop.com.tw/api/shoppingcart/query/cartPageData"
cart_data ={"data":{"cartName":"newNormal","productStatus":[],"cartFlag":"2"},"host":"WEB"}
s = session.post(url,headers=head,json=cart_data)
getdata_cart_data = json.loads(s.content)
print("")
print(f"{getdata_cart_data['rtnData']['shopCart']['tmGoods'][next(iter(getdata_cart_data['rtnData']['shopCart']['tmGoods']))]['goodsName']} 成功加入購物車!")


#url = "https://cart.momoshop.com.tw/api/shoppingcart/trackandhistory/checkWishItem"
#r = session.post(url,headers=head,json={"host":"WEB","data":{"goodsCodes":[goodsCode]}})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/trackandhistory/getWishItemCount"
#r = session.post(url,headers=head,json={"host":"WEB"})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/trackandhistory/getRecentlyPurchasedCount"
#r = session.post(url,headers=head,json={"host":"WEB"})

##

#url = "https://cart.momoshop.com.tw/api/shoppingcart/query/selectOpenIdByCondition"
#r = session.post(url,headers=head,json={})

url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/getPayPageData"
pay_data ={"data":{"moreData":"true","cartName":"newNormal"},"host":"WEB"}
t = session.post(url,headers=head,json=pay_data)
getdata_pay_data = json.loads(t.content)


#url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/getCityList"
#r = session.post(url,headers=head,json={"data":{"cartName":"newNormal"},"host":"WEB"})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/getOrDelRecordCreditCard"
#r = session.post(url,headers=head,json={"data":{"actionType":"0"},"host":"WEB"})

#url = "https://cart.momoshop.com.tw/api/temporary/getECMStaticFileHTML"
#r = session.post(url,headers=head,json={"host":"WEB","filePath":"/10/006/00/000/bt_A_019_01.html"})

#url = "https://cart.momoshop.com.tw/api/temporary/getECMStaticFileHTML"
#r = session.post(url,headers=head,json={"host":"WEB","filePath":"/10/006/00/000/bt_A_011_01.html"})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/getDistrictAndDely"
#r = session.post(url,headers=head,json={"data":{"cartName":"newNormal","cityPostGB":"410","type":"all"},"host":"WEB"})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/getRecentReceiverInfo"
#r = session.post(url,headers=head,json={"data":{"cartName":"newNormal","pageNo":1,"pageSize":10},"host":"WEB"})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/getRecentReceiverInfo"
#r = session.post(url,headers=head,json={"data":{"cartName":"newNormal","pageNo":1,"pageSize":10},"host":"WEB"})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/getPeriodAndPrice"
#r = session.post(url,headers=head,json={"data":{"cardNo":"430451******","cardNoKey":"cardNo_004_0","cartName":"newNormal"},"host":"WEB"})

#url = "https://cart.momoshop.com.tw/api/shoppingcart/payinfo/payTrems"
#r = session.post(url,headers=head,json={"host":"WEB"})


##


url = "https://cart.momoshop.com.tw/api/shoppingcart/checkout/"
check_data = {"host":"WEB","data":{"cartName":"newNormal","dontCleanCart":True,"payment":[{"allot":1,"code":"Linepay","questAmt":getdata_cart_data['rtnData']['shopCart']['totalLastPrice']}],
                      "orderReceiver":{"custName":getdata_pay_data['rtnData']['payPageData']['receiverData']['custName'],"custDDD":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverDDD'],"custTel1":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverTel1'],"custTel2":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverTel2'],"custTel3":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverTel3'],"custHp1":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverHp1'],"custHp2":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverHp2'],"custHp3":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverHp3'],"custPost":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverAddrPost'],"custAddr":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverAddr'],"emailAddr":getdata_pay_data['rtnData']['payPageData']['receiverData']['eMail']},
                      "goodsReceiver":{"selAddress":"0","receiverSeq":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverAddrSeq'],"receiverName":getdata_pay_data['rtnData']['payPageData']['receiverData']['custName'],"receiverDDD":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverDDD'],"receiverTel1":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverTel1'],"receiverTel2":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverTel2'],"receiverTel3":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverTel3'],"receiverHp1":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverHp1'],"receiverHp2":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverHp2'],"receiverHp3":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverHp3'],"receiverPost":"X","receiverAddr":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverAddr'],"outside":"0","storeType":"","storeId":"","storeName":"","address":"","ship":"","reservedNos":"","deliveryDate":"","bearMomDelyDate":"","bearMomDelyTime":"","bearMomDelyNo":"","bearMomPostNo":"","bearMomAddr":"","receiverGifterYN":"0","receiverGifter":"","capacityType":"","capacityDay":"","capacityTime":"","chkGreenConsolidate":"","chkConsolidate":""},
                      "openIdCkboxInfo":[],"receiptReceiver":{"invoiceSeq":getdata_pay_data['rtnData']['payPageData']['receiverData']['receiverAddrSeq'],"selInvoiceAddr":"0","invoicePost":"702","invoiceAddr":"新孝路***巷**弄**號","eInvoiceType":"E2","mobileInvoice":"HK5HDHX","mobileInvoiceYN":"1","pIdNo":"","personInvoiceYN":"1","invoiceType":"E","invoiceTitle":"","invoiceUniNo":"","companyYN":"1","grantFlag":"2","invoiceEmail":getdata_pay_data['rtnData']['payPageData']['receiverData']['eMail']},"cardOwnerReceiver":{"custAsCardOwner":"1","cardOwnerName":"","cardOwnerBirthYear":"","cardOwnerBirthMonth":"","cardOwnerBirthDate":"","cardOwnerID":"","cardOwnerHP":"","cardOwnerTEL":"","cardOwnerPost":"X","cardOwnerGuName":"","cardOwnerPostName":"","cardOwnerAddr":""},"cardInfo":{},"_u_email":"to*******@hotmail.com","mediaGb":"07","rutenCode":"","osm":"","useQuintupleVoucher":"0","asiaYoTraveler":{},
                      "cartCamTime":getdata_pay_data['rtnData']['payPageData']['cartCamTime']}}
u = session.post(url,headers=head,json=check_data)
getdata_check = json.loads(u.content)
print("")
#print(getdata_check)

try:
    if getdata_check['rtnData']['orderEndMessageArea']:
        print(getdata_check['rtnData']['orderEndMessageArea'])
    if getdata_check['rtnData']['paymentUrl']:
        print(f"linepay付款網址:{getdata_check['rtnData']['paymentUrl']}")
        
except:
    pass

url = "https://cart.momoshop.com.tw/api/temporary/getECMStaticFileHTML"
r = session.post(url,headers=head,json={"host":"WEB","filePath":"/10/006/00/000/bt_A_011_01.html"})

session.close()

url = 'https://notify-api.line.me/api/notify'
token = ''
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
data = {
    'message':'momo下單成功！請前往結帳'     # 設定要發送的訊息
}

for i in range(10):
    data_send = requests.post(url, headers=headers, data=data)
    time.sleep(1)
