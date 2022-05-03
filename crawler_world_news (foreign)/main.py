# region (Import Layer)
from google_trans_new import google_translator
import geometry.crawler as crawler
import requests, json, csv, uuid
import urllib.request as req
import txt_to_xlsx as ttx
import datetime
import openpyxl
import time
import bs4
import re
import ssl
# endregion

# region (News api)
API_KEY = 'a9c23f150c24416084bd859f692077c2'    
pageNum = 1
totalPageNum = 1
# endregion

#這兩個是有用NewsAPI的才會用到
#意思是搜尋從 today 到 yesterday 的新聞
today = datetime.date.today()
yesterday=today-datetime.timedelta(days=7)  #days是要從今天起往回算幾天

#只用來翻譯泰國的發布時間
google_translator=google_translator()

#翻譯整個網站
def website_translte(sl,url):
    result="https://translate.google.com/translate?hl=&sl="+sl+"&tl=zh-TW&u="+url
    return result

t= time.strftime("%Y-%m-%d", time.localtime())

# Indonesia_news()有用到
def GetDate(url,label,name):
    data=None
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    date=root.find(label,class_=name)
    return date.text

#AZURE的翻譯工具
def translator(content):
    subscription_key = "adcf5dbd2e46495181e37cb2d65ba329"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "global"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': ['zh-Hant']
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': content
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0]["translations"][0]["text"]

# 用NewsAPI
def Japan_news():
    fp1 = open("./news_txt/japan.txt", "w+",encoding="utf8") # 開啟檔案

    url = ('https://newsapi.org/v2/everything?'
        'q="新型コロナ"&'
        'from='+str(today)+'&'
        'to='+str(yesterday)+'&'
        'sortBy=publishedAt&'
        'domains=nhk.or.,asahi.com&' 
        'page=' + str(pageNum) + '&'
        'apiKey=' + API_KEY)

    aRes = requests.get(url)
    newsDict = json.loads(aRes.text)
   
    print('totalResults: ' + str(newsDict['totalResults']))
    global totalPageNum
    totalPageNum = int(newsDict['totalResults']/20) + 1
    # print('Retrieving Page ' + str(pageNum) + '/' + str(totalPageNum))
    for article in newsDict['articles']:
        print(translator(article['title']))
        fp1.write(translator(article['title']))
        fp1.write('\n')       

        
        print(translator(article['description']).replace("\n", ""))
        fp1.write(translator(article['description']).replace("\n", ""))
        fp1.write('\n')   

        print((article['publishedAt'])[:10])
        fp1.write((article['publishedAt'])[:10])
        fp1.write('\n')     

        # print(article['url']) 
        print(website_translte("ja",article['url']))
        fp1.write(website_translte("ja",article['url']))
        fp1.write('\n') 

        if article['urlToImage'] != None:
            print(article['urlToImage']+'\n')
            fp1.write(article['urlToImage'])
            fp1.write('\n') 

        fp1.write('japan')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n') 



    fp1.close() # 關閉檔案

# 用NewsAPI
def Korea_news():
    fp1 = open("./news_txt/korea.txt", "w+",encoding="utf8") # 開啟檔案

    url = ('https://newsapi.org/v2/everything?'
        'q="코로나19"&'
        'from='+str(today)+'&'
        'to='+str(yesterday)+'&'
        'sortBy=publishedAt&'
        'domains=khan.co.kr&'
        'page=' + str(pageNum) + '&'
        'apiKey=' + API_KEY)

    aRes = requests.get(url)
    newsDict = json.loads(aRes.text)
   
    # print('totalResults: ' + str(newsDict['totalResults']))
    global totalPageNum
    totalPageNum = int(newsDict['totalResults']/20) + 1
    # print('Retrieving Page ' + str(pageNum) + '/' + str(totalPageNum))
    
    for article in newsDict['articles']:
        print(translator(article['title']))
        fp1.write(translator(article['title']))
        fp1.write('\n')  

        print(translator(article['description']).replace("\n", ""))
        fp1.write(translator(article['description']).replace("\n", ""))
        fp1.write('\n')   

        print(article['publishedAt'])
        fp1.write((article['publishedAt'])[:10])
        fp1.write('\n')   

        # print(article['url'])
        print(website_translte("ko",article['url']))
        fp1.write(website_translte("ko",article['url']))
        fp1.write('\n')

        if article['urlToImage'] != None:
            print(article['urlToImage']+'\n')
            fp1.write(article['urlToImage'])
            fp1.write('\n')

        fp1.write('korea')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n') 
        
