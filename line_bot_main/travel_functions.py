from datetime import time
from line_bot_Luis import *
from linebot.models import *
import need_to_modify as ntm
line_bot_api = LineBotApi(ntm.Channel_access_token)
handler = WebhookHandler(ntm.Channel_secret)


def sendUse_travel(event):  #旅遊功能按鍵
    try:
        message = TextSendMessage(text='您想了解哪個國家的行程呢？',
        quick_reply=QuickReply(
            #會傳值到handle_postback裡，我用class分類下一步要做什麼
            items=[ QuickReplyButton(action=PostbackAction(label="台灣", text="瞭解台灣的行程" , data='country=taiwan&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="日本", text="瞭解日本的行程" , data='country=japan&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="南韓", text="瞭解南韓的行程" , data='country=korean&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="新加坡", text="瞭解新加坡的行程" , data='country=singapore&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="馬來西亞", text="瞭解馬來西亞的行程" , data='country=malasia&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="泰國", text="瞭解泰國的行程" , data='country=thailand&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="澳門", text="瞭解澳門的行程" , data='country=macao&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="菲律賓", text="瞭解菲律賓的行程" , data='country=philippines&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="越南", text="瞭解越南的行程" , data='country=vietnam&class=menu')),
                    QuickReplyButton(action=PostbackAction(label="印尼", text="瞭解印尼的行程" , data='country=indonesia&class=menu')),
                    ]))  
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='旅遊資訊發生錯誤！'))

def sendUse_menu(event,country):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=7)
    n_day = now + delta
    today_7 = n_day.strftime("%Y-%m-%d")
    today = now.strftime("%Y-%m-%d")

    try:
        #判斷國家圖片、旅行社網址參數
        if country == "japan":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=TYO&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "taiwan":
            ticket= ""
        elif country == "korean":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=SEL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "macao":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=MFM&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "singapore":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=SIN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "china":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=SHA&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "thailand":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=BKK&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "malasia":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=KUL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "vietnam":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=SGN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "indonesia":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=JKT&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "philippines":
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure="+today+"&backdate="+today_7+"&city=MNL&type=ROU&adt=1&chd=0&bclass=EC"
        
        FlexMessage=travel_card.travel_menu(country,ticket)
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(country+'旅遊資訊',FlexMessage))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=country+'旅遊資訊發生錯誤！'))

def select_TravelAgent(event,country):  #選擇旅行社
    try:
        FlexMessage = travel_card.travel_card(country)   
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('旅遊行程',FlexMessage))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='旅行社發生錯誤！'))

def sendUse_travelsettour(event,country): #東南旅遊
    try:
        #判斷國家圖片、旅行社網址參數
        if country == "japan":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%97%A5%E6%9C%AC&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=TYO&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "taiwan":
            travel_agency= "https://trip.settour.com.tw/taiwan/search?tourDays=&departure=&startDate=20210917&endDate=20211117&keyWord=%E5%8F%B0%E7%81%A3&destination="
            ticket= ""
        elif country == "korean":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E9%9F%93%E5%9C%8B&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SEL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "macao":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%BE%B3%E9%96%80&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=MFM&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "singapore":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%96%B0%E5%8A%A0%E5%9D%A1&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SIN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "china":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E4%B8%AD%E5%9C%8B%E5%A4%A7%E9%99%B8&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SHA&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "thailand":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%B3%B0%E5%9C%8B&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_cityo[]=TY_TP&departure=&backdate=&city=BKK&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "malasia":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E9%A6%AC%E4%BE%86%E8%A5%BF%E4%BA%9E&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=KUL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "vietnam":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E8%B6%8A%E5%8D%97&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SGN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "indonesia":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E5%8D%B0%E5%B0%BC&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=JKT&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "philippines":
            travel_agency= "https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E8%8F%B2%E5%BE%8B%E8%B3%93&search-check=pc-check1-1"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=MNL&type=ROU&adt=1&chd=0&bclass=EC"
        
        FlexMessage = travel_card.travel_country_card(country,travel_agency,ticket,"東南旅遊")   
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('旅遊行程資訊',FlexMessage))

        
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！2'))

def sendUse_travelUrlLionTravel(event,country): #雄獅旅行社
    try:
        #判斷國家圖片、旅行社網址參數
        if country == "japan":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=-A-6,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords="
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=TYO&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "taiwan":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=--9,&GoDateStart=2021-09-16&GoDateEnd=2021-10-16&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords="
            ticket= ""
        elif country == "korean":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=韓國"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SEL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "macao":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=2021-08-15&GoDateEnd=2021-09-15&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=%E6%BE%B3%E9%96%80"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=MFM&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "singapore":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=新加坡"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SIN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "china":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=--5,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords="
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SHA&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "thailand":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=泰國"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=BKK&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "malasia":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=馬來西亞"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=KUL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "vietnam":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=越南"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SGN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "indonesia":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=印尼"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=JKT&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "philippines":
            travel_agency= "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=菲律賓"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=MNL&type=ROU&adt=1&chd=0&bclass=EC"
        
        FlexMessage = travel_card.travel_country_card(country,travel_agency,ticket,"雄獅旅遊")   
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('旅遊行程資訊',FlexMessage))

        
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！2'))

def sendUse_travelUrlEzTravel(event,country):   #ezTravel
    try:
        #判斷國家圖片、旅行社網址參數
        if country == "japan":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/24?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=TYO&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "taiwan":
            travel_agency= "https://trip.eztravel.com.tw/domestic/keywords?kw=%E9%81%BF%E6%9A%91&depart=TPE&depDateFrom=20210916&depDateTo=20210930&avaliableOnly=true"
            ticket= ""
        elif country == "korean":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/35?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SEL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "macao":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/448?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=MFM&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "singapore":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/23?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SIN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "china":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/keywords/?q=%E4%B8%AD%E5%9C%8B%E5%A4%A7%E9%99%B8&departure=TPE&"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SHA&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "thailand":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/26?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=BKK&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "malasia":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/37?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=KUL&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "vietnam":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/89?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=SGN&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "indonesia":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/19?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=JKT&type=ROU&adt=1&chd=0&bclass=EC"
        elif country == "philippines":
            travel_agency= "https://vacation.eztravel.com.tw/pkgfrn/results/TPE/31?"
            ticket= "https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY_TP&departure=&backdate=&city=MNL&type=ROU&adt=1&chd=0&bclass=EC"
        

        #給旅行社用
        #取出今天日期
        now = datetime.datetime.now()  
        agency_depDate = now.strftime("%Y%m%d") #日期型式 YYYYMMDD
        travel_agency = travel_agency + "depDateFrom=" + agency_depDate #把網址加上今天日期

        FlexMessage = travel_card.travel_country_card(country,travel_agency,ticket,"ezTravel")   
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('旅遊行程資訊',FlexMessage))

    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

