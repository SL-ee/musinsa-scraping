# musinsa-scraping
의류 쇼핑몰 무신사를 스크래핑하는 파이썬 코드

1. getLinks.py를 사용해 제품 링크를 스크래핑합니다.
   검색 조건을 바꾸려면 url을 조건에 맞게 수정해야 합니다.

   ex. url = 'https://www.musinsa.com/categories/item/001?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=N&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
   --> 상의 카테고리(item/001), 무신사 추천순(sort=pop_category), 1페이지(page=1), 품절 불포함(ex_soldout=N)

2. getDetail.py를 사용해 제품 링크에서 제품 사이즈표, 리뷰를 스크래핑합니다.

   사이즈표 형식이 다양하기 때문에 데이터가 정확히 들어갔는지 반드시 확인해야 합니다.
