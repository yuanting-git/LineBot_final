import time
import openpyxl
import txt_to_xlsx
from web_crawler.indonesia import indo
from web_crawler.japan import jap
from web_crawler.korea import kor      
from web_crawler.macao import mac
from web_crawler.malaysia import mala
from web_crawler.philippines import phili
from web_crawler.singapore import singa
from web_crawler.thailand import thai
from web_crawler.vietnam import viet
from web_crawler.taiwan import tai


t= time.strftime("%Y-%m-%d", time.localtime())

print("Crawling...")

indo(t)
jap(t)
kor(t)        
mac(t)
mala(t)
phili(t)
singa(t)
thai(t)
viet(t)
tai(t)


# 建立一個工作簿 (存成 .xlsx)
workbook = openpyxl.Workbook()
workbook.save('./situation_xlsx/'+t+'.xlsx')


#將爬回來的資料整理進excel(.txt --> .xlsx)
txt_to_xlsx.write_excel("indonesia",t)
txt_to_xlsx.write_excel("japan",t)
txt_to_xlsx.write_excel("korea",t)
txt_to_xlsx.write_excel("macao",t)
txt_to_xlsx.write_excel("malaysia",t)
txt_to_xlsx.write_excel("philippines",t)
txt_to_xlsx.write_excel("singapore",t)
txt_to_xlsx.write_excel("thailand",t)
txt_to_xlsx.write_excel("vietnam",t)
txt_to_xlsx.write_excel("taiwan",t)
print("Data is already written to the excel !!")