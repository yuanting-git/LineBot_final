import pydub
from line_bot_Luis import *
import covid_country_card
import datetime

#region 人工處理未知問題的function -------------------------------------------------------------------------
def question_to_reply(event):
    uid = event.source.user_id # 取得使用者的UID
    question = event.message.text

    datetime_dt = datetime.datetime.today()
    datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M")
    print(datetime_str) 
    print(uid, question)
    sql_cmd = "INSERT INTO public.question_to_reply(uid, question,datetime)VALUES ('" + uid + "','" + question + "','" + datetime_str +"');"
    db.engine.execute(sql_cmd)
# endregion

# region 記錄錯誤訊息function-------------------------------------------------------------------------------
def error_process(e,event):
    import sys
    import traceback
    question = event.message.text
    error_class = e.__class__.__name__ #取得錯誤類型
    detail = e.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    datetime_dt = datetime.datetime.today()
    datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M")

    sql_cmd = "INSERT INTO public.exception_process(error_message, fileName, lineNum, error_class, error_detail,datetime)VALUES ('" + question + "','" + fileName + "','" + str(lineNum) + "','" + error_class +"','" + detail+ "','" + datetime_str +"');"
    db.engine.execute(sql_cmd)

def auto_push_error_process(e,question):
    import sys
    import traceback
    error_class = e.__class__.__name__ #取得錯誤類型
    detail = e.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    datetime_dt = datetime.datetime.today()
    datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M")

    sql_cmd = "INSERT INTO public.exception_process(error_message, fileName, lineNum, error_class, error_detail,datetime)VALUES ('" + question + "','" + fileName + "','" + str(lineNum) + "','" + error_class +"','" + detail+ "','" + datetime_str +"');"
    db.engine.execute(sql_cmd)

#endregion

#region 有關推播功能的function -------------------------------------------------------------------------
def subscribe_news_or_situation(event): # 選擇要設定 疫情現況/新聞 
    try:
        message = TextSendMessage(text='要訂閱疫情現況還是國際新聞:',
        quick_reply=QuickReply(
            items=[ QuickReplyButton(action=PostbackAction(label="訂閱疫情現況",text="我要訂閱疫情現況",data='i_want=subscribe_situation')),
                    QuickReplyButton(action=PostbackAction(label="訂閱國際新聞",text="我要訂閱國際新聞",data='i_want=subscribe_news'))
                    ]))     

        line_bot_api.reply_message(event.reply_token,message)
    except Exception as e:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='訂閱選擇發生錯誤！'))
        error_process(e,event)

