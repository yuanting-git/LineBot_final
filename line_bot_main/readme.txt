flask server：
py -m pip install Flask
---------------------------------------------------------------------------------
linebot api & pgadmin4 的參數 可以去 need_to_modify.py 修改
我把有關旅遊的function整理到travel_functions(tf)
其他的function都丟到line_bot_functions(lbf.)
---------------------------------------------------------------------------------
終止運行：
Ctrl+C
---------------------------------------------------------------------------------
line_bot sdk：
py -m pip install line-bot-sdk
---------------------------------------------------------------------------------
ngrok操作:
先去cmd到linebot程式的資料夾
輸入ngrok http 5000 -host-header="localhost:5000"
複製cmd上的forwarding的網址
要去line developer的Messaging API settings的Webhook settings修改URL
再去vs執行 程式

連線至本機檔案:
omagemap:ngrok http "file:///C:\Users\yuanting\Desktop\0817\imagemap\image_map_pic"
---------------------------------------------------------------------------------
pgadmin:
1. create db
2. create table
3. create column
4. column -> definition -> data type 選 character varyin
---------------------------------------------------------------------------------
檔案說明：
line_bot_Luis.py為主程式，若要啟動line bot請執行這個，所有功能判斷都在這個程式
country_card.py、news_card.py分別為疫情、新聞flexmessage的檔案
其他都不太重要：)
---------------------------------------------------------------------------------
注意事項:
1. pgadmin內的命名可能不一樣
2. table中的column順序不一樣，因此針對select完操作situation[][]對應的值應該也不一樣，在line_bot_Luis.py、news_card.py搜尋「#可能要修改！！！！！」即可到該位置做修改
3. 疫情的資訊是透過日期去DB撈資料，若要正常運行需要當日的最新資料