# 用NewsAPI
def Singapore_news():
    fp1 = open("./news_txt/singapore.txt", "w+",encoding="utf8") # 開啟檔案

    url = ('https://newsapi.org/v2/everything?'
        'q="COVID 19"AND"Singapore"&'
        'from='+str(today)+'&'
        'to='+str(yesterday)+'&'
        'sortBy=publishedAt&'
        'domains=channelnewsasia.com&'
        'page=' + str(pageNum) + '&'
        'apiKey=' + API_KEY)

    aRes = requests.get(url)
    newsDict = json.loads(aRes.text)
   
    # print('totalResults: ' + str(newsDict['totalResults']))
    global totalPageNum
    totalPageNum = int(newsDict['totalResults']/20) + 1
    # print('Retrieving Page ' + str(pageNum) + '/' + str(totalPageNum))
    
    for article in newsDict['articles']:
        print(translator(article['title']).replace("\n", "").replace("\t", "").replace("\r", ""))
        fp1.write(translator(article['title']).replace("\n", "").replace("\t", "").replace("\r", ""))
        fp1.write('\n')  
        try:
            print(translator(article['description']).replace("\n", "").replace("\t", "").replace("\r", ""))
            fp1.write(translator(article['description']).replace("\n", "").replace("\t", "").replace("\r", ""))
            fp1.write('\n')
        except:
            print('\n')
            fp1.write('\n')   
        

        print(article['publishedAt'].replace("\n", ""))
        fp1.write((article['publishedAt'])[:10].replace("\n", ""))
        fp1.write('\n') 

        # print(article['url'])
        print(website_translte("en",article['url']))
        fp1.write(website_translte("en",article['url']))
        fp1.write('\n')


        if article['urlToImage'] != None:
            print(article['urlToImage']+'\n')
            fp1.write(article['urlToImage'])
            fp1.write('\n') 

        fp1.write('singapore')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n') 

def Malaysia_news():
    fp1 = open("./news_txt/malaysia.txt", "w+",encoding="utf8") # 開啟檔案

    url="https://www.orientaldaily.com.my/news/nation"
    data=None
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    ssl._create_default_https_context = ssl._create_unverified_context
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="news-item")
    for title in titles:
        if title.find("a",class_="label") != None:
            if "新闻精选" not in title.a['href']:
                # title
                print(translator(title.a['title'])) 
                fp1.write(translator(title.a['title']))
                fp1.write('\n')                  

                # content
                print(translator(title.p.text))
                fp1.write(translator(translator(title.p.text).replace("\n", "")))
                fp1.write('\n')   

                # 發布日期
                #格式:YYYY/MM/DD XX:XX
                #Y:西元年、M:月份、D:日期 後面是24小時制時間
                date=title.time['datetime'][:-3]
                print(translator(date))
                fp1.write(translator(date)[:10])
                fp1.write('\n')            

                # url
                print(title.a['href'])
                fp1.write(title.a['href'])
                fp1.write('\n')                

                #imgurl
                # print(title.img["src"]+"\n")
                fp1.write((title.img["src"]))
                fp1.write('\n') 

                if title.img != None:
                    print(title.img["src"]+'\n')
                    fp1.write(title.img["src"])
                    fp1.write('\n') 


                fp1.write('malaysia')
                fp1.write('\n') 
                fp1.write(t) 
                fp1.write('\n') 

def Vietnam_news():
    fp1 = open("./news_txt/vietnam.txt", "w+",encoding="utf8") # 開啟檔案

    url="https://vtv.vn/tim-kiem.htm?keywords=COVID-19"
    data=None
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("li",class_="tlitem")
    for title in titles:
        # title
        # print(translator(title.h4.text))
        print(google_translator.translate(title.h4.text, lang_tgt='zh-tw'))
        fp1.write(google_translator.translate(title.h4.text, lang_tgt='zh-tw'))
        fp1.write('\n')         

        # content
        content=title.find("p",class_="sapo")
        # print(translator(content.text))
        print(google_translator.translate(content.text, lang_tgt='zh-tw'))
        fp1.write((google_translator.translate(content.text, lang_tgt='zh-tw')).replace('VTV.VN','').replace('vtv.vn',''))
        fp1.write('\n')   

        # 發布日期
        #格式:YYYY/MM/DD XX:XX
        #Y:西元年、M:月份、D:日期 後面是24小時制時間
        date=title.find("p",class_="time")
        date=date.text
        date=re.split("/| ",date)
        a=date[2]+"/"+date[1]+"/"+date[0]+" "+date[-1]
        print(a)
        fp1.write(a)
        fp1.write('\n') 

        # url
        # print(title.h4.a['href'])
        print(website_translte("vi",title.h4.a['href']))
        fp1.write(website_translte("vi",title.h4.a['href']))
        fp1.write('\n') 

        #imgurl
        print(title.img["src"]+"\n")
        fp1.write(title.img["src"]+"\n")
        fp1.write('vietnam')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n') 
    
