from line_bot_Luis import *


def senduse_image_map(url, country1, country2, country3, country4):
    alText_1 = return_country_alText(country1)
    alText_2 = return_country_alText(country2)
    alText_3 = return_country_alText(country3)
    alText_4 = return_country_alText(country4)
    imgmap_msg = ImagemapSendMessage(
                base_url=url, 
                alt_text="儀錶板", 
                base_size=BaseSize(height=1040, width=1040),                  
                actions=[
                    MessageImagemapAction(
                        text=alText_1,
                        area=ImagemapArea(
                            x=0, y=0,
                            width=1040, height=1040
                        )
                    ),
                    MessageImagemapAction(
                        text=alText_2,
                        area=ImagemapArea(
                            x=520, y=0,
                            width=1040, height=1040
                        )
                    ),
                    MessageImagemapAction(
                        text=alText_3,
                        area=ImagemapArea(
                            x=0, y=520,
                            width=1040, height=1040
                        )
                    ),
                    MessageImagemapAction(
                        text=alText_4,
                        area=ImagemapArea(
                            x=520, y=520,
                            width=1040, height=1040
                        )
                    )
                ])

    return imgmap_msg


def return_country_alText(country):
    if country == "japan":
        alText = "日本最新現況"
    elif country == "korea":
        alText = "南韓最新現況"
    elif country == "singapore":
        alText = "新加坡最新現況"
    elif country == "malaysia":
        alText = "馬來西亞最新現況"
    elif country == "vietnam":
        alText = "越南最新現況"
    elif country == "thailand":
        alText = "泰國最新現況"
    elif country == "philippines":
        alText = "菲律賓最新現況"
    elif country == "indonesia":
        alText = "印尼最新現況"
    elif country == "macao":
        alText = "澳門最新現況"

    return alText
