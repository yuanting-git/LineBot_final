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

    # t= time.strftime("%Y-%m-%d", time.localtime())
    t='2021-11-08'
    # file = t + ' news'


    all_country=['taiwan','japan','korea','singapore','malaysia','vietnam','thailand','philippines','indonesia','macao']

    for country in all_country:

        df=pd.read_excel('./situation_xlsx/'+t+'.xlsx', sheet_name= country)


        total_rows = (len(df.index)) # 存儲這個國家的新聞比數 給迴圈用 

        for r in range(total_rows):
                int_vac = ''
                area = df.iat[r, 0].replace('\n','')
                sum = str(df.iat[r, 1]).replace(',','') # 取代掉數字中的逗號
                day_new = str(df.iat[r, 2]).replace(',','')
                million = str(df.iat[r,3]).replace(',','').replace('\n','')
                death = str(df.iat[r,4]).replace(',','').replace('\n','')
                vaccine = str(df.iat[r,5])


                try:
                    sum = int(sum) 
                except:
                    sum = 0 

                try:
                    day_new = int(day_new) 
                except:
                    day_new = 0 
                
                try:
                    million = int(million) 
                except:
                    million = 0 

                try:
                    death = int(death) 
                except:
                    death = 0 

                try:
                    for i in range(len(vaccine)):
                        if vaccine[i] == "一":
                            int_vac += "1"
                        if vaccine[i] == "二":
                            int_vac += "2"
                        if vaccine[i] == "三":
                            int_vac += "3"
                        if vaccine[i] == "四":
                            int_vac += "4"
                        if vaccine[i] == "五":
                            int_vac += "5"
                        if vaccine[i] == "六":
                            int_vac += "6"
                        if vaccine[i] == "七":
                            int_vac += "7"
                        if vaccine[i] == "八":
                            int_vac += "8"
                        if vaccine[i] == "九":
                            int_vac += "9"
                        if vaccine[i] == "〇":
                            int_vac += "0"
                        if vaccine[i] == ".":
                            int_vac += "."
                    
                    int_vac=float(int_vac)
                except:
                    int_vac = 0

                cur = conn.cursor()
                cur.execute("INSERT INTO world_situation (area, sum, day_new, million, death, vaccine , update_time, country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (area,sum,day_new,million,death,int_vac,t,country))
                conn.commit()

                print ("News Records created successfully")
    conn.close()
                
topgaadmin()                 