def news_subscribe_flex(event): # 呼叫 訂閱新聞的清單(FLEX MSG)
    try:
        user_id = event.source.user_id # 取得使用者的UID

        have_subscribed_news = ' '
        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"

        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][1] == 'subscribe':
            have_subscribed_news += '日本 '
            jp_sub=["取消訂閱新聞","action=cancel&item=news&country=japan","取消成功!","secondary","#bdc3c7"]             
        else:
            jp_sub=["訂閱新聞","action=subscribe&item=news&country=japan","訂閱日本成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][2] == 'subscribe':
            have_subscribed_news += '韓國 ' 
            kr_sub=["取消訂閱新聞","action=cancel&item=news&country=korea","取消成功!","secondary","#bdc3c7"]             
        else:
            kr_sub=["訂閱新聞","action=subscribe&item=news&country=korea","訂閱韓國成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][3] == 'subscribe':
            have_subscribed_news += '新加坡 '
            sin_sub=["取消訂閱新聞","action=cancel&item=news&country=singapore","取消成功!","secondary","#bdc3c7"]             
        else:
            sin_sub=["訂閱新聞","action=subscribe&item=news&country=singapore","訂閱新加坡成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][4] == 'subscribe':
            have_subscribed_news += '馬來西亞 ' 
            malay_sub=["取消訂閱新聞","action=cancel&item=news&country=malaysia","取消成功!","secondary","#bdc3c7"]             
        else:
            malay_sub=["訂閱新聞","action=subscribe&item=news&country=malaysia","訂閱馬來西亞成功!","primary","#27ae60"]

        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][5] == 'subscribe':
            have_subscribed_news += '越南 '
            viet_sub=["取消訂閱新聞","action=cancel&item=news&country=vietnam","取消成功!","secondary","#bdc3c7"]             
        else:
            viet_sub=["訂閱新聞","action=subscribe&item=news&country=vietnam","訂閱越南成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][6] == 'subscribe':
            have_subscribed_news += '泰國 ' 
            tha_sub=["取消訂閱新聞","action=cancel&item=news&country=thailand","取消成功!","secondary","#bdc3c7"]             
        else:
            tha_sub=["訂閱新聞","action=subscribe&item=news&country=thailand","訂閱泰國成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][7] == 'subscribe':
            have_subscribed_news += '菲律賓 '
            phi_sub=["取消訂閱新聞","action=cancel&item=news&country=philippines","取消成功!","secondary","#bdc3c7"]             
        else:
            phi_sub=["訂閱新聞","action=subscribe&item=news&country=philippines","訂閱菲律賓成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][8] == 'subscribe':
            have_subscribed_news += '印尼 ' 
            ind_sub=["取消訂閱新聞","action=cancel&item=news&country=indonesia","取消成功!","secondary","#bdc3c7"]             
        else:
            ind_sub=["訂閱新聞","action=subscribe&item=news&country=indonesia","訂閱印尼成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][9] == 'subscribe':
            have_subscribed_news += '澳門 ' 
            ma_sub=["取消訂閱新聞","action=cancel&item=news&country=macao","取消成功!","secondary","#bdc3c7"]             
        else:
            ma_sub=["訂閱新聞","action=subscribe&item=news&country=macao","訂閱澳門成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_news where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][10] == 'subscribe':
            have_subscribed_news += '台灣 '  
            tw_sub=["取消訂閱新聞","action=cancel&item=news&country=taiwan","取消成功!","secondary","#bdc3c7"]           
        else:
            tw_sub=["訂閱新聞","action=subscribe&item=news&country=taiwan","訂閱台灣成功!","primary","#27ae60"]

        FlexMessage = news_card.subscribe_news_flex_card(have_subscribed_news,tw_sub, jp_sub , kr_sub , sin_sub , malay_sub , viet_sub , tha_sub , phi_sub , ind_sub , ma_sub)
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('訂閱清單',FlexMessage))
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='訂閱清單發生錯誤！'))

def situation_subscribe_flex(event): # 呼叫 訂閱現況的清單(FLEX MSG)
    try:
        user_id = event.source.user_id # 取得使用者的UID

        have_subscribed_situation = ' '
        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][1] == 'subscribe':
            have_subscribed_situation += '日本 '
            jp_sub=["取消訂閱疫情","action=cancel&item=situation&country=japan","取消成功!","secondary","#bdc3c7"]             
        else:
            jp_sub=["訂閱疫情","action=subscribe&item=situation&country=japan","訂閱日本成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][2] == 'subscribe':
            have_subscribed_situation += '韓國 ' 
            kr_sub=["取消訂閱疫情","action=cancel&item=situation&country=korea","取消成功!","secondary","#bdc3c7"]             
        else:
            kr_sub=["訂閱疫情","action=subscribe&item=situation&country=korea","訂閱韓國成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][3] == 'subscribe':
            have_subscribed_situation += '新加坡 '
            sin_sub=["取消訂閱疫情","action=cancel&item=situation&country=singapore","取消成功!","secondary","#bdc3c7"]             
        else:
            sin_sub=["訂閱疫情","action=subscribe&item=situation&country=singapore","訂閱新加坡成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][4] == 'subscribe':
            have_subscribed_situation += '馬來西亞 ' 
            malay_sub=["取消訂閱疫情","action=cancel&item=situation&country=malaysia","取消成功!","secondary","#bdc3c7"]             
        else:
            malay_sub=["訂閱疫情","action=subscribe&item=situation&country=malaysia","訂閱馬來西亞成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][5] == 'subscribe':
            have_subscribed_situation += '越南 '
            viet_sub=["取消訂閱疫情","action=cancel&item=situation&country=vietnam","取消成功!","secondary","#bdc3c7"]             
        else:
            viet_sub=["訂閱疫情","action=subscribe&item=situation&country=vietnam","訂閱越南成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][6] == 'subscribe':
            have_subscribed_situation += '泰國 ' 
            tha_sub=["取消訂閱疫情","action=cancel&item=situation&country=thailand","取消成功!","secondary","#bdc3c7"]             
        else:
            tha_sub=["訂閱疫情","action=subscribe&item=situation&country=thailand","訂閱泰國成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][7] == 'subscribe':
            have_subscribed_situation += '菲律賓 '
            phi_sub=["取消訂閱疫情","action=cancel&item=situation&country=philippines","取消成功!","secondary","#bdc3c7"]             
        else:
            phi_sub=["訂閱疫情","action=subscribe&item=situation&country=philippines","訂閱菲律賓成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][8] == 'subscribe':
            have_subscribed_situation += '印尼 ' 
            ind_sub=["取消訂閱疫情","action=cancel&item=situation&country=indonesia","取消成功!","secondary","#bdc3c7"]             
        else:
            ind_sub=["訂閱疫情","action=subscribe&item=situation&country=indonesia","訂閱印尼成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][9] == 'subscribe':
            have_subscribed_situation += '澳門 ' 
            ma_sub=["取消訂閱疫情","action=cancel&item=situation&country=macao","取消成功!","secondary","#bdc3c7"]             
        else:
            ma_sub=["訂閱疫情","action=subscribe&item=situation&country=macao","訂閱澳門成功!","primary","#27ae60"]

        sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if list(query_data)[0][10] == 'subscribe':
            have_subscribed_situation += '台灣 '  
            tw_sub=["取消訂閱疫情","action=cancel&item=situation&country=taiwan","取消成功!","secondary","#bdc3c7"]           
        else:
            tw_sub=["訂閱疫情","action=subscribe&item=situation&country=taiwan","訂閱台灣成功!","primary","#27ae60"]
        # ----------------------------------------------------------------------------------
        # if list(query_data)[0][1] == 'subscribe':
        #     have_subscribed_situation += '日本 '

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][2] == 'subscribe':
        #     have_subscribed_situation += '韓國 ' 

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][3] == 'subscribe':
        #     have_subscribed_situation += '新加坡 '

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][4] == 'subscribe':
        #     have_subscribed_situation += '馬來西亞 '

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][5] == 'subscribe':
        #     have_subscribed_situation += '越南 '

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][6] == 'subscribe':
        #     have_subscribed_situation += '泰國 ' 

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][7] == 'subscribe':
        #     have_subscribed_situation += '菲律賓 '

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][8] == 'subscribe':
        #     have_subscribed_situation += '印尼 ' 

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][9] == 'subscribe':
        #     have_subscribed_situation += '澳門 ' 

        # sql_cmd = "select * from linebot_user_situation where line_uid = '" + user_id + "'"
        # query_data = db.engine.execute(sql_cmd)
        # if list(query_data)[0][10] == 'subscribe':
        #     have_subscribed_situation += '台灣 ' 



        print(have_subscribed_situation)
        # have_subscribed_situation = 'hi'
        FlexMessage = news_card.subscribe_situation_flex_card(have_subscribed_situation,tw_sub, jp_sub , kr_sub , sin_sub , malay_sub , viet_sub , tha_sub , phi_sub , ind_sub , ma_sub)
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('訂閱現況清單',FlexMessage))
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='訂閱現況清單發生錯誤！'))