def Thailand_news():
    fp1 = open("./news_txt/thailand.txt", "w+",encoding="utf8") # 開啟檔案

    url="https://www.bangkokbiznews.com/corona"
    data=None
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="card-v-wdetail")
    for title in titles:
        # title
        tit=title.find("a",class_="s-news-title")
        print(google_translator.translate(tit.text, lang_tgt='zh-tw'))
        fp1.write(google_translator.translate(tit.text, lang_tgt='zh-tw'))
        fp1.write('\n')    

        # content
        content=title.find("a",class_="s-news-excerpt")
        print(google_translator.translate(content.text, lang_tgt='zh-tw'))
        fp1.write(google_translator.translate(content.text, lang_tgt='zh-tw'))
        fp1.write('\n')        

        # 發布日期
        #格式:YYYY/M/D
        #Y:西元年、M:月份、D:日期 後面是24小時制時間
        # 因為泰國寫日期跟我們不一樣就把它翻譯
        date=title.find("div",class_="s-date")
        date_translate=translator(date.text)
        date_translate=google_translator.translate(date.text, lang_tgt='zh-tw')
        date_translate=date_translate.replace("年","/")
        date_translate=date_translate.replace("月","/")
        date_translate=date_translate.replace("日","")
        print(date_translate)
        fp1.write(date_translate)
        fp1.write('\n')  

        # url
        # print(tit['href'])
        print(website_translte("th",tit['href']))
        fp1.write(website_translte("th",tit['href']))
        fp1.write('\n')          

        #imgurl
        print(title.img["src"]+"\n")
        fp1.write(title.img["src"]+"\n")
        fp1.write('thailand')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n') 

def Philippines_news():
    fp1 = open("./news_txt/philippines.txt", "w+",encoding="utf8") # 開啟檔案

    url="https://mbcn.com.ph/category/%e8%8f%b2%e5%be%8b%e8%b3%93/"
    data=None
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",id=re.compile("^post"))
    # titles=titles.find_all("div")
    for title in titles:
        # title
        print(translator(title.h2.a.text))
        fp1.write(translator(translator(title.h2.a.text)))
        fp1.write('\n')  

        # content
        print(translator(title.p.text))
        fp1.write(translator(title.p.text))
        fp1.write('\n')  

        # 發布日期
        #格式:YYYY/M/D
        #Y:西元年、M:月份、D:日期 後面是24小時制時間
        # 因為泰國寫日期跟我們不一樣就把它翻譯
        date=title.find("span",class_="meta_date")
        date=date.text
        if 'May' in date:
            date=date.replace("May","5")
        elif 'June' in date:
            date=date.replace("June","6")
        elif 'July' in date:
            date=date.replace("July","7")
        elif 'August' in date:
            date=date.replace("August","8")
        elif 'Sertemper' in date:
            date=date.replace("Sertemper","9")
        elif 'October' in date:
            date=date.replace("October","10")
        elif 'November' in date:
            date=date.replace("November","11")
        date=re.split(",| ",date)
        a=date[-1]+"/"+date[0]+"/"+date[1]
        print(a)
        fp1.write(a)
        fp1.write('\n') 

        # url
        print(title.h2.a['href'])  
        fp1.write(title.h2.a['href'])
        fp1.write('\n')

        #imgurl
        print(title.img["src"]+"\n")
        fp1.write(title.img["src"]+"\n")
        fp1.write('philippines')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n') 

