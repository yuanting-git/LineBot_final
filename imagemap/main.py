import time
import txt_to_xlsx

today= time.strftime("%Y-%m-%d", time.localtime())
txt_to_xlsx.write_excel(today)
