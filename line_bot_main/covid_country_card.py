from linebot.models import *
import json

def covid_country_card(country, new, sum, death,vac):
    flex_message = ""
    url = ""

    # 判斷國家候選圖片         all_country=['japan','korea','singapore','malaysia','vietnam','thailand','philippines','indonesia','macao']

    if country == "日本" or country == 'japan':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/255px-Flag_of_Japan.svg.png"
        ratio='20:13'
        color = '#AE0000'
    elif country == "台灣" or country == '臺灣' or country == 'taiwan':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Flag_of_Taiwan.png/640px-Flag_of_Taiwan.png"
        ratio='20:13'
        color = '#E0000A'
    elif country == "南韓" or country == 'korea':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/255px-Flag_of_South_Korea.svg.png"
        ratio='20:13'
        color = '#004B97'
    elif country == "澳門" or country == 'macao':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Flag_of_Macau.svg/255px-Flag_of_Macau.svg.png"
        ratio='20:13'
        color = '#067662'
    elif country == "新加坡" or country == 'singapore':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/255px-Flag_of_Singapore.svg.png"
        ratio='20:13'
        color = '#ef1f33'
    elif country == "中國" or country == 'china':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/255px-Flag_of_the_People%27s_Republic_of_China.svg.png"
        ratio='20:13'
        color = '#ef1620'
    elif country == "泰國" or country == 'thailand':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_Thailand.svg/255px-Flag_of_Thailand.svg.png"
        ratio='20:13'
        color = '#292549'
    elif country == "馬來西亞" or country == 'malaysia':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/255px-Flag_of_Malaysia.svg.png"
        ratio='26:13'
        color = '#000066'
    elif country == "越南" or country == 'vietnam':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/255px-Flag_of_Vietnam.svg.png"
        ratio='20:13'
        color = '#db2017'
    elif country == "印尼" or country == 'indonesia':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Indonesia.svg/255px-Flag_of_Indonesia.svg.png"
        ratio='20:13'
        color = '#ff0000'
    elif country == "菲律賓" or country == 'philippines':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_the_Philippines.svg/255px-Flag_of_the_Philippines.svg.png"
        ratio='26:13'
        color = '#0035aa'

    # jp、kor兩個有其它地區的疫情狀況
    if country == "日本" or country == "南韓" or country == "台灣" or country == "臺灣":
        flex_message = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": url,
                "size": "full",
                "aspectRatio": ratio,
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": country,
                        "size": "xl",
                        "weight": "bold",
                        "decoration": "none",
                        "align": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "今日新增 : "+new,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計確診 : "+sum,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計死亡 : "+death,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "接種疫苗人口比例 : "+vac+"%",
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#000001",
                                "margin": "xxl",
                                "height": "120px"
                            }
                        ],
                        "offsetTop": "-10px"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "postback",
                            "label": "查看"+country+"其他地區",
                            "text": "@"+country+"其他地區",
                            "data":"country="+country+"&situation_func_type=other_area&func=covi_situation"
                        },
                        "color": color
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "查看更多國家",
                            "text": "@疫情現況"
                        },
                        "color": color
                    }
                ],
                "offsetTop": "-10px"
            }
        }
    elif country == "新加坡" or country == "印尼":
        flex_message = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": url,
                "size": "full",
                "aspectRatio": ratio,
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                        "type": "separator",
                        "color": "#000000"
                    },
                    {
                        "type": "text",
                        "text": country,
                        "size": "xl",
                        "weight": "bold",
                        "decoration": "none",
                        "align": "center",
                        "offsetTop": "5px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "今日新增 : "+new,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計確診 : "+sum,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計死亡 : "+death,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "接種疫苗人口比例 : "+vac+"%",
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#000001",
                                "margin": "xxl",
                                "height": "120px"
                            }
                        ],
                        "offsetTop": "-10px"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "查看更多國家",
                            "text": "@疫情現況"
                        },
                        "color": color
                    }
                ],
                "offsetTop": "-10px"
            }
        }
    else:
        flex_message = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": url,
                "size": "full",
                "aspectRatio": ratio,
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": country,
                        "size": "xl",
                        "weight": "bold",
                        "decoration": "none",
                        "align": "center",
                        "offsetTop": "5px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "今日新增 : "+new,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計確診 : "+sum,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計死亡 : "+death,
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "接種疫苗人口比例 : "+vac+"%",
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#000001",
                                "margin": "xxl",
                                "height": "120px"
                            }
                        ],
                        "offsetTop": "-10px"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "查看更多國家",
                            "text": "@疫情現況"
                        },
                        "color": color
                    }
                ],
                "offsetTop": "-10px"
            }
        }

    return flex_message

def covid_area_card(country, situation):  #傳進來的situation是二維陣列
    flex_message = ""
    url = ""

    # 判斷國家候選圖片         all_country=['japan','korea','singapore','malaysia','vietnam','thailand','philippines','indonesia','macao']
    if country == "日本" or country == 'japan':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/255px-Flag_of_Japan.svg.png"
        ratio='20:13'
        color = '#AE0000'
    elif country == "南韓" or country == 'korea':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/255px-Flag_of_South_Korea.svg.png"
        ratio='20:13'
        color = '#004B97'
    elif country == "台灣" or country == 'taiwan':
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Flag_of_Taiwan.png/640px-Flag_of_Taiwan.png"
        ratio='20:13'
        color = '#E0000A'

    flex_message={"type":"carousel","contents":[]}  #carousel架構

   
    def area_bubble(area_situation): #這裡的是一維陣列
        #可能要改
        #situation[1]：sum，situation[2]：day_new，situation[4]：death
        area_message = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": url,
                "size": "full",
                "aspectRatio": ratio,
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": str(area_situation[0]).strip(),
                        "size": "xl",
                        "weight": "bold",
                        "decoration": "none",
                        "align": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "今日新增 : "+str(area_situation[2]).strip(),
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計確診 : "+str(area_situation[1]).strip(),
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
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
                                                "type": "icon",
                                                "url": "https://image.flaticon.com/icons/png/128/2659/2659980.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "累計死亡 : "+str(area_situation[4]).strip(),
                                                "color": "#000001",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm",
                                        "borderColor": "#000001"
                                    },
                                    {
                                        "type": "filler"
                                    },
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#000001",
                                "margin": "xxl",
                                "height": "120px"
                            }
                        ],
                        "offsetTop": "-10px"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "查看更多國家",
                            "text": "@疫情現況"
                        },
                        "color": color
                    }
                ],
                "offsetTop": "-10px"
            }
        }

        return area_message


    for area_num in range(len(situation)):
        if area_num == 12:  #因為carousel不能超過12個bubble
            break
        else:
            area = situation[area_num][0]
            if area != country:
                #把各自bubble加入carousel
                flex_message["contents"].append(area_bubble(situation[area_num]))
            

    return flex_message
    