def situation_subscribe_fun(event,action,item,country): # 更改linebot_user_situation 的訂閱資料(執行SQL)
    try:
        user_id = event.source.user_id # 取得使用者的UID
        sql_cmd = "update linebot_user_situation set "+country+" = '"+action+"' where line_uid='" + user_id + "'" # 更改新聞的國家='subscribe' 或 'cancel'
        db.engine.execute(sql_cmd)
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='更改訂閱資料發生錯誤！'))

def news_subscribe_fun(event,action,item,country): # 更改linebot_user_news 的訂閱資料(執行SQL)
    try:
        user_id = event.source.user_id # 取得使用者的UID
        sql_cmd = "update linebot_user_news set "+country+" = '"+action+"' where line_uid='" + user_id + "'" # 更改新聞的國家='subscribe' 或 'cancel'
        db.engine.execute(sql_cmd)

    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='更改訂閱資料發生錯誤！'))

def auto_push_situation(): # 自動推播疫情現況
    try:
        all_country=['japan','korea','singapore','malaysia','vietnam','thailand','philippines','indonesia','macao','taiwan']
        for country in all_country:
            sql_cmd = "select * from linebot_user_situation where "+ country +" = 'subscribe'"
            query_data = db.engine.execute(sql_cmd)
            userall = list(query_data)

            sql_cmd_2 = "SELECT * FROM world_situation WHERE country = '"+ country +"' AND update_time ='" + today +"'"  # 抓出新聞
            query_data_2 = db.engine.execute(sql_cmd_2)
            situation = list(query_data_2)  
            sum = str(situation[0][1])
            day_new = str(situation[0][2])
            # million = situation[0][4]
            death = str(situation[0][4])
            vac = str(situation[0][7])

            for user in userall:  #逐一推播
                #FlexMessage = covid_country_card.covid_country_card(country,situation[0][2],situation[0][1],situation[0][4],situation[0][7])  
                FlexMessage = covid_country_card.covid_country_card(str(country), day_new, sum, death,vac)            
                line_bot_api.push_message(to=user[0], messages=[FlexSendMessage('推播每日國際疫情',FlexMessage)])  #推播訊息

    except Exception as e:
        auto_push_error_process(e,"推播每日國際疫情")
        line_bot_api.broadcast(TextSendMessage(text='推播每日國際疫情發生錯誤!!'))

