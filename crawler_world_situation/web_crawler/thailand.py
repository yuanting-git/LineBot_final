def thai(t):
    import urllib.request as req
    url="https://news.google.com/covid19/map?hl=zh-TW&mid=%2Fm%2F07f1x&gl=TW&ceid=TW%3Azh-Hant"
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
        
    import bs4

    root=bs4.BeautifulSoup(data,"html.parser")

    dis = root.find_all('tr',class_="sgXwHf wdLSAe ROuVee")

    # 寫入到檔案
    fp1 = open("./situation_txt/thailand.txt", "w+",encoding="utf8")
    #fp1.write(t)
    #fp1.write('\n')
    for d in dis:
        name=d.find('div',class_="pcAJd").get_text()
        fp1.write(name)
        fp1.write('\n')
        num=d.find_all('td',class_="l3HOY")
        for n in num:
            if n!=" ":
                fp1.write(n.get_text())
                fp1.write('\n')

    url = "https://news.google.com/covid19/map?hl=zh-TW&mid=%2Fm%2F07f1x&gl=TW&ceid=TW%3Azh-Hant&state=4"
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

    # 關閉檔案
    fp1.close()
