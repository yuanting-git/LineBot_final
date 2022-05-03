
import urllib.request as req
import bs4

# 台灣各縣市新增
url = "https://covid-19.nchc.org.tw/"
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")

city_dis = root.find_all('a', class_="btn btn-success btn-lg")

fp1 = open("taiwan.txt", "w+", encoding="utf8")
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
