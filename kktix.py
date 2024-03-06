# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:55:20 2024

@author: tomhu
"""


import json
import requests
import time
import webbrowser
import capsolver
import pyperclip

cookies = "" 
session = "hteghz"
count = "2"
ticket_area = ['694630']
#count_limilt = "1"



url = f"https://kktix.com/g/events/{session}/register_info"        
head = {"Cookie":cookies,
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
w = requests.get(url,headers=head)
getdata = json.loads(w.content)
currency = getdata['order']['price_currency']
search_token = w.headers['Set-Cookie']
authenticity_token = search_token[11:-16]


while True:
    try:
        '''
        url = f"https://kktix.com/g/events/{session}/register_info"        
        head = {"Cookie":cookies,
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
        w = requests.get(url,headers=head)
        getdata = json.loads(w.content)
        currency = getdata['order']['price_currency']
        search_token = w.headers['Set-Cookie']
        authenticity_token = search_token[11:-16]
        '''
        
        url = f"https://queue.kktix.com/queue/{session}?authenticity_token={authenticity_token}"        
        data = '{"tickets":[{"id":'+ticket_area[0]+',"quantity":'+count+',"invitationCodes":[],"member_code":"","use_qualification_id":null}],"currency":"'+currency+'","recaptcha":{},"agreeTerm":true}'
        #data = '{"tickets":[{"id":692701,"quantity":2,"invitationCodes":[],"member_code":"","use_qualification_id":null}],"currency":"TWD","recaptcha":{},"custom_captcha":"糟糕","agreeTerm":true}'
        head = {"Cookie":cookies,
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
        x = requests.post(url,headers=head,data=data.encode('utf-8'))
        getToken = json.loads(x.content)
        print(getToken)
        try :
            if getToken['result'] == 'TICKET_SOLD_OUT':
                continue     
            elif getToken['result'] == 'CAPTCHA_WRONG_ANSWER':
                capsolver.api_key = ""
                '''
                solution = capsolver.solve({
                            "type": "ReCaptchaV3EnterpriseTaskProxyless",
                            "websiteURL": "https://kktix.com",
                            "websiteKey": "6LcU8fglAAAAAOPLzR2f34XdCE2Ab257o5NqS7JC",
                            "minScore": 0.7,
                            "apiDomain": "www.recaptcha.net",
                            "pageAction": "enqueue"
                              })
                '''
                solution = capsolver.solve({
                            "type": "ReCaptchaV2TaskProxyless",
                            "websiteURL": "https://kktix.com",
                            "websiteKey": "6LfAmDsmAAAAANOYx4ajYcIuWB7jZiO4NpKoWiA2",
                            "apiDomain": "www.recaptcha.net",
                            "isInvisible": True
                              })
                
                print(solution['gRecaptchaResponse'])
                data = '{"tickets":[{"id":'+ticket_area[0]+',"quantity":'+count+',"invitationCodes":[],"member_code":"","use_qualification_id":null}],"currency":"'+currency+'","recaptcha":{"responseChallenge":"'+solution['gRecaptchaResponse']+'"},"agreeTerm":true}'
                #data = '{"tickets":[{"id":'+ticket_area[0]+',"quantity":'+count+',"invitationCodes":[],"member_code":"","use_qualification_id":null}],"currency":"'+currency+'","recaptcha":{"responseChallenge":"'+solution['gRecaptchaResponse']+'"},"custom_captcha":"高雄","agreeTerm":true}'
                head = {"Cookie":cookies,
                    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
                x = requests.post(url,headers=head,data=data.encode('utf-8'))
                getToken = json.loads(x.content)
                print(getToken)
                search_cookies = x.headers['Set-Cookie']
                cookies_add = search_cookies.split('; ')[0]
                cookies = cookies+"; "+cookies_add
        except:
            pass
        
        #time.sleep(1.5)

        head = {"Cookie":cookies,
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
        url = f'https://queue.kktix.com/queue/token/{getToken["token"]}'
        webbrowser.open_new(url)
        y = requests.get(url,headers=head)
        getOrder = json.loads(y.content)
        print(getOrder)
        try: 
            if getOrder['result'] == 'not_found':
                time.sleep(3)
                y = requests.get(url,headers=head)
                getOrder = json.loads(y.content)
                print(getOrder)
                webbrowser.open_new(f'https://kktix.com/events/{session}/registrations/{getOrder["to_param"]}')
            
        
        except:
            webbrowser.open_new(f'https://kktix.com/events/{session}/registrations/{getOrder["to_param"]}')
        
        
        if getOrder["to_param"]:
            pyperclip.copy(getOrder["to_param"])
            break
    except:
        continue
    

