from linebot.models import *


def covid_pic_or_situation(country):
    flex_message = ""
    url = ""

    # 判斷國家候選圖片
    if country == "日本":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/255px-Flag_of_Japan.svg.png"
        ratio='20:13'
    elif country == "台灣" or country == "臺灣":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Flag_of_Taiwan.png/640px-Flag_of_Taiwan.png"
        ratio='20:13'
    elif country == "南韓" or country == "韓國":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/255px-Flag_of_South_Korea.svg.png"
        ratio='20:13'
    elif country == "澳門":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Flag_of_Macau.svg/255px-Flag_of_Macau.svg.png"
        ratio='20:13'
    elif country == "新加坡":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/255px-Flag_of_Singapore.svg.png"
        ratio='20:13'
    elif country == "中國":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/255px-Flag_of_the_People%27s_Republic_of_China.svg.png"
        ratio='20:13'
    elif country == "泰國":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_Thailand.svg/255px-Flag_of_Thailand.svg.png"
        ratio='20:13'
    elif country == "馬來西亞":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/255px-Flag_of_Malaysia.svg.png"
        ratio='26:13'
    elif country == "越南":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/255px-Flag_of_Vietnam.svg.png"
        ratio='20:13'
    elif country == "印尼":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Indonesia.svg/255px-Flag_of_Indonesia.svg.png"
        ratio='20:13'
    elif country == "菲律賓":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_the_Philippines.svg/255px-Flag_of_the_Philippines.svg.png"
        ratio='26:13'

    flex_message = {
        "type": "carousel",
        "contents": [
                {
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                        "type": "image",
                        "url": url,
                        "size": "full",
                        "aspectRatio": ratio,
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing":"sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": country,
                                "style": "normal",
                                "align": "center",
                                "size": "3xl",
                                "margin": "none",
                                "weight": "bold",
                                "decoration": "none",
                            }
                        ],
                        "height": "70px",
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "查看" + country + "今日疫情",
                                    "text": "@疫情最新現況",
                                    "data":"country="+country+"&situation_func_type=situation&func=covi_situation"
                                },
                                "offsetEnd": "none",
                                "offsetTop": "none",
                                "height": "sm",
                                "margin": "none"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "7日疫情趨勢圖",
                                    "text": "@7日疫情趨勢圖",
                                    "data":"country="+country+"&situation_func_type=7_graph&func=covi_situation"
                                },
                                "offsetTop": "none",
                                "height": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "30日疫情趨勢圖",
                                    "text": "@30日疫情趨勢圖",
                                    "data":"country="+country+"&situation_func_type=30_graph&func=covi_situation"
                                },
                                "offsetTop": "none",
                                "height": "sm"
                            }
                        ],
                        "offsetStart": "none",
                        "borderWidth": "none",
                        "offsetTop": "none"
                    }
                }
        ]
    }
    return flex_message
