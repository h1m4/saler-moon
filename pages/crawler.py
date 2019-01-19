from bs4 import BeautifulSoup
import requests as rq

res = rq.get('http://www.oliveyoung.co.kr/store/main/getSaleList.do')
page_path = '?pageIdx=2%d'
page = 2
res.encoding = 'utf-8'

# 페이지를 넘어가면서 모든 정보를 크롤링
soup = BeautifulSoup(res.text, 'lxml')
#posts = soup.select('body div.sale-area div.TabsConts.on ul li div.prd_info')
listname = soup.select('.tx_name')
listprice = soup.select('.tx_cur')

for i, j in enumerate(listname, 1):
    print(i, j.text.strip(), listprice[i-1].text.strip())
