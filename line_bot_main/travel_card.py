from linebot.models import *

def travel_card(country):
    agency={
        "japan":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%97%A5%E6%9C%AC&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=-A-6,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/24?",
            }
        ],
        "taiwan":[
            {
                "settour":"https://trip.settour.com.tw/taiwan/search?tourDays=&departure=&startDate=20210917&endDate=20211117&keyWord=%E5%8F%B0%E7%81%A3&destination=",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=--9,&GoDateStart=2021-09-16&GoDateEnd=2021-10-16&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=",
                "eztravel":"https://trip.eztravel.com.tw/domestic/keywords?kw=%E9%81%BF%E6%9A%91&depart=TPE&depDateFrom=20210916&depDateTo=20210930&avaliableOnly=true",
            }
        ],
        "korean":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E9%9F%93%E5%9C%8B&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=韓國",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/35?",
            }
        ],
        "macao":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%BE%B3%E9%96%80&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=2021-08-15&GoDateEnd=2021-09-15&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=%E6%BE%B3%E9%96%80",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/448?",
            }
        ],
        "singapore":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%96%B0%E5%8A%A0%E5%9D%A1&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=新加坡",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/23?",
            }
        ],
        "china":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E4%B8%AD%E5%9C%8B%E5%A4%A7%E9%99%B8&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=--5,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/keywords/?q=%E4%B8%AD%E5%9C%8B%E5%A4%A7%E9%99%B8&departure=TPE&",
            }
        ],
        "thailand":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E6%B3%B0%E5%9C%8B&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=泰國",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/26?",
            }
        ],
        "malasia":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E9%A6%AC%E4%BE%86%E8%A5%BF%E4%BA%9E&search-check=pc-check1-1",
                "lion": "https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=馬來西亞",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/37?",
            }
        ],
        "vietnam":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E8%B6%8A%E5%8D%97&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=越南",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/89?",
            }
        ],
        "indonesia":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E5%8D%B0%E5%B0%BC&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=印尼",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/19?",
            }
        ],
        "philippines":[
            {
                "settour":"https://tour.settour.com.tw/search?destinationCode=&sortType=BA&departureCode=&depDate=20210818&arrDate=20211018&isOrderFlag=true&isNoPay=false&isNoShopping=false&keyWords=%E8%8F%B2%E5%BE%8B%E8%B3%93&search-check=pc-check1-1",
                "lion":"https://travel.liontravel.com/search?DepartureID=&ArriveID=,&GoDateStart=&GoDateEnd=&Days=&IsEnsureGroup=false&IsSold=true&TravelType=0&GroupID=&Keywords=菲律賓",
                "eztravel":"https://vacation.eztravel.com.tw/pkgfrn/results/TPE/31?",
            }
        ],
    }

    flex_message = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "kilo",
                "hero": {
                    "type": "image",
                    "url": "https://lh3.googleusercontent.com/RMzLlX7QMGZbPWjxeEtTCQtnY6J7fhYOJCBkYdTVzmHu633W8j9P0-RUsnPmide16XKDvAU3GIBrTLWW=w1080-h608-p-no-v0",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "ezTravel 易遊網",
                            "weight": "bold",
                            "size": "xl",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1138/1138518.png"
                                        },
                                        {
                                            "type": "text",
                                            "text": "價格：",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/128/3132/3132778.png"
                                        },
                                        {
                                            "type": "text",
                                            "text": "評價：",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/2107/2107685.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "低價策略、主流路線為主",
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "button",
                            "action": {
                                # "type": "postback",
                                # "label": "就是他了",
                                # "data": "country="+country+"&agent=ezTravel&class=travelAgent"
                                "type": "uri",
                                "label": "就是他了",
                                "uri": agency[country][0]["eztravel"]
                            },
                            "color": "#005AB5",
                            "margin": "md"
                        }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
            },
            {
                "type": "bubble",
                "size": "kilo",
                "hero": {
                    "type": "image",
                    "url": "https://www.liontravel.com/omo/edm/specialedm/210611-m/images/epaper_logo.png",
                    "size": "full",
                    "aspectMode": "fit",
                    "aspectRatio": "320:213",
                    "backgroundColor": "#E0E0E0"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "雄獅旅遊",
                            "weight": "bold",
                            "size": "xl",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1138/1138518.png"
                                        },
                                        {
                                            "type": "text",
                                            "text": "價格：",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/2107/2107685.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/128/3132/3132778.png"
                                        },
                                        {
                                            "type": "text",
                                            "text": "評價：",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/2107/2107685.png"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "團多、選擇多、辦事方便",
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                    ]
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        # "type": "postback",
                                        # "label": "就是他了",
                                        # "data": "country="+country+"&agent=Lion&class=travelAgent"
                                        "type": "uri",
                                        "label": "就是他了",
                                        "uri": agency[country][0]["lion"]
                                    },
                                    "color": "#005AB5",
                                    "margin": "md"
                                }
                            ]
                        }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
            },
            {
                "type": "bubble",
                "size": "kilo",
                "hero": {
                    "type": "image",
                    "url": "https://img.biggo.com.tw/sqm0jwPNcN9rp2_ZQ9UMdaKI--j4M4m3SQvx-eYD9W1M/https://biggo.com.tw/images/cashback/tw_pec_settour@2x.png",
                    "size": "full",
                    "aspectMode": "fit",
                    "aspectRatio": "320:213",
                    "backgroundColor": "#E0E0E0"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "東南旅遊",
                            "weight": "bold",
                            "size": "xl",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1138/1138518.png"
                                        },
                                        {
                                            "type": "text",
                                            "text": "價格：",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/2107/2107685.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828970.png"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/128/3132/3132778.png"
                                        },
                                        {
                                            "type": "text",
                                            "text": "評價：",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/1828/1828614.png"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/png/512/2107/2107685.png"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "導遊服務專業、品質穩定",
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                    ]
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        # "type": "postback",
                                        # "label": "就是他了",
                                        # "data": "country="+country+"&agent=Settour&class=travelAgent"
                                        "type": "uri",
                                        "label": "就是他了",
                                        "uri": agency[country][0]["settour"]
                                    },
                                    "color": "#005AB5",
                                    "margin": "md"
                                }
                            ]
                        }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
            }
        ]


    }
    return flex_message

