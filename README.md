# python-scrapy
利用python scrapy 抓取蘋果新聞實現多網頁網路爬蟲，並可將爬取資料存成json檔案或是存取至sqlite
## sqlite 擷取頁面
![](./img/sqlite.png)

### 執行專案
```
$ scrapy crawl apple
```
### 輸出json檔案
```
$ scrapy crawl apple -o apple.json -t json
```