def auto_push_news(): # 自動推播國際新聞
    try:
        all_country=['japan','korea','singapore','malaysia','vietnam','thailand','philippines','indonesia','macao','taiwan']

        for country in all_country:
            sql_cmd = "select * from linebot_user_news where "+ country +" = 'subscribe'"  
            query_data = db.engine.execute(sql_cmd)
            userall = list(query_data)  

            sql_cmd_2 = "SELECT * FROM world_news WHERE country = '"+ country +"' AND update_time ='" + today +"'"  # 抓出新聞
            query_data_2 = db.engine.execute(sql_cmd_2)
            news = list(query_data_2)  

            for user in userall:  #逐一推播
                print('user:'+user[0])
                FlexMessage = news_card.news_card(country, news)                
                line_bot_api.push_message(to=user[0], messages=[FlexSendMessage('推播每日國際新聞',FlexMessage)])  #推播訊息

    except Exception as e:
        auto_push_error_process(e,"推播每日國際新聞")
        line_bot_api.broadcast(TextSendMessage(text='推播每日國際新聞發生錯誤!!'))

#endregion 有關推播功能的function-------------------------------------------------------------------------

def new_user(event): # 將user_id新增至DB
    try:
        # 這邊可以執行 SQL COMMAND(抓取對方LINE UID)
        # 之後 linebot_user_news & linebot_user_situation 可以存放使用者偏好
        user_id = event.source.user_id # 取得使用者的UID
        sql_cmd = "select * from linebot_user_news where line_uid='" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if len(list(query_data)) == 0:  # 如果是新的用戶(資料庫此UID)，就INSERT一筆新資料
            sql_cmd = "insert into linebot_user_news (line_uid) values('" + user_id + "');"
            db.engine.execute(sql_cmd)

        sql_cmd = "select * from linebot_user_situation where line_uid='" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if len(list(query_data)) == 0:  # 如果是新的用戶(資料庫此UID)，就INSERT一筆新資料
            sql_cmd = "insert into linebot_user_situation (line_uid) values('" + user_id + "');"
            db.engine.execute(sql_cmd)

        sql_cmd = "select * from linebot_user_situation_temp where line_uid='" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if len(list(query_data)) == 0:  # 如果是新的用戶(資料庫此UID)，就INSERT一筆新資料
            sql_cmd = "insert into linebot_user_situation_temp (line_uid) values('" + user_id + "');"
            db.engine.execute(sql_cmd)
          
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendUse_help(event):  # 說明功能按鍵
    try:
        text_help = '''「浪疾天涯」目前提供五大功能！！\n1. 疫情現況\n2. 最新新聞\n3. 旅遊資訊\n4. 法規資訊\n5. 推播設定\n點及下方功能列表即可操作做，亦可直接透過文字或語音表達需要的服務\n\n教學影片連結：\nhttps://www.youtube.com/watch?v=FimZ15yGZw0'''
        message = TextSendMessage(
                text=text_help
            )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='功能說明發生錯誤！'))

