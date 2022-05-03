from linebot.models import *

# 新聞的FLEX MSG
def news_card(country, situation): 
    news_name = ""
    news_url = ""

    if country == "日本" or country == "japan":
        news_name = "朝日新聞"
        news_url = "https://www.asahi.com"

    elif country  == "台灣" or country == "taiwan":
        news_name = "元氣網"
        news_url = "https://health.udn.com/health/index"

    elif country  == "南韓" or country == "韓國" or country == "korea":
        news_name = "경향신문"
        news_url = "https://m.khan.co.kr/?tab=home"

    elif country == "新加坡" or country == "singapore":
        news_name = "CNA"
        news_url = "https://www.channelnewsasia.com/news/international"

    elif country == "馬來西亞" or country == "malaysia":
        news_name = "東方日報"
        news_url = "https://www.orientaldaily.com.my"

    elif country == "越南" or country == "vietnam":
        news_name = "VTV"
        news_url = "https://vtv.vn/tim-kiem.htm?keywords=COVID-19"

    elif country == "泰國" or country == "thailand":
        news_name = "Bangkokbiz"
        news_url = "https://www.bangkokbiznews.com"

    elif country == "菲律賓" or country == "philippines":
        news_name = "馬尼拉公報"
        news_url = "https://mbcn.com.ph"
        
    elif country == "印尼" or country == "indonesia":
        news_name = "CNBC"
        news_url = "https://www.cnbcindonesia.com"

    elif country == "澳門" or country == "macao":
        news_name = "ETtoday"
        news_url = "https://www.ettoday.net"

    # python中的json若有True，需改成大寫True，否則會報錯
    # situation[][]二微陣列使用說明：
    # situation[i][j]，i為控制第幾則新聞；j=0為新聞標題，j=1為新聞連結，j=2為新聞發布時間，j=3為新聞內文，j=4為新聞國家，j=5為新聞上傳時間，j=6為新聞id，j=7為新聞圖片網址
    # 於situation[][]後加 .strip() 是為了移除換行符號，傳值去json時若有換行符號，會導致FlexSendMessage無法正確讀取！
    # 目前我只放六頁新聞(一個新聞區塊唯為一則新聞)，新聞排序由新至舊，FlexSendMessage最多可放10頁的樣子，若有需要可自行增加
    
    # 可能要修改！！！！！
    flex_message = {
        "type": "carousel",
        "contents": [
            # 新聞區塊1
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": situation[0][6].strip(),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
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
                                            "type": "text",
                                            "text": situation[0][0].strip(),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": situation[0][2].strip(),
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0,
                                            "wrap": True
                                        }
                                    ],
                                    "spacing": "lg"
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
                                                    "text": "新聞連結",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "新聞",
                                                "uri": situation[0][1].strip()
                                            }
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
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": news_name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                            #news_url
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": news_url
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": country,
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
            },
            # 新聞區塊2
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": situation[1][6].strip(),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
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
                                            "type": "text",
                                            "text": situation[1][0].strip(),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": situation[1][2].strip(),
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0,
                                            "wrap": True
                                        }
                                    ],
                                    "spacing": "lg"
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
                                                    "text": "新聞連結",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "新聞",
                                                "uri": situation[1][1].strip()
                                            }
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
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": news_name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                            #news_url
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": news_url
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": country,
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
            },
            # 新聞區塊3
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": situation[2][6].strip(),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
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
                                            "type": "text",
                                            "text": situation[2][0].strip(),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": situation[2][2].strip(),
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0,
                                            "wrap": True
                                        }
                                    ],
                                    "spacing": "lg"
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
                                                    "text": "新聞連結",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "新聞",
                                                "uri": situation[2][1].strip()
                                            }
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
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": news_name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                            #news_url
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": news_url
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": country,
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
            },
            # 新聞區塊4
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": situation[3][6].strip(),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
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
                                            "type": "text",
                                            "text": situation[3][0].strip(),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": situation[3][2].strip(),
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0,
                                            "wrap": True
                                        }
                                    ],
                                    "spacing": "lg"
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
                                                    "text": "新聞連結",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "新聞",
                                                "uri": situation[3][1].strip()
                                            }
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
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": news_name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                            #news_url
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": news_url
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": country,
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
            },
            # 新聞區塊5
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": situation[4][6].strip(),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
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
                                            "type": "text",
                                            "text": situation[4][0].strip(),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": situation[4][2].strip(),
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0,
                                            "wrap": True
                                        }
                                    ],
                                    "spacing": "lg"
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
                                                    "text": "新聞連結",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "新聞",
                                                "uri": situation[4][1].strip()
                                            }
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
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": news_name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                            #news_url
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": news_url
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": country,
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
            },
            # 新聞區塊6
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": situation[5][6].strip(),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
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
                                            "type": "text",
                                            "text": situation[5][0].strip(),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": situation[5][2].strip(),
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0,
                                            "wrap": True
                                        }
                                    ],
                                    "spacing": "lg"
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
                                                    "text": "新聞連結",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "新聞",
                                                "uri": situation[5][1].strip()
                                            }
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
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": news_name,
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px",
                                    "wrap": True
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "23px",
                            "width": "85px",
                            #news_url
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": news_url
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": country,
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
            },

        ]
    }
    return flex_message

