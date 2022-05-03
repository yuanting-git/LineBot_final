from flask_sqlalchemy import SQLAlchemy
import merge_image
import pyimgur
import psycopg2
from flask import Flask
from urllib.parse import parse_qsl
import pgadmin4 as pg
import datetime

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

sql_cmd = "SELECT * FROM world_situation_statistics WHERE update_time='" + today + "'"
query_data = db.engine.execute(sql_cmd)
situation = list(query_data)

print(situation[0][0],situation[0][1],situation[0][2],situation[0][3])
path_1 = './image/' + situation[0][0] + "_1.png"
path_2 = './image/' + situation[0][1] + "_2.png"
path_3 = './image/' + situation[0][2] + "_3.png"
path_4 = './image/' + situation[0][3] + "_4.png"

merge_image.merge_4(path_1,path_2,path_3,path_4,700)

def upload_to_imgur(path):

    CLIENT_ID = "2f3efd9148b1935"
    PATH = path

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")

    return uploaded_image.link  # 回傳url連結

#image_path為合成後相片儲存位置
today = datetime.datetime.today().strftime("%Y-%m-%d")
image_path = './image_map_pic/four_merged_' + today +'.png' 
img_url = upload_to_imgur(image_path)    
print(img_url)

#
conn = psycopg2.connect(database = pg.database, user = pg.user, password = pg.password, host = pg.host, port = pg.port)
print ("Opened database successfully")

cur = conn.cursor()
print ("Connect database successfully")
cur.execute("UPDATE world_situation_statistics SET url = '" + img_url + "' WHERE update_time = '" + today +"'")
conn.commit()

print ("News Records created successfully")
conn.close()