def sendUse_covid(event):  # 疫情功能按鍵
    try:
        message = TextSendMessage(text='您想了解哪個國家的疫情呢？',
        quick_reply=QuickReply(
            items=[QuickReplyButton(action=MessageAction(
                        label="台灣", text="台灣最新現況", data='country=taiwan')),  # 對應到showTokyoSituation
                    QuickReplyButton(action=MessageAction(
                        label="日本", text="日本最新現況", data='country=japan')),  # 對應到showTokyoSituation
                    QuickReplyButton(action=MessageAction(
                        label="南韓", text="南韓最新現況", data='country=korea')),
                    QuickReplyButton(action=MessageAction(
                        label="新加坡", text="新加坡最新現況", data='country=singapore')),
                    QuickReplyButton(action=MessageAction(
                        label="馬來西亞", text="馬來西亞最新現況", data='country=malaysia')),
                    QuickReplyButton(action=MessageAction(
                        label="泰國", text="泰國最新現況", data='country=thailand')),
                    QuickReplyButton(action=MessageAction(
                        label="澳門", text="澳門最新現況", data='country=macao')),
                    QuickReplyButton(action=MessageAction(
                        label="菲律賓", text="菲律賓最新現況", data='country=philippines')),
                    QuickReplyButton(action=MessageAction(
                        label="越南", text="越南最新現況", data='country=vietnam')),
                    QuickReplyButton(action=MessageAction(
                        label="印尼", text="印尼最新現況", data='country=indonesia')),
                    ]))
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='疫情功能發生錯誤！'))
        error_process(e,event)

def sendUse_news(event):  # 新聞功能按鍵
    try:
        message = TextSendMessage(text='您想了解哪個國家的新聞呢？',
        quick_reply=QuickReply(
            items=[QuickReplyButton(action=MessageAction(
                        label="台灣", text="台灣最新新聞", data='country=taiwan')),
                    QuickReplyButton(action=MessageAction(label="日本", text="日本最新新聞", data='country=japan')),  # 對應到showTokyoSituation
                    QuickReplyButton(action=MessageAction(
                        label="南韓", text="南韓最新新聞", data='country=korea')),
                    QuickReplyButton(action=MessageAction(
                        label="新加坡", text="新加坡最新新聞", data='country=singapore')),
                    QuickReplyButton(action=MessageAction(
                        label="馬來西亞", text="馬來西亞最新新聞", data='country=malaysia')),
                    QuickReplyButton(action=MessageAction(
                        label="泰國", text="泰國最新新聞", data='country=thailand')),
                    QuickReplyButton(action=MessageAction(
                        label="澳門", text="澳門最新新聞", data='country=macao')),
                    QuickReplyButton(action=MessageAction(
                        label="菲律賓", text="菲律賓最新新聞", data='country=philippines')),
                    QuickReplyButton(action=MessageAction(
                        label="越南", text="越南最新新聞", data='country=vietnam')),
                    QuickReplyButton(action=MessageAction(
                        label="印尼", text="印尼最新新聞", data='country=indonesia')),
                    QuickReplyButton(action=MessageAction(
                        label="中國", text="中國最新新聞", data='country=china')),
                    ]))
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='新聞功能發生錯誤！'))