# 訂閱清單的FLEX MSG 
# def subscribed_list_card(subscripted_news_1,subscripted_situation_1,subscripted_news_2,subscripted_situation_2): 

    
    country_list = {'japan':'日本', 'indonesia':'印尼', 'korea':'韓國', 'macao':'澳門', 'malaysia':'馬來西亞',
                    'philippines':'菲律賓', 'singapore':'新加坡', 'vietnam':'越南', 'thailand':'泰國', '尚未設定':'尚未設定'}

    subscripted_news_1 = country_list[subscripted_news_1]
    subscripted_situation_1 = country_list[subscripted_situation_1]
    subscripted_news_2 = country_list[subscripted_news_2]
    subscripted_situation_2 = country_list[subscripted_situation_2]

    flex_message = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "訂閱清單",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "text",
        "text": "目前的訂閱項目",
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      },
      {
        "type": "text",
        "text": "可依照您自身需求做調整",
        "size": "xs",
        "color": "#aaaaaa",
        "wrap": True
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "疫情現況1:",
                "size": "md",
                "color": "#555555",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": subscripted_situation_1.strip(),
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "疫情現況2:",
                "size": "md",
                "color": "#555555",
                "flex": 0,
                "weight": "bold"
              },
              {
                "type": "text",
                "text": subscripted_situation_2.strip(),
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "國際新聞1:",
                "size": "md",
                "color": "#555555",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": subscripted_news_1.strip(),
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "國際新聞2:",
                "size": "md",
                "color": "#555555",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": subscripted_news_2.strip(),
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "修改",
              "text": "我想修改訂閱項目"  # 這邊照理來說應該是可以用postback傳資料才對 我先用 msg event接 
            },
            "margin": "none",
            "style": "primary",
            "offsetTop": "none",
            "offsetEnd": "none",
            "offsetStart": "none",
            "offsetBottom": "none"
          }
        ]
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
    }
    return flex_message

