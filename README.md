# LineBot_final
NCYU MIS final project, documents is released 2021/11/09.
- line_bot_main為主程式之各項功能存資料夾，其中line_bot_Luis(main).py 為主程式，串接起line後端與使用者互動之各項功能
- crawler_world_news (foreign)、crawler_world_situation、country_crawler資料夾中分別存放負責各國疫情即時資訊、疫情相關新聞以及各國出入境法規的爬蟲程式碼
- covid_graph 主要透過爬取得的疫情資料進行趨勢繪圖
- imagemap 為line聊天室中一功能，透過爬取得的疫情資料統計出上升、下降、疫苗覆蓋率、今日新增做多國家等資訊，並繪製為line所能接受之圖片格式