def sendUse_law(event):  # 法規功能按鍵
    try:
        message = TextSendMessage(text='點選你想了解的國家法規',
        quick_reply=QuickReply(
            items=[                                                                 # 對應到showTokyoSituation
                    QuickReplyButton(action=MessageAction(
                        label="日本", text="日本入境規定", data='country=japan')),  
                    QuickReplyButton(action=MessageAction(
                        label="南韓", text="南韓入境規定", data='country=korea')),
                    QuickReplyButton(action=MessageAction(
                        label="新加坡", text="新加坡入境規定", data='country=singapore')),
                    QuickReplyButton(action=MessageAction(
                        label="馬來西亞", text="馬來西亞入境規定", data='country=malaysia')),
                    QuickReplyButton(action=MessageAction(
                        label="泰國", text="泰國入境規定", data='country=thailand')),
                    QuickReplyButton(action=MessageAction(
                        label="澳門", text="澳門入境規定", data='country=macao')),
                    QuickReplyButton(action=MessageAction(
                        label="菲律賓", text="菲律賓入境規定", data='country=philippines')),
                    QuickReplyButton(action=MessageAction(
                        label="越南", text="越南入境規定", data='country=vietnam')),
                    QuickReplyButton(action=MessageAction(
                        label="印尼", text="印尼入境規定", data='country=indonesia')),
                    ]))
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='法規功能發生錯誤！'))

def sendUse_push(event):  # 推播功能按鍵
    try:
        text_help = '''請問您要關注的內容是？'''
        message = TextSendMessage(
                text=text_help
            )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='推播功能發生錯誤！'))

def sendUse_covid_pic7(event, country):  # 疫情現況：傳送趨勢圖
    try:
        if country == "日本":
            country = "japan"
        elif country == "韓國" or country == "南韓":
            country = "korea"                
        elif country == "新加坡":
            country = "singapore"
        elif country == "馬來西亞":
            country = "malaysia"
        elif country == "越南":
            country = "vietnam"
        elif country == "泰國":
            country = "thailand"
        elif country == "菲律賓":
            country = "philippines"
        elif country == "印尼":
            country = "indonesia"
        elif country == "澳門":
            country = "macao"
        elif country == "台灣" or country == "臺灣":
            country = "taiwan"

        print(country)
        sql_cmd = "SELECT * FROM covid_graph WHERE country = '" + country + "' AND release_time ='" + today + "'"
        query_data = db.engine.execute(sql_cmd)
        situation = list(query_data)

        day7_url = situation[0][1]
        
        # 傳送image必須要提供原圖與縮圖網址，兩個可相同
        originalContentUrl = day7_url
        previewImageUrl = day7_url

        line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            originalContentUrl, previewImageUrl))

    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='7日趨勢圖發生錯誤！'))

def sendUse_covid_pic30(event, country):  # 疫情現況：傳送趨勢圖
    try:

        if country == "日本":
            country = "japan"
        elif country == "韓國" or country == "南韓":
            country = "korea"                
        elif country == "新加坡":
            country = "singapore"
        elif country == "馬來西亞":
            country = "malaysia"
        elif country == "越南":
            country = "vietnam"
        elif country == "泰國":
            country = "thailand"
        elif country == "菲律賓":
            country = "philippines"
        elif country == "印尼":
            country = "indonesia"
        elif country == "澳門":
            country = "macao"
        elif country == "台灣" or country == "臺灣":
            country = "taiwan"

        print(country)
        sql_cmd = "SELECT * FROM covid_graph WHERE country = '" + country + "' AND release_time ='" + today + "'"
        query_data = db.engine.execute(sql_cmd)
        situation = list(query_data)

        day30_url = situation[0][2]
        
        # 傳送image必須要提供原圖與縮圖網址，兩個可相同
        originalContentUrl = day30_url
        previewImageUrl = day30_url

        line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            originalContentUrl, previewImageUrl))

    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='30日趨勢圖發生錯誤！'))

