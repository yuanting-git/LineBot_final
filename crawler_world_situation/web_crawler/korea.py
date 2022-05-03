def kor(t):
    import urllib.request as req
    url="http://ncov.mohw.go.kr/cn/bdBoardList.do?brdId=26&brdGubun=262&dataGubun=&ncvContSeq=&contSeq=&board_id="
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
            
    import bs4

    root=bs4.BeautifulSoup(data,"html.parser")

    dis = root.find_all('tbody')

    for d in dis:
        name=d.find_all(name='th',attrs={"scope":"row"})
        sum=d.find_all(name='td',attrs={"headers":"status_con s_type1"})
        new=d.find_all(name='td',attrs={"headers":"status_level l_type1"})
        death=d.find_all(name='td',attrs={"headers":"status_con s_type4"})

    # 寫入到檔案
    fp1 = open("./situation_txt/korea.txt", "w+",encoding="utf8")
    for i in range(19):
        if name[i].get_text() == "合计":
            name[i] = "南韓"
            fp1.write(name[i])
            fp1.write('\n')
            fp1.write(sum[i].get_text())
            fp1.write('\n')
            fp1.write(new[i].get_text())
            fp1.write('\n')
            fp1.write('\n')
            fp1.write('\n')
            fp1.write(death[i].get_text())
            fp1.write('\n')  
            url = "https://news.google.com/covid19/map?hl=zh-TW&mid=%2Fm%2F06qd3&gl=TW&ceid=TW%3Azh-Hant&state=4"
            request = req.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            })
            with req.urlopen(request) as response:
                data = response.read().decode("utf-8")


            root = bs4.BeautifulSoup(data, "html.parser")

            vac = root.find_all('tr', class_="sgXwHf wdLSAe ROuVee")

            for v in vac:
                num=v.find_all('td',class_="l3HOY")
                for n in num:
                    if '%' in n.get_text():
                        fp1.write(n.get_text())
                        fp1.write('\n')  
        else:
            fp1.write(name[i].get_text())
            fp1.write('\n')
            fp1.write(sum[i].get_text())
            fp1.write('\n')
            fp1.write(new[i].get_text())
            fp1.write('\n')
            fp1.write('\n')
            fp1.write('\n')
            fp1.write(death[i].get_text())
            fp1.write('\n')     

    

    # 關閉檔案
    fp1.close()