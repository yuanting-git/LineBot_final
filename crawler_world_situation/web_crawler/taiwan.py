def tai(t):
    import urllib.request as req
    url="https://news.google.com/covid19/map?hl=zh-TW&mid=/m/06f32&gl=TW&ceid=TW:zh-Hant"
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
        
    import bs4

    root=bs4.BeautifulSoup(data,"html.parser")
    
    dis = root.find_all('tr',class_="sgXwHf wdLSAe ROuVee")

    # 寫入到檔案
    fp1 = open("./situation_txt/taiwan.txt", "w+",encoding="utf8")
    for d in dis:
        name=d.find('div',class_="pcAJd").get_text()
        fp1.write(name)
        fp1.write('\n')
        num=d.find_all('td',class_="l3HOY")
        for n in num:
            fp1.write(n.get_text())
            fp1.write('\n')
    
    url = "https://news.google.com/covid19/map?hl=zh-TW&mid=%2Fm%2F06f32&gl=TW&ceid=TW%3Azh-Hant&state=4"
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

    # 台灣各縣市新增
    url = "https://covid-19.nchc.org.tw/"
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    city_dis = root.find_all('a', class_="btn btn-success btn-lg")

    for d in city_dis:
        city_name = d.find(name = 'span', attrs = {"style":"font-size: 1em;"})
        city_name = city_name.get_text()
        city_name_2 = city_name.split('+')
        city_name = city_name_2[0]
        name = city_name[0:3]
        sum = city_name[4:]
        fp1.write(name)
        fp1.write('\n')
        fp1.write(sum)
        fp1.write('\n')
        try:
            day_new = city_name_2[1]       
            fp1.write(day_new)
            fp1.write('\n')
            fp1.write('0')
            fp1.write('\n')
            fp1.write('0')
            fp1.write('\n')
        except:
            fp1.write('0')
            fp1.write('\n')
            fp1.write('\n')
            fp1.write('0')
            fp1.write('\n')
            fp1.write('0')
            fp1.write('\n')
    fp1.close()