def travel_country_card(country, agency, ticket, agency_name):

    if country == "japan":
        name = "日本"
        img_url = "https://i.pinimg.com/564x/65/a9/43/65a9434b8b627940627b024296f2121c.jpg"
    elif country == "taiwan":
        name = "台灣"
        img_url = "https://i.pinimg.com/564x/8b/6d/b3/8b6db3ef0e53a0a450cc6a9b4cc48715.jpg"
    elif country == "korean":
        name = "南韓"
        img_url = "https://i.pinimg.com/564x/35/3b/8d/353b8df401f9b45a469d5c87edd1355f.jpg"
    elif country == "macao":
        name = "澳門"
        img_url = "https://i.pinimg.com/564x/e4/db/2b/e4db2bc74c35432417cbf96a19d3dcef.jpg"
    elif country == "singapore":
        name = "新加坡"
        img_url = "https://i.pinimg.com/564x/f2/a5/31/f2a53195bc37c784b98d23f060b2b3e1.jpg"
    elif country == "china":
        name = "中國"
        img_url = "https://i.pinimg.com/564x/0b/48/f7/0b48f714d57d9733ca88d92c14740b30.jpg"
    elif country == "thailand":
        name = "泰國"
        img_url = "https://i.pinimg.com/564x/fb/69/18/fb69180fd4e84f95cff8cb7e43360fad.jpg"
    elif country == "malasia":
        name = "馬來西亞"
        img_url = "https://live.staticflickr.com/4811/46930132441_efc558fbf4_b.jpg"
    elif country == "vietnam":
        name = "越南"
        img_url = "https://i.pinimg.com/564x/e0/39/ff/e039ff64995659c47c86c10dfb665ebf.jpg"
    elif country == "indonesia":
        name = "印尼"
        img_url = "https://i.pinimg.com/564x/02/21/ad/0221ad079845c3157be2a3e2bef978ce.jpg"
    elif country == "philippines":
        name = "菲律賓"
        img_url = "https://i.pinimg.com/564x/62/0b/91/620b9164eba4d0eab94f4a814cc03384.jpg"

    if country == "taiwan":
        flex_message={
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": img_url,
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top",
                            "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": agency
                                    }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "旅行社行程",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": agency
                                    }
                                },
                            ],
                            "position": "relative",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "10px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px"
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": agency_name,
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#a6ed8e",
                            "height": "23px",
                            "width": "85px",
                            "offsetEnd": "18px"
                        }
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
    }
    else:
        flex_message = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": img_url,
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top",
                            "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": agency
                                    }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "旅行社行程",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": agency
                                    }
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "機票資訊",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": ticket
                                    }
                                }
                            ],
                            "position": "relative",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "10px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px"
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": agency_name,
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#a6ed8e",
                            "height": "23px",
                            "width": "85px",
                            "offsetEnd": "18px"
                        }
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
    }

    return flex_message