def sendUse_covid_country(event, country):  # 疫情現況：傳送covid_country_card
    try:
        if country == '台灣' or country == '臺灣':
            country = '台灣'
        sql_cmd = "SELECT * FROM world_situation WHERE area = '" + country + "' AND update_time ='" + today + "'"
        query_data = db.engine.execute(sql_cmd)
        situation = list(query_data)

        # 可能要修改！！！！！
        # area = situation[0][1]
        sum = str(situation[0][1])
        day_new = str(situation[0][2])
        # million = situation[0][4]
        death = str(situation[0][4])
        vac = str(situation[0][7])
        print(country, day_new, sum, death,vac)

        FlexMessage = covid_country_card.covid_country_card(str(country), day_new, sum, death,vac)
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(country+'疫情', FlexMessage))        

    except Exception as e:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=country+'疫情發生錯誤！'))   
        error_process(e,event) 

def sendUse_covid_area(event,country):
    try:
        if country == "日本":
            en_country = "japan"
        elif country == "南韓":
            en_country = "korea"
        elif country == "台灣" or country == "臺灣":
            en_country = "taiwan"

        sql_cmd = "SELECT * FROM world_situation WHERE country = '" + en_country + "' AND update_time ='" + today + "'"
        query_data = db.engine.execute(sql_cmd)
        situation = list(query_data)
        

        FlexMessage = covid_country_card.covid_area_card(str(country), situation)
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(country+'其他地區', FlexMessage))        

    except Exception as e:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=country+'其他地區發生錯誤！'))  
        error_process(e,event)  


#確認各使用者當下使用之的疫情資訊function-------------------------------------------------------------------------
def situation_temp_fun(event, country): # 更改linebot_user_situation_temp 的訂閱資料(執行SQL)
    try:
        user_id = event.source.user_id # 取得使用者的UID
        sql_cmd = "update linebot_user_situation_temp set situation_temp = '"+country+"' where line_uid='" + user_id + "'" # 更改新聞的國家='subscribe' 或 'cancel'
        db.engine.execute(sql_cmd)
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='更改situation_temp資料發生錯誤！'))

def return_situation_temp_fun(event): # 更改linebot_user_situation_temp 的訂閱資料(執行SQL)
    try:
        user_id = event.source.user_id # 取得使用者的UID
        sql_cmd = "select * from linebot_user_situation_temp where line_uid='" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        situation = list(query_data)
        return situation[0][1]
    except Exception as e:
        error_process(e,event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='回傳situation_temp資料發生錯誤！'))

def dashboard ():  # 推播每日儀表板
    try:
        sql_cmd = "select * from linebot_user_situation"
        query_data = db.engine.execute(sql_cmd)
        userall = list(query_data)

        sql_cmd = "SELECT * FROM world_situation_statistics WHERE update_time = '" + today + "' "
        query_data = db.engine.execute(sql_cmd)
        situation = list(query_data)
        imgmap_msg = image_map.senduse_image_map(situation[0][5], situation[0][0], situation[0][1], situation[0][2], situation[0][3])   
       
        for user in userall:  #逐一推播          
            line_bot_api.push_message(to=user[0], messages=imgmap_msg)  #推播訊息

    except Exception as e:
        auto_push_error_process(e,"推播每日國際疫情")
        line_bot_api.broadcast(TextSendMessage(text='推播每日國際疫情發生錯誤!!'))

#AZURE_語音辨識之function-------------------------------------------------------------------------
# def STT():
#     #先config
#     speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language='zh-tw')
#     #創建分辨器
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config = speech_config)
#     result = speech_recognizer.recognize_once()

#     if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         print("Recognized: {}".format(result.text))
#         return result.text
#     elif result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(result.no_match_details))
#     elif result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))

def trans_m4a_to_wav(filepath, out_name):       #把line接接收到的audio由m4a轉檔為wva，trans_m4a_to_wav(檔案路徑, 輸出檔案名稱)
    # print("我還活著")
    AudioSegment.converter = 'D://ffmpeg-N-104005-g2761a7403b-win64-gpl//bin//ffmpeg.exe'
    with open(filepath,'rb') as f:
        song = AudioSegment.from_file(f,format='m4a')
        song.export(out_name + ".wav", format="wav")

def speech_recognizer(filename_path):
    speech_config = speechsdk.SpeechConfig(subscription="8e620401f2ba40099233671f7e8bd081", region="southeastasia", speech_recognition_language='zh-tw')
    audio_input = speechsdk.AudioConfig(filename=filename_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)  
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    return result.text
    
