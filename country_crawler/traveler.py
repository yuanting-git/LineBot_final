from flask import Flask, render_template
from traveldata import openWB, updatetime
#先執行traveldata在執行這個檔案
app = Flask(__name__)

@app.route("/")
def home():
	return "hi~this is flask"

@app.route("/<country>")
def root(country):
    # 將國家名稱傳入test.py中的openWB(select_country)，同時傳入更新時間～
    #headers = {'Content-Type':'text/xml;charset=utf-8'}
    #return make_response(render_template("travel_"+country+"test.html",user_template=openWB(country),updatetime=updatetime()),200,headers)
    return render_template("travel_"+country+".html",user_template=openWB(country))

if __name__ == "__main__":
	app.run(debug=True)
	
