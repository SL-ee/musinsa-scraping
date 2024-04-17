from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# list 선언
goods_name_list = []
goods_link_list = []

# item /001: 상의, /002: 아우터, /003: 바지
# sort pop_category: 무신사 추천순, new: 신상품 입고순, emt_high: 후기순
# ex_soldout Y: 품절 포함, N: 품절 포함하지 않음

for page in range(1, 10):
    time.sleep(0.2)
    url = 'https://www.musinsa.com/categories/item/003?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page='+str(page)+'&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=N&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
    result = requests.get(url, headers=request_headers)
    soup = BeautifulSoup(result.text, "lxml")

    section = soup.find("div", attrs={'class': 'section_product_list'}).find('ul', attrs={'id': 'searchList'})
    goods_list = section.find_all('li', attrs={'class': 'li_box'})


    for goods in goods_list:
        goods_each = goods.find('div', attrs={'class': 'article_info'}).find('p', attrs={'class': 'list_info'})
        goods_link = goods_each.find('a', attrs={'name': 'goods_link'})['href']
        goods_link_list.append(goods_link)
        goods_name = goods_each.text.strip()
        goods_name_list.append(goods_name)


excel = pd.DataFrame(
    {
        '제품명': goods_name_list,
        '링크': goods_link_list
    })

print(excel)
excel.to_excel("./제품명_top_pop.xlsx", header=True, index=False)
