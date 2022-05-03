# xlsx 匯入 pgadmin參考: http://tw.gitbook.net/postgresql/2013080998.html
# Pandas應用: https://www.learncodewithmike.com/2020/12/read-excel-file-using-pandas.html
# 排程器設定: https://zh-tw.coderbridge.com/@JohnnyFoxChang/5ea14379cd974b78a69d41e87d10dcde

我把各個國家的爬蟲程式拆成不同檔案，並用國家英文名去命名 ex.japan.py
執行單爬蟲程式時預設會將爬下來資料存於文字文件 ex.japan.txt
現在是將各個國家的爬蟲程整合進daycall.py，執行daycall.py可以一次互叫全部爬蟲程式並執行，並將全部資料整合存於excel之中，aycall.py會自動新建一個呼叫當下日期的xlsx ex.2021-04-29.xlsx