# 訂閱國家新聞清單
def subscribe_news_flex_card(have_subscribed_news, twlist, jplist, krlist, sinlist, malaylist, vietlist, thalist, philist, indlist, malist): 

    flex_message ={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "RECEIPT",
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
          },
          {
            "type": "text",
            "text": "已訂閱的新聞:",
            "weight": "bold",
            "size": "xxl",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "size": "lg",
                "color": "#555555",
                "flex": 0,
                "text": have_subscribed_news
              },
              {
                "type": "separator"
              }
            ]
          }
        ]
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/2560px-Flag_of_the_Republic_of_China.svg.png",
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
            "text": "台灣新聞",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [

               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": twlist[0],
                   "data": twlist[1],
                   "displayText": twlist[2]
                 },
                 "style": twlist[3],
                 "height": "sm",
                 "offsetTop": "3%",
                 "color": twlist[4]
               }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    },
  {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://cdn.countryflags.com/thumbs/japan/flag-400.png",
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
            "text": "日本新聞",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "postback",
                  "label": jplist[0],
                  "data": jplist[1],
                  "displayText": jplist[2]
                },
                "style": jplist[3],
                "color": jplist[4],
                "position": "relative",
                "margin": "sm",
                "height": "sm"
                }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    },
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://cdn.countryflags.com/thumbs/south-korea/flag-400.png",
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
            "text": "韓國新聞",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "postback",
                  "label": krlist[0],
                  "data":  krlist[1],
                  "displayText":  krlist[2]
                },
                "style":  krlist[3],
                "color":  krlist[4],
                "position": "relative",
                "margin": "sm",
                "height": "sm"
              }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    },
     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://static3.depositphotos.com/1000209/137/v/600/depositphotos_1378158-stock-illustration-singapore-flag-vector-illustration.jpg",
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
             "text": "新加坡新聞",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": sinlist[0],
                   "data": sinlist[1],
                   "displayText": sinlist[2]
                 },
                 "style": sinlist[3],
                 "color": sinlist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },

     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/1949_Malaya_Flag_Proposal_3.png/1200px-1949_Malaya_Flag_Proposal_3.png",
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
             "text": "馬來西亞新聞",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": malaylist[0],
                   "data": malaylist[1],
                   "displayText": malaylist[2]
                 },
                 "style": malaylist[3],
                 "color": malaylist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/1024px-Flag_of_Vietnam.svg.png",
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
             "text": "越南新聞",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": vietlist[0],
                   "data": vietlist[1],
                   "displayText": vietlist[2]
                 },
                 "style": vietlist[3],
                 "color": vietlist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://cdn.countryflags.com/thumbs/thailand/flag-400.png",
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
             "text": "泰國新聞",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":thalist[0],
                   "data": thalist[1],
                   "displayText": thalist[2]
                 },
                 "style": thalist[3],
                 "color": thalist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
    {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://cdn.britannica.com/73/3473-004-6E573BFA/Flag-Philippines.jpg",
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
             "text": "菲律賓新聞",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":philist[0],
                   "data": philist[1],
                   "displayText": philist[2]
                 },
                 "style": philist[3],
                 "color": philist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
    {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Indonesia.svg/2560px-Flag_of_Indonesia.svg.png",
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
             "text": "印度新聞",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":indlist[0],
                   "data": indlist[1],
                   "displayText": indlist[2]
                 },
                 "style": indlist[3],
                 "color": indlist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Flag_of_Macau.svg/1024px-Flag_of_Macau.svg.png",
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
            "text": "澳門新聞",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":malist[0],
                   "data": malist[1],
                   "displayText": malist[2]
                 },
                 "style": malist[3],
                 "color": malist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    }
  ]
}
    return flex_message



