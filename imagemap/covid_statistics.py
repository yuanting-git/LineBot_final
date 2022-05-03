from flask_sqlalchemy import SQLAlchemy
import datetime
from flask import Flask
from urllib.parse import parse_qsl
import pgadmin4 as pg


#endregion

app = Flask(__name__)

#region 各式連線參數
# 不知道為啥要加這行
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# PostgreSQL Connection
app.config['SQLALCHEMY_DATABASE_URI'] ='' + pg.Server + '://' + pg.user + ':'+ pg.password + '@127.0.0.1:5432/' + pg.database + ''
db = SQLAlchemy(app)

# 處理今天日期
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")  # 轉換為指定的格式 YYYY-MM-DD

#1. 今日新增最多國家
sql_cmd_1 = "SELECT * FROM world_situation WHERE day_new = (SELECT MAX(day_new) FROM world_situation WHERE update_time='" + today + "')"
query_data_1 = db.engine.execute(sql_cmd_1)
situation_1 = list(query_data_1)

#2. 染疫人數最多國家
sql_cmd_2 = "SELECT * FROM world_situation WHERE sum = (SELECT MAX(sum) FROM world_situation WHERE update_time='" + today + "')"
query_data_2 = db.engine.execute(sql_cmd_2)
situation_2 = list(query_data_2)

#3. 近7日新增最快國家
sql_cmd_3 = "SELECT * FROM world_situation WHERE update_time='" + today + "'"
query_data_3 = db.engine.execute(sql_cmd_3)
situation_3 = list(query_data_3)

#4. 近7日下降最快國家(不一定是7日可於下方修改)
minus_day = 7   #扣幾日修改處
minus_today = datetime.datetime.today()
minus_today -= datetime.timedelta(days=minus_day)
print(minus_today.strftime("%Y-%m-%d"))

sql_cmd_4 = "SELECT * FROM world_situation WHERE update_time='" + str(minus_today.strftime("%Y-%m-%d")) + "'"
query_data_4 = db.engine.execute(sql_cmd_4)
situation_4 = list(query_data_4)
#print(situation_4[0][0])
#print(situation_4[0][6])

slope = []
for i in range(len(situation_4)):
    #print(situation_3[i][2])
    #print(situation_4[i][2])
    slope.append((situation_3[i][2] - situation_4[i][2])/7)
slope_max = max(slope)
slope_min = min(slope)

#5. 疫苗施打普及率最高之國家
sql_cmd_5 = "SELECT * FROM world_situation WHERE vaccine = (SELECT MAX(vaccine) FROM world_situation WHERE update_time='" + today + "')"
query_data_5 = db.engine.execute(sql_cmd_5)
situation_5 = list(query_data_5)

#儀錶板統計結果之國家1~4
country_1 = situation_1[0][5]                           #今日新增最多國家
country_2 = situation_2[0][5]                           #累計染疫人數最多國家
country_3 = situation_3[slope.index(slope_max)][5]      #近7日新增最快國家
country_4 = situation_3[slope.index(slope_min)][5]      #近7日下降最快國家
country_5 = situation_5[0][5]                           #疫苗施打普及率最高之國家

#print(country_1)
#print(country_2)
print("slope_max:",slope_max,"index:",slope.index(slope_max),"country:",situation_3[slope.index(slope_max)][5])
print("slope_min:",slope_min,"index:",slope.index(slope_min),"country:",situation_3[slope.index(slope_min)][5])

# 寫入到檔案
fp1 = open("./image_map_txt/"+today+".txt", "w+",encoding="utf8")
fp1.write(country_1)
fp1.write('\n')
fp1.write(country_5) #累計染疫人數最多國家更改為疫苗施打普及率最高之國家
fp1.write('\n')
fp1.write(country_3)
fp1.write('\n')
fp1.write(country_4)

# 關閉檔案
fp1.close()