def Indonesia_news():
    fp1 = open("./news_txt/indonesia.txt", "w+",encoding="utf8") # 開啟檔案

    url="https://www.cnbcindonesia.com/search?query=COVID%2019&kanal=news&tipe=artikel&date="
    data=None
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find("ul",class_="list media_rows middle thumb terbaru gtm_indeks_feed")
    titles=titles.find_all("li")
    for title in titles:
        # title
        print(translator(title.h2.text))
        fp1.write(translator(title.h2.text))
        fp1.write('\n')   

        # content
        # 這個沒有...
        fp1.write('\n') # 換行取代內文

        # 發布日期
        #格式:YYYY/MM/DD XX:XX
        #Y:西元年、M:月份、D:日期 後面是24小時制時間
        date=GetDate(title.a['href'],"div","date")
        if 'May' in date:
            date=date.replace("May","05")
        elif 'June' in date:
            date=date.replace("June","06")
        elif 'July' in date:
            date=date.replace("July","07")
        elif 'August' in date:
            date=date.replace("August","08")
        elif 'Sertemper' in date:
            date=date.replace("Sertemper","09")
        elif 'October' in date:
            date=date.replace("October","10")
        elif 'November' in date:
            date=date.replace("November","11")
        date=date.split()
        a=date[2]+"/"+date[1]+"/"+date[0]+" "+date[-1]
        print(a)
        fp1.write(a)
        fp1.write('\n')     

        # url
        # print(title.a['href'])
        print(website_translte("id",title.a['href']))
        fp1.write(website_translte("id",title.a['href']))
        fp1.write('\n')     

        #imgurl
        print(title.img['src']+'\n')
        fp1.write(title.img['src']+'\n')
        fp1.write('indonesia')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n')   
  
def Macao_news():
    fp1 = open("./news_txt/macao.txt", "w+",encoding="utf8") # 開啟檔案

    bug = crawler.Crawler("https://www.ettoday.net/news_search/doSearch.php?keywords=%E6%BE%B3%E9%96%80&idx=2&kind=3")
    titles=bug.anaylis("div","archive clearfix")
    for title in titles:
        information=title.find("div",class_="box_2")
         #標題
        print(information.a.string)   
            
        #url
        print(information.a.get('href'))  

        #發布日期 
        #格式:YYYY-MM-DD XX:XX
        #Y:西元年、M:月份、D:日期 後面是24小時制時間
        date=title.find("span",class_="date")
        for i in date.findAll():
            i.decompose()
        release_t = (((date.text.strip('()').strip()).strip("/")).strip()).replace("-","/")
        print(release_t)

        #內容
        content=title.find("p",class_="detail")
        for child in content.findAll():
            child.decompose()
        print(content.text.replace('\n',''))

        img=title.find("div",class_="box_1")
        #imgurl
        print("https:"+img.img['src']+'\n')

        fp1.write(information.a.string)
        fp1.write('\n') 

        fp1.write(content.text.replace('\n','').replace('\r',''))
        fp1.write('\n') 

        fp1.write(release_t)   
        fp1.write('\n') 

        fp1.write(information.a.get('href').replace('\n',''))
        fp1.write('\n') 

        fp1.write("https:"+img.img['src']+'\n')

        fp1.write('macao')
        fp1.write('\n') 

        fp1.write(t) 
        fp1.write('\n')  

def Taiwan_news():
    fp1 = open("./news_txt/taiwan.txt", "w+",encoding="utf8") # 開啟檔案

    url="https://health.udn.com/health/search/%E5%8F%B0%E7%81%A3%E7%96%AB%E6%83%85"
    data=None

    request = req.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("address",class_="search_cards")

    for title in titles:
        tit=title.h2.text
        print(tit)
        fp1.write(tit)
        fp1.write('\n')   

        cont=title.p.text
        print(cont)
        fp1.write(cont)
        fp1.write('\n')   

        date=title.time.text
        print(date)
        fp1.write(date)
        fp1.write('\n')

        url=title.a["href"]
        print(url)
        fp1.write(url)
        fp1.write('\n')

        imgURL=title.a.img["data-original"]
        print(imgURL)
        fp1.write(imgURL)
        fp1.write('\n')
        fp1.write('taiwan')
        fp1.write('\n') 
        fp1.write(t) 
        fp1.write('\n') 


Japan_news()
Korea_news()
Singapore_news()
Malaysia_news()
Vietnam_news()
Thailand_news()
Philippines_news()
Indonesia_news()
Macao_news()
Taiwan_news()

'''
    # 是NewsAPI的東西
    # 現在只print第一頁的結果，這個while
    while pageNum < totalPageNum:
        pageNum += 1
        Japan_news()
'''

all_country=['japan','korea','singapore','malaysia','vietnam','thailand','philippines','indonesia','macao','taiwan']
# 建立一個工作簿
workbook = openpyxl.Workbook()
workbook.save('./news_xlsx/' +t+ ' news'+'.xlsx')
#將爬回來的資料整理進excel
for country in all_country:
    ttx.write_excel(country,t)

 