# 訂閱國家疫情清單
def subscribe_situation_flex_card(have_subscribed_situation, twlist, jplist, krlist, sinlist, malaylist, vietlist, thalist, philist, indlist, malist): 

    flex_message ={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "RECEIPT",
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
          },
          {
            "type": "text",
            "text": "已訂閱的疫情:",
            "weight": "bold",
            "size": "xxl",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "size": "lg",
                "color": "#555555",
                "flex": 0,
                "text": have_subscribed_situation
              },
              {
                "type": "separator"
              }
            ]
          }
        ]
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/2560px-Flag_of_the_Republic_of_China.svg.png",
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
            "text": "台灣疫情",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [

               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": twlist[0],
                   "data": twlist[1],
                   "displayText": twlist[2]
                 },
                 "style": twlist[3],
                 "height": "sm",
                 "offsetTop": "3%",
                 "color": twlist[4]
               }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    },
  {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://cdn.countryflags.com/thumbs/japan/flag-400.png",
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
            "text": "日本疫情",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "postback",
                  "label": jplist[0],
                  "data": jplist[1],
                  "displayText": jplist[2]
                },
                "style": jplist[3],
                "color": jplist[4],
                "position": "relative",
                "margin": "sm",
                "height": "sm"
                }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    },
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://cdn.countryflags.com/thumbs/south-korea/flag-400.png",
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
            "text": "韓國疫情",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "postback",
                  "label": krlist[0],
                  "data":  krlist[1],
                  "displayText":  krlist[2]
                },
                "style":  krlist[3],
                "color":  krlist[4],
                "position": "relative",
                "margin": "sm",
                "height": "sm"
              }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    },
     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://static3.depositphotos.com/1000209/137/v/600/depositphotos_1378158-stock-illustration-singapore-flag-vector-illustration.jpg",
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
             "text": "新加坡疫情",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": sinlist[0],
                   "data": sinlist[1],
                   "displayText": sinlist[2]
                 },
                 "style": sinlist[3],
                 "color": sinlist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },

     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/1949_Malaya_Flag_Proposal_3.png/1200px-1949_Malaya_Flag_Proposal_3.png",
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
             "text": "馬來西亞疫情",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": malaylist[0],
                   "data": malaylist[1],
                   "displayText": malaylist[2]
                 },
                 "style": malaylist[3],
                 "color": malaylist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/1024px-Flag_of_Vietnam.svg.png",
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
             "text": "越南疫情",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label": vietlist[0],
                   "data": vietlist[1],
                   "displayText": vietlist[2]
                 },
                 "style": vietlist[3],
                 "color": vietlist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
     {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://cdn.countryflags.com/thumbs/thailand/flag-400.png",
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
             "text": "泰國疫情",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":thalist[0],
                   "data": thalist[1],
                   "displayText": thalist[2]
                 },
                 "style": thalist[3],
                 "color": thalist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
    {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://cdn.britannica.com/73/3473-004-6E573BFA/Flag-Philippines.jpg",
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
             "text": "菲律賓疫情",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":philist[0],
                   "data": philist[1],
                   "displayText": philist[2]
                 },
                 "style": philist[3],
                 "color": philist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
    {
       "type": "bubble",
       "size": "kilo",
       "hero": {
         "type": "image",
         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Indonesia.svg/2560px-Flag_of_Indonesia.svg.png",
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
             "text": "印度疫情",
             "weight": "bold",
             "size": "xxl",
             "wrap": True,
             "style": "normal",
             "align": "center",
             "margin": "none",
             "offsetStart": "none"
           },
           {
             "type": "box",
             "layout": "vertical",
             "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":indlist[0],
                   "data": indlist[1],
                   "displayText": indlist[2]
                 },
                 "style": indlist[3],
                 "color": indlist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
             ],
             "paddingAll": "sm",
             "paddingTop": "none",
             "paddingBottom": "xl",
             "paddingStart": "lg",
             "paddingEnd": "lg",
             "spacing": "lg"
           }
         ],
         "spacing": "sm",
         "paddingAll": "13px",
         "backgroundColor": "#ecf0f1",
         "borderWidth": "none"
       }
     },
    {
      "type": "bubble",
      "size": "kilo",
      "hero": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Flag_of_Macau.svg/1024px-Flag_of_Macau.svg.png",
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
            "text": "澳門疫情",
            "weight": "bold",
            "size": "xxl",
            "wrap": True,
            "style": "normal",
            "align": "center",
            "margin": "none",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
               {
                 "type": "button",
                 "action": {
                   "type": "postback",
                   "label":malist[0],
                   "data": malist[1],
                   "displayText": malist[2]
                 },
                 "style": malist[3],
                 "color": malist[4],
                 "position": "relative",
                 "margin": "sm",
                 "height": "sm"
               }
            ],
            "paddingAll": "sm",
            "paddingTop": "none",
            "paddingBottom": "xl",
            "paddingStart": "lg",
            "paddingEnd": "lg",
            "spacing": "lg"
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px",
        "backgroundColor": "#ecf0f1",
        "borderWidth": "none"
      }
    }
  ]
}
    return flex_message

