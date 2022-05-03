# xlsx 匯入 pgadmin參考: http://tw.gitbook.net/postgresql/2013080998.html
# Pandas應用: https://www.learncodewithmike.com/2020/12/read-excel-file-using-pandas.html
# 排程器設定: https://zh-tw.coderbridge.com/@JohnnyFoxChang/5ea14379cd974b78a69d41e87d10dcde
import pandas as pd
import psycopg2
import time
import pgadmin4 as pg
 

def topgaadmin() :

    # 連線至 pgmin 的資料 
    # 本機端的 SQL Server
    ###########################################下面這行要改(去pgadmin4.py改)########################################
    conn = psycopg2.connect(database = pg.database, user = pg.user, password = pg.password, host =pg.host, port = pg.port)
    # Heroku Postgre SQL Server(線上版資料庫)
    # conn = psycopg2.connect('postgres://dtylmlhpkbhatn:1acbc25080c71538681a73284fcce77853e6d01709e7551f06f0a2ab05895594@ec2-34-193-112-164.compute-1.amazonaws.com:5432/d8lr0jqds8s2mj')
    print ("Opened database successfully")

    t= time.strftime("%Y-%m-%d", time.localtime())
    # file = t + ' news'


    all_country=['japan','korea','singapore','malaysia','vietnam','thailand','philippines','indonesia','macao','taiwan']

    for country in all_country:

        df=pd.read_excel("./news_xlsx/" + t +" news.xlsx", sheet_name= country) # 讀取不同國家的sheet
        total_rows = (len(df.index)) # 存儲這個國家的新聞比數 給迴圈用 

        for r in range(total_rows):
                title = df.iat[r, 0]
                content = df.iat[r, 1]
                release_time = df.iat[r, 2]
                url = df.iat[r, 3]
                img_url = df.iat[r, 4]
 
                cur = conn.cursor()
                cur.execute("INSERT INTO world_news (title, content, release_time, url, img_url, country, update_time) VALUES (%s, %s, %s,%s,%s,%s,%s)", (title,content,release_time,url,img_url,country,t))
                conn.commit()

                print ("News Records created successfully")
    conn.close()
                
topgaadmin()                 