def travel_menu(country, ticket):
    if country == "japan":
        name = "日本"
        img_url = "https://i.pinimg.com/564x/65/a9/43/65a9434b8b627940627b024296f2121c.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-519-c8ecd-1.html"
    elif country == "taiwan":
        name = "台灣"
        img_url = "https://i.pinimg.com/564x/8b/6d/b3/8b6db3ef0e53a0a450cc6a9b4cc48715.jpg"
    elif country == "korean":
        name = "南韓"
        img_url = "https://i.pinimg.com/564x/35/3b/8d/353b8df401f9b45a469d5c87edd1355f.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-409-01e96-1.html"
    elif country == "macao":
        name = "澳門"
        img_url = "https://i.pinimg.com/564x/e4/db/2b/e4db2bc74c35432417cbf96a19d3dcef.jpg"
        waring="https://www.mac.gov.tw/News.aspx?n=E0243AD02975213D"
    elif country == "singapore":
        name = "新加坡"
        img_url = "https://i.pinimg.com/564x/f2/a5/31/f2a53195bc37c784b98d23f060b2b3e1.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-695-9e491-1.html"
    elif country == "china":
        name = "中國"
        img_url = "https://i.pinimg.com/564x/0b/48/f7/0b48f714d57d9733ca88d92c14740b30.jpg"
        waring="https://www.mac.gov.tw/News.aspx?n=E0243AD02975213D"
    elif country == "thailand":
        name = "泰國"
        img_url = "https://i.pinimg.com/564x/fb/69/18/fb69180fd4e84f95cff8cb7e43360fad.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-706-61d73-1.html"
    elif country == "malasia":
        name = "馬來西亞"
        img_url = "https://live.staticflickr.com/4811/46930132441_efc558fbf4_b.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-253-95de0-1.html"
    elif country == "vietnam":
        name = "越南"
        img_url = "https://i.pinimg.com/564x/e0/39/ff/e039ff64995659c47c86c10dfb665ebf.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-320-03c21-1.html"
    elif country == "indonesia":
        name = "印尼"
        img_url = "https://i.pinimg.com/564x/02/21/ad/0221ad079845c3157be2a3e2bef978ce.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-720-cae7e-1.html"
    elif country == "philippines":
        name = "菲律賓"
        img_url = "https://i.pinimg.com/564x/62/0b/91/620b9164eba4d0eab94f4a814cc03384.jpg"
        waring="https://www.boca.gov.tw/sp-trwa-content-715-19619-1.html"

    if country == "taiwan":
        flex_message={
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": img_url,
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top",
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "旅行社行程",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "action": {
                                        "type": "postback",
                                        "label": "action",
                                        "data":"country="+country+"&class=route"
                                    }
                                },
                            ],
                            "position": "relative",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "10px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px"
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                        },
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
    }
    else:
        flex_message = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": img_url,
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top",
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "旅遊警示資訊",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": waring
                                    }
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "旅行社行程",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "action": {
                                        "type": "postback",
                                        "label": "action",
                                        "data": "country="+country+"&class=route"
                                    }
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "機票資訊",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": ticket
                                    }
                                },
                            ],
                            "position": "relative",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "10px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px"
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                        },
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
    }

    return flex_message