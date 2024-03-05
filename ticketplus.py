# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:08:25 2024

@author: tomhu
"""

import cairosvg
import ddddocr
import json
import requests
from PIL import Image
import time
from datetime import datetime
import random
import hashlib
import re



#第二步驟輸入購買資料及場次
countryCode= "1"
account    = ""   #在前面""內輸入帳號
password   = ""   #在前面""內輸入密碼
site       = "https://ticketplus.com.tw/order/d5de85de3bfbbac130b5d4a13ca874a5/650df280002032e23add5155a57e6f07"   #在前面""內輸入搶票選區網址(網址包含order)
count      =  1   #在前面輸入張數(注意每場限購幾張，越少張成功率越高)

#選區模式
area_option =  0   # 0 = 全區刷 ， 1 = 選價格刷， 2 = 選區域刷。  如果選擇刷全區下面兩項不用設定。

#選區模式選1需要設定pricefind
pricefind  = [2900]   #輸入要刷的價格區。            例如要5000,2000的，要寫成[5000,2000]，不設定也要留[]。

#選區模式選2需要設定area_pick
area_pick = ["橙2A-1區"]    #在[]內用'',''分隔要刷的區域。 例如要1F搖滾A區,'1F搖滾B區，要寫成['1F搖滾A區','1F搖滾B區']，不設定也要留[]。

#是否要連續座位
consecutiveSeats = True   #True/False

#line通知，不想用就不用設定
linenotify = ""   #輸入LineNotify的密鑰。

#如果有題目問答
serialNumber = ""






#個人資訊
md5_hash = hashlib.md5()
md5_hash.update(password.encode('utf-8'))
password_value = md5_hash.hexdigest()
login_data = {"mobile":account,"countryCode":countryCode,"password":password_value}
head = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
now = datetime.today().strftime("%Y-%m-%d %H:%M")
timestamp =  (int)(datetime.strptime(now, "%Y-%m-%d %H:%M").timestamp() * 1000)
login_url = f"https://apis.ticketplus.com.tw/user/api/v1/login?_={timestamp}"
w = requests.post(login_url,headers=head,json=login_data)
logdata = json.loads(w.content)

keys = logdata['userInfo']['id']
token = logdata['userInfo']['access_token']
Authorization = "Bearer "+token
refresh_Authorization = "Bearer "+ logdata['userInfo']['refresh_token']


#獲得/設定區域資訊
match1 = re.search(r'/order/([^/]+)/([^/]+)', site)
eventId = match1.group(1)
sessionId = match1.group(2)

ticketAreaId = []
productId = []
price = []

head = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
a = requests.get(f"https://apis.ticketplus.com.tw/config/api/v1/getS3?path=event/{eventId}/products.json",headers=head)
products_data = json.loads(a.content)
try:
    for x in products_data['products']:
       if x["sessionId"] == sessionId:
            ticketAreaId.append(x['ticketAreaId'])
            productId.append(x['productId'])
            if x['price'] not in price:
                price.append(x['price'])
    sub = f"ticketAreaId={'%2C'.join(ticketAreaId)}&productId={'%2C'.join(productId)}"
except:
    for x in products_data['products']:
        if x["sessionId"] == sessionId:
            productId.append(x['productId'])
            if x['price'] not in price:
                price.append(x['price'])
    sub = f"productId={'%2C'.join(productId)}"



w = requests.get(f"https://apis.ticketplus.com.tw/config/api/v1/get?{sub}",headers=head)
data = json.loads(w.content)

if area_option == 0:
    pricefind = price
    area = []
    print("抓取到以下區域")

    try:
      for c in pricefind:
          for i in data['result']['product']:
            if i['price'] == c:
                  for b in data['result']['ticketArea']:
                      if b['id'] == i['ticketAreaId']:
                          print(f"{i['id']}={b['ticketAreaName']}")
                          area.append(f"{i['id']}")
          print("")

    except:
      for c in pricefind:
        for i in data['result']['product']:
          if i['price'] == c:
            for w in products_data['products']:
              if i['id'] == w['productId']:
                print(f"{i['id']}={w['name']}")
                area.append(f"{i['id']}")
        print("")

elif area_option == 1:
    area = []
    print("抓取到以下區域")

    try:
      for c in pricefind:
          for i in data['result']['product']:
            if i['price'] == c:
                  for b in data['result']['ticketArea']:
                      if b['id'] == i['ticketAreaId']:
                          print(f"{i['id']}={b['ticketAreaName']}")
                          area.append(f"{i['id']}")
          print("")

    except:
      for c in pricefind:
        for i in data['result']['product']:
          if i['price'] == c:
            for w in products_data['products']:
              if i['id'] == w['productId']:
                print(f"{i['id']}={w['name']}")
                area.append(f"{i['id']}")
        print("")

elif area_option == 2:
    area = []
    print("抓取到以下區域")
    try:
      for c in area_pick:
        for i in data['result']['ticketArea']:
          if i['ticketAreaName'] == c:
            for b in data['result']['product']:
              if i['id'] == b['ticketAreaId']:
                print(f"{b['id']}={c}")
                area.append(f"{b['id']}")

    except:
      for c in area_pick:
        for i in products_data['products']:
          if i['name'] == c:
            print(f"{i['productId']}={c}")
            area.append(f"{i['productId']}")
    print("")


url = f'https://apis.ticketplus.com.tw/config/api/v1/get?productId={area[0]}'
r = requests.get(url)
getdata = json.loads(r.content)
Section = getdata['result']['product'][0]['sessionId']


#獲取驗證碼
time_start = time.time()
res_temp = ""
res = "1234"

captch_data = {"sessionId":Section}

head = {
        "Authorization":Authorization,
#        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
#        'User-Agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
        }

now = datetime.today().strftime("%Y-%m-%d %H:%M")
timestamp =  (int)(datetime.strptime(now, "%Y-%m-%d %H:%M").timestamp() * 1000)
captch_url = f"https://apis.ticketplus.com.tw/captcha/api/v1/generate?_={timestamp}"
w = requests.post(captch_url,headers=head,json=captch_data)
capdata = json.loads(w.content)
svg = capdata['data']  #獲得驗證碼data
cairosvg.svg2png(bytestring=svg, write_to='output.png')

image = Image.open('output.png')
new_image = Image.new('RGBA', image.size, (255, 255, 255, 255))
new_image.paste(image, (0, 0), image)
new_image.save('test.png')
new_image.close()
image.close()

ocr = ddddocr.DdddOcr(beta=True)
with open('test.png', 'rb') as f:
    image = f.read()
capt = ocr.classification(image)
print(capt)


#購票流程
while True :
        try:
            now = datetime.today().strftime("%Y-%m-%d %H:%M")
            timestamp =  (int)(datetime.strptime(now, "%Y-%m-%d %H:%M").timestamp() * 1000)
            url = f"https://apis.ticketplus.com.tw/ticket/api/v1/reserve?_={timestamp}"
            goodseatdata={"products":[{"productId":area[0],"count":count}],"captcha":{"key":keys,"ans":capt},"reserveSeats":True,"consecutiveSeats":consecutiveSeats,"finalizedSeats":True}
            if serialNumber :
                goodseatdata={"products":[{"productId":area[0],"count":count}],"captcha":{"key":keys,"ans":capt},"reserveSeats":True,"consecutiveSeats":consecutiveSeats,"finalizedSeats":True,"serialNumber":serialNumber}
            r = requests.post(url,headers=head,json=goodseatdata)
            getdata = json.loads(r.content)
            print(getdata)
            if getdata['errCode'] == '00':
                time_end = time.time()
                time_c= time_end - time_start   #執行所花時間
                print('time cost', time_c, 's')
                break
            elif getdata['errCode'] == '137':
                #time.sleep(0.7)
                continue
            elif getdata['errCode'] == '121':
                area.append(area.pop(0))
                rs = random.uniform(0.3, 0.4)
                time.sleep(rs)
                continue
            elif getdata['errCode'] == '115':
                area.append(area.pop(0))
                rs = random.uniform(0.3, 0.7)
                time.sleep(rs)
                continue
            elif getdata['errCode'] == '103':
                now = datetime.today().strftime("%Y-%m-%d %H:%M")
                timestamp =  (int)(datetime.strptime(now, "%Y-%m-%d %H:%M").timestamp() * 1000)
                url = f"https://apis.ticketplus.com.tw/user/api/v1/refreshToken?_={timestamp}"
                head = {
                        "Authorization":refresh_Authorization,
                #        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
                #        'User-Agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
                        }
                r = requests.post(url,headers=head,json={})
                refresh = json.loads(r.content)
                newtoken = refresh['userInfo']['access_token']
                newAuthorization = "Bearer "+newtoken
                head = {
                        "Authorization":newAuthorization,
                #        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
                #        'User-Agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
                        }
            else :
                try:
                    while True:
                        if res != res_temp:
                            now = datetime.today().strftime("%Y-%m-%d %H:%M")
                            timestamp =  (int)(datetime.strptime(now, "%Y-%m-%d %H:%M").timestamp() * 1000)
                            captch_url = f"https://apis.ticketplus.com.tw/captcha/api/v1/generate?_={timestamp}"
                            res_temp = res
                            w = requests.post(captch_url,headers=head,json=captch_data)
                            capdata = json.loads(w.content)
                            svg = capdata['data']  #獲得驗證碼data
                            cairosvg.svg2png(bytestring=svg, write_to='output.png')

                            image = Image.open('output.png')
                            new_image = Image.new('RGBA', image.size, (255, 255, 255, 255))
                            new_image.paste(image, (0, 0), image)
                            new_image.save('test.png')
                            new_image.close()
                            image.close()

                            ocr = ddddocr.DdddOcr(beta=True)
                            with open('test.png', 'rb') as f:
                                image = f.read()
                            res = ocr.classification(image)
                            print(res)
                        else:
                            capt = res
                            res_temp = ""
                            break
                except:
                    continue
        except:
            continue
        

#完成顯示
print("請時間內到下面網址登入結帳")
print(site[:26]+"confirm"+site[31:])
print("")
print('結帳截止時間:'+getdata['products'][0]['expiryTimestamp'])
print('座位')
try:
  for x in getdata['products'][0]['seats']:
    print(x['ticketAreaName']+x['row']+'排'+x['column']+'號')
except:
  print(getdata['products'][0]['productId'])

print("")
print('結帳總金額:'+str(getdata['total'])+' / '+str(getdata['products'][0]['count'])+'張')

#linenotify通知
if linenotify:
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + linenotify    # 設定權杖
    }
    data = {
        'message':f'''

下單成功！請前往結帳
{site[:26]}confirm{site[31:]}

結帳截止時間:
{getdata['products'][0]['expiryTimestamp']}

結帳總金額:
{str(getdata['total'])} / {str(getdata['products'][0]['count'])}張

    '''
    }
    for i in range(10):
        data_send = requests.post(url, headers=headers, data=data)
        time.sleep(1)
else:
    print("沒設定line通知")



