# region import...
# from traceback import _PT
from apscheduler.schedulers.background import BackgroundScheduler  # 排程器
from flask import render_template
import json
import http.client

from requests.api import patch
from werkzeug.exceptions import ExpectationFailed
import travel_card
from flask_sqlalchemy import SQLAlchemy
import datetime
import covid_pic_or_situation
import news_card
import covid_country_card
from linebot.models import *
import requests
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler, webhook
from flask import request, abort
from flask import Flask
from urllib.parse import parse_qsl
from PIL import Image
import line_bot_functions as lbf
import travel_functions as tf
import subscribption_functions as sf
import law_functions as lf
import covid_country_card
import image_map
import need_to_modify as ntm
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import wave
from flask import request
# endregion

app = Flask(__name__)

# region 各式連線參數
# 不知道為啥要加這行
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# LINE_BOT_API
line_bot_api = LineBotApi(ntm.Channel_access_token)
handler = WebhookHandler(ntm.Channel_secret)

# AZURE QnA maker
# host = 'coooooool-linebot.azurewebsites.net'  # 主機
# endpoint_key = "0eabd401-f8a3-40ed-81db-9dad0fb188a4"  # 授權碼
# kb = "02dd037e-a9ef-43ba-9d57-dfceb051d2b5"  # GUID碼
host = 'qnatest1023.azurewebsites.net'  # 主機
endpoint_key = "52a34ed2-4e58-4ee1-8ab5-2024cfe1f38e"  # 授權碼
kb = "26a5a80a-94be-491c-9009-e725fe0bd1fc"  # GUID碼
method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"

# AZURE_voice
speech_key, service_region = "8e620401f2ba40099233671f7e8bd081", "southeastasia"

# PostgreSQL Connection
app.config['SQLALCHEMY_DATABASE_URI'] = '' + ntm.Server + '://' + \
    ntm.User + ':' + ntm.Password + '@127.0.0.1:5432/' + ntm.Database + ''
db = SQLAlchemy(app)

