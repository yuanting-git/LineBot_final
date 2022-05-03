import pgadmin4 as pg
import pandas as pd
import psycopg2
import time
 

def topgaadmin() :

    # 連線至 pgmin 的資料 
    # 本機端的 SQL Server
    ###########################################下面這行要改########################################
    conn = psycopg2.connect(database = pg.database, user = pg.user, password = pg.password, host = pg.host, port = pg.port)
    # Heroku Postgre SQL Server
    # conn = psycopg2.connect('postgres://dtylmlhpkbhatn:1acbc25080c71538681a73284fcce77853e6d01709e7551f06f0a2ab05895594@ec2-34-193-112-164.compute-1.amazonaws.com:5432/d8lr0jqds8s2mj')
    print ("Opened database successfully")

    t= time.strftime("%Y-%m-%d", time.localtime())
    # file = t + ' news'


    df=pd.read_excel('./image_map_xlsx/'+t+".xlsx", sheet_name= 'imagemap')


    total_rows = (len(df.index)) # 存儲這個國家的新聞比數 給迴圈用 

    for r in range(total_rows):               
        country_1 = df.iat[r, 0].replace('\n','')
        country_2 = df.iat[r, 1].replace('\n','')
        country_3 = df.iat[r, 2].replace('\n','')
        country_4 = df.iat[r, 3].replace('\n','')

    cur = conn.cursor()
    cur.execute("INSERT INTO world_situation_statistics (top_daynew, top_sum, max_slope, min_slope, update_time) VALUES (%s,%s,%s,%s,%s)", (country_1,country_2,country_3,country_4,t))
    conn.commit()

    print ("News Records created successfully")
    conn.close()
                
topgaadmin()                 


