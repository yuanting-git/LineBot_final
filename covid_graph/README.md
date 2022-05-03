# 圖表檔案注意
`python環境：3.9.0`

## 開CMD下載
`pip install xlrd == 1.2.0`
這個很重要，版本錯誤會有問題，如果版本太新先解安裝`pip uninstall xlrd`
###畫圖的
`pip install matplotlib`
###上傳圖片的
`pip install pyimgur`

## 需修改之變數
+ `COVID_data_path = 'C:/Users/xxxxxx/Desktop/疫情資料/'`
  改成你的疫情資料存放地點~~~ // line 39

- - -

# 中文化
#### 請進去 '中文化資料夾' 
#### 你可以先用 `CHECK_FONT.py`檔案，確定你的MATPLOTLIB內有沒有中文字型
(還是其實你看不出來誰是中文字型
+ 如果你知道你認的出來誰是中文字型，你把列出來的中文字型其中一個複製，line-90 和 line-160
+ `plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] `
+ 改後面的'Taipei Sans TC Beta'，改成你複製的中文字型

### 1.你需要中文字形

### 2.找到你的matplotlib資料夾，可以直接開`font_set.py`，程式碼寫在裡面惹


`import matplotlib`

`print(matplotlib.__file__)`

+ 會看到這樣的訊息啦C:\Users\XXXXX\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\__init__.py

+ C:...\matplotlib\mpl-data\fonts\ttf，進去裡面把我給的ttf丟進去

### 3.用 `CHECK_FONT.py`檔案，確定你的MATPLOTLIB內有沒有中文字型`Taipei Sans TC Beta`
### 4.有了的話就可以運行惹
### 5.不行的話，刪除matplotlib的快取檔案
+ 到 `C:\Users\你電腦的名字\.matplotlib` 去刪除快取檔案`fontList.json`)`
+ 重新執行`import matplotlib` or 你直接執行看看`CHECK_FONT.py`檔案
- - -




#下面不用看ㄎㄎ
## 7天
### 變數設定
+   country：設定國家，預設'korea'
+   time_x：X軸的時間標題，預設為空的list
+   day_new_number：Y軸的數值，預設為空的list
+   today：開始的日期，看是要直接取當天日期，或是要傳值進去，我兩個方法都有提供可以選擇一下。預設為'2021-06-20'
+   position：填寫存那些excel檔案的資料夾，預設'C:/Users/restr/Desktop/tesr/plot7.png'，目前我的電腦位置，要改成你的放置位置
+   sum_number：此為暫時存取表中數值，此行可控制要選擇的行列，現在預設`booksheet.cell_value(1,2)`，為新增病例人數。
+   filename：檔案存取位置，及檔名目前直接命名，檔名部分可能要處理一下，如果照這個方法會直接替代。

![7天](https://i.imgur.com/hD0qzyi.png)

- - -
## 30天
### 變數設定
+   country：設定國家，預設'korea'
+   **time_x**：**所有**時間標題，預設為空的list
+   **time_real_x**：X軸**實際**要在圖表上的標
+   day_new_number：Y軸的數值，預設為空的list
+   today：開始的日期，看是要直接取當天日期，或是要傳值進去，我兩個方法都有提供可以選擇一下。
+   position：填寫存那些excel檔案的資料夾，預設'C:/Users/restr/Desktop/tesr/plot7.png'，目前我的電腦位置，要改成你的放置位置
+   sum_number：此為暫時存取表中數值，此行可控制要選擇的行列，現在預設`booksheet.cell_value(1,2)`，為新增病例人數。
+   filename：檔案存取位置，及檔名目前直接命名，檔名部分可能要處理一下，如果照這個方法會直接替代。


![30天](https://i.imgur.com/IlLy4QV.png)

- - -
#上傳imgur

##python環境
pip3 install imgurpython
pip install pyimgur

##imgur環境
帳號：mis981124@gmail.com
密碼：mis1234567

Client ID:2f3efd9148b1935
Client secret:a0028ca90abefc0ac1baab13222799786e9b0971

Access token:  56c57435eb613b6b5e0a6d1248bd5f39e0f37bae
Refresh token: c001083ca3afe60ff2b4b6a53ad8501090afa811