# 處理今天日期
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")  # 轉換為指定的格式 YYYY-MM-DD
# endregion


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route("/question_list", methods=['GET', 'POST'])
def home():
    sql_cmd = "select * from question_to_reply "
    query_data = db.engine.execute(sql_cmd)
    # line_bot_api.broadcast(TextSendMessage(text='發生錯誤!!'))
    if request.method == 'POST':
        reply = request.form.get('reply')
        uid = request.form.get('uid')
        datetime = request.form.get('datetime')
        question = request.form.get('question')
        qid = request.form.get('qid')

    #     Confirm_template = TemplateSendMessage(
    #     alt_text='目錄 template',
    #     template=ConfirmTemplate(
    #         title='這是ConfirmTemplate',
    #         text='這就是ConfirmTemplate,用於兩種按鈕選擇',
    #         actions=[
    #             PostbackTemplateAction(
    #                 label='Y',
    #                 text='Y',
    #                 data='action=buy&itemid=1'
    #             ),
    #             MessageTemplateAction(
    #                 label='N',
    #                 text='N'
    #             )
    #         ]
    #     )
    # )
    #     line_bot_api.push_message(uid, Confirm_template)

        reply_msg1 = "親愛的用戶您好，關於日前您所提問:  " + question
        reply_msg2 = "我們的回覆如下:  " + reply
        line_bot_api.push_message(uid, TextSendMessage(text=reply_msg1))
        line_bot_api.push_message(uid, TextSendMessage(text=reply_msg2))
        sql_cmd = "UPDATE public.question_to_reply	SET have_replied= 'Replied' WHERE qid ='" + qid + "'; "
        db.engine.execute(sql_cmd)
        sql_cmd = "select * from question_to_reply "
        query_data = db.engine.execute(sql_cmd)

    return render_template("table_form.html", data=query_data)

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route("/post_submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        qid = request.form.get('qid')
        uid = request.form.get('uid')
        question = request.form.get('question')
        have_replied = request.form.get('have_replied')
        datetime = request.form.get('datetime')

    return render_template("get.html", qid=qid, uid=uid, question=question, have_replied=have_replied, datetime=datetime)
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route("/exception_list", methods=['GET', 'POST'])
def exception_home():
    sql_cmd = "select * from exception_process "
    query_data = db.engine.execute(sql_cmd)
    # line_bot_api.broadcast(TextSendMessage(text='發生錯誤!!'))
    if request.method == 'POST':
        sql_cmd = "select * from exception_process "
        query_data = db.engine.execute(sql_cmd)

    return render_template("exception_table.html", data=query_data)
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route("/exception_solved", methods=['POST'])
def exception_solved():
    qid = request.form.get('qid')
    sql_cmd = "UPDATE public.exception_process	SET have_solved= 'Solved' WHERE eid ='" + qid + "'; "
    db.engine.execute(sql_cmd)
    sql_cmd = "select * from exception_process "
    query_data = db.engine.execute(sql_cmd)

    return render_template("exception_table.html", data=query_data)


# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@app.route("/<country>")
def root(country):
    # 將國家名稱傳入test.py中的openWB(select_country)，同時傳入更新時間～
    # headers = {'Content-Type':'text/xml;charset=utf-8'}
    # return make_response(render_template("travel_"+country+"test.html",user_template=openWB(country),updatetime=updatetime()),200,headers)
    return render_template("travel_"+country+".html", user_template=lf.openWB(country), updatetime=lf.updatetime())

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@handler.add(FollowEvent)  # 處理加入好友的事件 (詢問推播設定)
def handle_follow(event):
    lbf.new_user(event)  # 檢查是否為新好友

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@handler.add(MessageEvent, message=TextMessage)  # 處理文字訊息事件
def handle_message(event):

    lbf.new_user(event)  # 檢查是否為新好友
    mtext = event.message.text
    if mtext == '@操作說明':
        lbf.sendUse_help(event)

    elif mtext == '@疫情現況':
        lbf.sendUse_covid(event)

    elif mtext == '@最新新聞':
        lbf.sendUse_news(event)

    elif mtext == '@旅遊資訊':
        tf.sendUse_travel(event)

    elif mtext == '@法規資訊':
        lbf.sendUse_law(event)

    elif mtext == '@推播設定':
        lbf.subscribe_news_or_situation(event)

    elif mtext == '@7日疫情趨勢圖':
        print('cool_7日疫情趨勢圖')
    #     temp_country = lbf.return_situation_temp_fun(event)
    #     lbf.sendUse_covid_pic7(event, temp_country)

    elif mtext == '@30日疫情趨勢圖':
        print('cool_30日疫情趨勢圖')
    #     temp_country = lbf.return_situation_temp_fun(event)
    #     lbf.sendUse_covid_pic30(event, temp_country)

    elif mtext == '@疫情最新現況':
        print('cool_疫情最新現況')
    #     temp_country = lbf.return_situation_temp_fun(event)
    #     lbf.sendUse_covid_country(event, temp_country)

    elif mtext[3:] == "其他地區":
        print('cool_其他地區')
        # temp_country = lbf.return_situation_temp_fun(event)
        # lbf.sendUse_covid_area(event, temp_country)

    # elif mtext == "測試":
    #     temp_country = lbf.return_situation_temp_fun(event)
    #     lbf.sendUse_covid_area(event, temp_country)

    elif mtext[:4] == '我要訂閱' or mtext[:3] == '選擇:' or mtext[:4] == '我想查看' or mtext == '我想修改訂閱項目' or mtext[:3] == '設定:' or mtext == '我想清除所有訂閱項目' or mtext == '好的' or mtext == '不用了':  # 排除luis介入
        print('')

    # 權恒儀錶板的功能在這邊，你加油，麻煩你了qq
    elif mtext == '@儀表板':
        try:
            sql_cmd = "SELECT * FROM world_situation_statistics WHERE update_time = '" + today + "' "
            query_data = db.engine.execute(sql_cmd)
            situation = list(query_data)
            imgmap_msg = image_map.senduse_image_map(
                situation[0][5], situation[0][0], situation[0][1], situation[0][2], situation[0][3])
            line_bot_api.reply_message(event.reply_token, imgmap_msg)
        except Exception as e:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='儀錶板發生錯誤！'))
            lbf.error_process(e, event)

    else:  # 一般性輸入
        sendLUIS(event, mtext)

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@handler.add(MessageEvent, message=AudioMessage)  # 處理音訊訊息事件
def handle_audio_message(event):

    message_content = line_bot_api.get_message_content(event.message.id)
    use_id = event.source.user_id
    path = "./voice/"+use_id+".m4a"
    print(path)
    # path="use_id.m4a"
    with open(path, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

    lbf.trans_m4a_to_wav(path, "./voice/"+use_id)
    result = lbf.speech_recognizer("./voice/"+use_id+".wav")    
    sendLUIS(event, result)


# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@handler.add(PostbackEvent)  # 處理Postback事件
def handle_postback(event):
    backdata = dict(parse_qsl(event.postback.data))  # 取得Postback資料
    if backdata.get('class') == 'route':
        tf.select_TravelAgent(event, backdata.get('country'))
    # if backdata.get('class') == 'menu':
    #     tf.sendUse_menu(event, backdata.get('country'))
    elif backdata.get('class') == 'travelAgent':
        if backdata.get('agent') == 'ezTravel':
            tf.sendUse_travelUrlEzTravel(event, backdata.get('country'))
        elif backdata.get('agent') == 'Lion':
            tf.sendUse_travelUrlLionTravel(event, backdata.get('country'))
        elif backdata.get('agent') == 'Settour':
            tf.sendUse_travelsettour(event, backdata.get('country'))

    elif backdata.get('action') == 'subscribe' or backdata.get('action') == 'cancel':  # 呼叫 訂閱列表
        action = backdata.get('action')
        item = backdata.get('item')
        country = backdata.get('country')
        print(action, item, country)

        if item == 'news':
            lbf.news_subscribe_fun(event, action, item, country)
            lbf.news_subscribe_flex(event)
        elif item == 'situation':
            lbf.situation_subscribe_fun(event, action, item, country)
            lbf.situation_subscribe_flex(event)

    elif backdata.get('i_want') == 'subscribe_news':  # 呼叫 訂閱新聞  這裡這裡
        lbf.news_subscribe_flex(event)

    elif backdata.get('i_want') == 'subscribe_situation':  # 呼叫 訂閱新聞 這裡這裡
        lbf.situation_subscribe_flex(event)

    elif backdata.get('action') == 'insert_to_question_list':  # 呼叫 將問題存入處理列表
        lbf.question_to_reply(event)
        event.reply_token, TextSendMessage(text='感謝提問，專員將在下個工作日回覆您')

    elif backdata.get('func') == 'covi_situation':  # 疫情功能選擇
        func_type = backdata.get('situation_func_type')
        country = backdata.get('country')
        print(func_type, country)

        if func_type == 'situation':
            lbf.sendUse_covid_country(event, country)
        elif func_type == '7_graph':
            lbf.sendUse_covid_pic7(event, country)
        elif func_type == '30_graph':
            lbf.sendUse_covid_pic30(event, country)
        elif func_type == 'other_area':
            lbf.sendUse_covid_area(event, country)


# '''''''''''''''''''''''''''''''''''''''''''''''''''


def sendQnA(mtext):  # QnA
    question = {
        'question': mtext,
    }
    content = json.dumps(question)
    headers = {
        'Authorization': 'EndpointKey ' + endpoint_key,
        'Content-Type': 'application/json',
        'Content-Length': len(content)
    }
    conn = http.client.HTTPSConnection(host)
    conn.request("POST", method, content, headers)
    response = conn.getresponse()
    result = json.loads(response.read())
    # print(result)
    result1 = result['answers'][0]['answer']
    if 'No good match' in result1:
        text1 = '很抱歉，目前無此國家相關法規\n已轉交給專員，將會在下個工作日回復您!!'
    else:
        text1 = result1
    return text1
# '''''''''''''''''''''''''''''''''''''''''''''''''''


def sendLUIS(event, mtext):  # LUIS
    try:
        r = requests.get('https://my-project-luis.cognitiveservices.azure.com/luis/prediction/v3.0/apps/2b92918d-b2b3-425f-a860-452deb4e9e5c/slots/production/predict?subscription-key=47349ff14daa48af91cae8598caa0b71&verbose=true&show-all-intents=true&log=true&query=' + mtext)
        result = r.json()
        # print(result)

        country1 = ''
        intent1 = ''
        country2 = ''
        intent2 = ''
        country3 = ''
        intent3 = ''
        country4 = ''
        intent4 = ''
        # country5 = ''
        intent5 = ''
        intent5_situation = ''
        intent5_news = ''

        if result["prediction"]['topIntent'] == '國家疫情現況':
            country1 = result["prediction"]['entities']['地點'][0]
            if country1 == '韓國':
                country1 = '南韓'
            intent1 = result["prediction"]['entities']['目的-疫情'][0]
            print("國家："+country1+" 動機："+intent1)

        elif result["prediction"]['topIntent'] == '國家當地新聞':
            country2 = result["prediction"]['entities']['地點'][0]
            if country2 == '韓國':
                country2 = '南韓'
            intent2 = result["prediction"]['entities']['目的_新聞'][0]
            print("國家："+country2+" 動機："+intent2)

        elif result["prediction"]['topIntent'] == '國家法規資訊':
            country3 = result["prediction"]['entities']['地點'][0]
            # intent3 = result["prediction"]['entities']['目的_法規'][0]

        elif result["prediction"]['topIntent'] == '旅遊資訊系統':
            country4 = result["prediction"]['entities']['地點'][0]
            intent4 = result["prediction"]['entities']['目的_旅遊'][0]
            print(country4,intent4)

        elif result["prediction"]['topIntent'] == '推播設定':
            # print(result)
            intent5 = result["prediction"]['entities']['目的_推播'][0]
            try:
                intent5_situation = result["prediction"]['entities']['推播類別_疫情'][0]
            except:
                intent5_news = result["prediction"]['entities']['推播類別_新聞'][0]

        if country1 != '':  # 地點存在，疫情回應
            # message = '問題類別：國家疫情現況\n intent是：'  + intent1 +'\n國家為：' + country1
            # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))

            try:
                # lbf.situation_temp_fun(event, country1)
                # global global_country
                # global_country = country1
                FlexMessage = covid_pic_or_situation.covid_pic_or_situation(
                    country1)
                line_bot_api.reply_message(
                    event.reply_token, FlexSendMessage('疫情資訊類別選擇', FlexMessage))
                # return global_country
            except Exception as e:
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text='疫情資訊類別選擇發生錯誤！'))
                lbf.error_process(e, event)

        elif country2 != '':  # 地點存在，新聞回應
            # message = '問題類別：國家當地新聞\n intent是：'  +intent2 +'\n國家為：' + country2
            # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            if country2 == "日本":
                temp = "japan"
            elif country2 == "台灣" or country2 == "臺灣":
                temp = "taiwan"
            elif country2 == "韓國" or country2 == "南韓":
                temp = "korea"
            elif country2 == "新加坡":
                temp = "singapore"
            elif country2 == "馬來西亞":
                temp = "malaysia"
            elif country2 == "越南":
                temp = "vietnam"
            elif country2 == "泰國":
                temp = "thailand"
            elif country2 == "菲律賓":
                temp = "philippines"
            elif country2 == "印尼":
                temp = "indonesia"
            elif country2 == "澳門":
                temp = "macao"

            try:
                # sql_cmd = "SELECT * FROM world_news WHERE country = '" + temp + "' ORDER BY 6 DESC;"
                sql_cmd = "SELECT * FROM world_news WHERE update_time='"+today+"' AND country = '"+temp+"';"
                print(sql_cmd)
                query_data = db.engine.execute(sql_cmd)
                situation = list(query_data)
                # for i in situation:
                #     print(i)

                FlexMessage = news_card.news_card(country2, situation)
                line_bot_api.reply_message(
                    event.reply_token, FlexSendMessage(country2+"新聞", FlexMessage))

            except Exception as e:
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text=country2+'新聞發生錯誤！'))
                lbf.error_process(e, event)
                lbf.question_to_reply(event)

        elif country3 != '':  # 地點存在，法規回應
            # message = '問題類別：國家法規資訊\n intent是：'  +intent3 +'\n國家為：' + country3
            try:
                temp = sendQnA(mtext)
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text=temp))
                # temp = '以下為日本入境相關法規，僅供參考：\nhttps://db21-120-113-180-135.jp.ngrok.io/japan'
                # line_bot_api.reply_message(
                #     event.reply_token, TextSendMessage(text=temp))
            except Exception as e:
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text=country3+'法規發生錯誤！'))
                lbf.error_process(e, event)
                lbf.question_to_reply(event)

        elif country4 != '':  # 地點存在，旅遊回應，，用postback寫，所以直接放func()進來會出錯，再麻煩你們試試看
            print(country4)
            if country4 == "日本":
                temp = "japan"
            elif country4 == "台灣":
                temp = "taiwan"
            elif country4 == "韓國" or country4 == "南韓":
                temp = "korean"
            elif country4 == "新加坡":
                temp = "singapore"
            elif country4 == "馬來西亞":
                temp = "malasia"
            elif country4 == "越南":
                temp = "vietnam"
            elif country4 == "泰國":
                temp = "thailand"
            elif country4 == "菲律賓":
                temp = "philippines"
            elif country4 == "印尼":
                temp = "indonesia"
            elif country4 == "澳門":
                temp = "macao"
            try:
                tf.sendUse_menu(event, temp)          #有問題
            except Exception as e:
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text=country3+'旅遊發生錯誤！')) 
                lbf.error_process(e,event)
                lbf.question_to_reply(event)

        elif intent5 != '':  # 訂閱請放這，用postback寫，所以直接放func()進來會出錯，再麻煩你們試試看
            if intent5_situation != '':
                lbf.situation_subscribe_flex(event)
            elif intent5_news != '':
                lbf.news_subscribe_flex(event)


    except:
        lbf.question_to_reply(event)

        line_bot_api.reply_message(event.reply_token, TextSendMessage(
            text='抱歉我不太懂您的意思~~ 已轉交給專員，將會在下個工作日回復您!!')
            )
    #     question = event.message.text

    #     Confirm_template = TemplateSendMessage(
    #     alt_text='專員處理',
    #     template=ConfirmTemplate(
    #         title='這是ConfirmTemplate',
    #         text='抱歉我不太懂您的意思~~ 是否需要將您的問題轉交給專員處理?',
    #         actions=[                              
    #             PostbackTemplateAction(
    #                 label='好的',
    #                 text='好的',
    #                 data='action=insert_to_question_list'
    #             ),
    #             MessageTemplateAction(
    #                 label='不用了',
    #                 text='不用了'
    #             )
    #         ]
    #     )
    # )
    #     line_bot_api.reply_message(event.reply_token,Confirm_template)


if __name__ == '__main__':
    app.run(debug= False)

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 自動推播功能(不知道為什麼要放在name==main下面)


def auto_push_all():
    lbf.auto_push_situation()
    lbf.auto_push_news()
    # print("DF")


sched = BackgroundScheduler(daemon=True)
sched.add_job(auto_push_all, 'interval', seconds=15)  # 設定排程時間 幾秒執行一次
# scheduler.add_job(auto_push_all, 'cron', day_of_week='mon-sun', hour=2, minute=50,end_date='2022-05-30') #設定排程時間 每天的幾點幾分執行一次
# sched.start()
