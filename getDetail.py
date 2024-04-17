from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# 제품 아이디 리스트(id_list: 사이즈표, id_list_3: 리뷰)
id_list = []
id_list_3 = []

# 제품명 리스트
title_list = []
title_list_3 = []

# 성별 리스트
gender_list = []
gender_list_3 = []

# 링크 리스트
link_list = []
link_list_3 = []

# 사이즈표
size_list = []
gender = ''
length = []
shoulder = []
chest = []
arm = []
# 상의
size_info = {'총장': length, '어깨너비': shoulder, '가슴단면': chest, '소매길이': arm}

# 리뷰
review_list = []
how_size_list = []
comment_list = []

excel = pd.read_excel("./제품명_top_pop.xlsx")

url_list = excel['링크'][:10]

# chrome 띄우지 않음
options = ChromeOptions()
options.add_argument('-headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

for url in url_list:
    browser.get('https:'+url)
    try:
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-detail__sc-8631sn-1"))
        )
    except:
        continue
        
        
    soup = BeautifulSoup(browser.page_source, "lxml")
    
    print(url)
    
    right = soup.find('div', attrs={'class': 'product-detail__sc-8631sn-0'})
    
    # 제품명
    pro_title = soup.find('div', attrs={'class': 'product-detail__sc-1klhlce-0'}).find('h3', attrs={'class': 'product-detail__sc-1klhlce-3'}).text.strip()
    
    # 성별
    for_check = soup.find('div', attrs={'class': 'product-detail__sc-achptn-0'}).find('ul',attrs={'class': 'product-detail__sc-achptn-1'}).find_all('li', attrs={'class': 'product-detail__sc-achptn-2'})
    for check in for_check:
        if '성별' in check.find('div', attrs={'class': 'product-detail__sc-achptn-5'}).text:
            if '시즌' in check.find('div', attrs={'class': 'product-detail__sc-achptn-5'}).text:
                gender = check.find('div', attrs={'class': 'product-detail__sc-achptn-6'}).find_all('span', attrs={'class': 'product-detail__sc-achptn-4'})[1].text
            else:
                gender = check.find('div', attrs={'class': 'product-detail__sc-achptn-6'}).find('span', attrs={'class': 'product-detail__sc-achptn-4'}).text
    
    # 사이즈표
    table = soup.find('table', attrs={'class': 'product-detail__sc-swak4b-3'})
    if table:
        thead = table.find('thead')
        thead_list = thead.find_all('td', attrs={'class': 'product-detail__sc-swak4b-5'})

        tbody = table.find('tbody')
        tbody_tr = tbody.find_all('tr', attrs={"class": 'product-detail__sc-swak4b-7'})[1:]

        for i, tr in enumerate(tbody_tr):
            number_list = tr.find_all('td', attrs={'class': 'product-detail__sc-swak4b-9'})

            # 사이즈표 구성이 다른 경우를 대비
            if len(number_list)==4:
                for k, td in enumerate(number_list):
                    size_info[thead_list[k].text].append(td.text)
            elif len(number_list)==3:
                keep_name = []
                for k, td in enumerate(number_list):
                    size_info[thead_list[k].text].append(td.text)
                    keep_name.append(thead_list[k].text)
                if '총장' not in thead_list and '총장' not in keep_name:
                    length.append('없음')
                if '어깨너비' not in thead_list and '어깨너비' not in keep_name:
                    shoulder.append('없음')
                if '가슴단면' not in thead_list and '가슴단면' not in keep_name:
                    chest.append('없음')
                if '소매길이' not in thead_list and '소매길이' not in keep_name:
                    arm.append('없음')
            elif len(number_list)==2:
                keep_name = []
                for k, td in enumerate(number_list):
                    size_info[thead_list[k].text].append(td.text)
                    keep_name.append(thead_list[k].text)
                if '총장' not in thead_list and '총장' not in keep_name:
                    length.append('없음')
                if '어깨너비' not in thead_list and '어깨너비' not in keep_name:
                    shoulder.append('없음')
                if '가슴단면' not in thead_list and '가슴단면' not in keep_name:
                    chest.append('없음')
                if '소매길이' not in thead_list and '소매길이' not in keep_name:
                    arm.append('없음')
            elif len(number_list)==1:
                keep_name = []
                for k, td in enumerate(number_list):
                    size_info[thead_list[k].text].append(td.text)
                    keep_name.append(thead_list[k].text)
                if '총장' not in thead_list and '총장' not in keep_name:
                    length.append('없음')
                if '어깨너비' not in thead_list and '어깨너비' not in keep_name:
                    shoulder.append('없음')
                if '가슴단면' not in thead_list and '가슴단면' not in keep_name:
                    chest.append('없음')
                if '소매길이' not in thead_list and '소매길이' not in keep_name:
                    arm.append('없음')
                
            size_list.append(tr.find('th', attrs={'class': 'product-detail__sc-swak4b-8'}).text)
            title_list.append(pro_title)
            id_list.append(url.replace('https://www.musinsa.com/app/goods/', ''))
            gender_list.append(gender)
            link_list.append(url)
    else:
        size_list.append('없음')
        length.append('없음')
        shoulder.append('없음')
        chest.append('없음')
        arm.append('없음')
        title_list.append(pro_title)
        id_list.append(url.replace('https://www.musinsa.com/app/goods/', ''))
        gender_list.append(gender)
        link_list.append(url)
    
    # 리뷰
    reviews = soup.find('div', attrs={'id': 'reviewListFragment'}).find_all('div', attrs={'class': 'review-list'})
    for rv in reviews:
        review_profile_info = rv.find('div', attrs={'class': 'review-profile'}).find('div', attrs={'class': 'review-profile__information'})
        if review_profile_info.find('p'):
            review_list.append(review_profile_info.find('p').text)
        else:
            review_list.append('없음')
        if rv.find('ul', attrs={'class': 'review-evaluation--type3__list'}):
            how_size_list.append(rv.find('ul', attrs={'class': 'review-evaluation--type3__list'}).find_all('li')[0].text)
        else:
            how_size_list.append('없음')
        comment_list.append(rv.find('div', attrs={'class': 'review-contents'}).find('div', attrs={'class': 'review-contents__text'}).text)
        title_list_3.append(pro_title)
        id_list_3.append(url.replace('//www.musinsa.com/app/goods/', ''))
        gender_list_3.append(gender)
        link_list_3.append(url)

excel = pd.DataFrame(
    {
        '아이디': id_list,
        '제품명': title_list,
        '성별': gender_list,
        '사이즈': size_list,
        '총장': length,
        '어깨너비': shoulder,
        '가슴단면': chest,
        '소매길이': arm,
        '링크': link_list
    })


print(excel)
excel.to_excel("./상세정보_top_pop_size.xlsx", header=True, index=False)

excel_3 = pd.DataFrame(
    {
        '아이디': id_list_3,
        '제품명': title_list_3,
        '성별': gender_list_3,
        '프로필': review_list,
        '사이즈 코멘트': how_size_list,
        '코멘트': comment_list,
        '링크': link_list_3
    })

print(excel_3)
excel_3.to_excel("./상세정보_top_pop_review.xlsx", header=True, index=False)
