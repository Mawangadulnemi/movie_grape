import time
import re
import math
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# anaconda prompt
# > conda activate cnu_python
# > pip install beautifulsoup
# > pip install selenium
# > pip install webdriver_manager


# Selenium: 동적 페이지에서 웹 크롤링 가능!
#          -> 원래 용도: 웹 브라우저 테스트용

# http: 웹 https(secure 약자)
# ftp: 파일 전송
# ssh: 터미널 접속
# smtp: 메일전송
########################################  request 로 html 가져오기
# movie_id=160244
# url=f"https://movie.daum.net/moviedb/grade?movieId={movie_id}"   # Protocal Address Data
#
# result=requests.get(url)
# print(result.text)
# doc=BeautifulSoup(result.text, "html.parser")
# reviews=doc.select("ul.list_comment li")
# print(reviews)
##############################################


########################################
# 1.Install ChromeDriver for selenium #
#########################################
# Selenium -> webdriver필요 우린 chrome사용

options=Options()
options.add_experimental_option("detach", True)  #ChromeDriver 자동종료 X
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



#########################################
# 2.Open URL in ChromeDriver #
#########################################
movie_id=160244
url=f"https://movie.daum.net/moviedb/grade?movieId={movie_id}"
# Selenium의 ChromeDriver를 통해 해당 URL 접속
driver.get(url)
time.sleep(1)  # 1초 딜레이(web page 렌더링 완료까지 기다리기 시간 벌기 느낌)
doc_html=driver.page_source  # 해당 URl 소스코드

doc=BeautifulSoup(doc_html, "html.parser")
title=doc.select("span.txt_tit")[1].text.strip() # 영화 제목 수집  텍스트만 좌우 공백 없애기


total_review_txt=doc.select("span.txt_netizen")[0].text
# 정규화 -> 숫자만 추출
total_review=int(re.sub(r"[^~0-9]","",total_review_txt))




# 리뷰 총 91개
# 기존 10개
# 1클릭당 30개 추가
# 전체리뷰-기존출력/30 =3(평점 더보기 클릭 횟수)

click_cnt=math.ceil((total_review-10)/30)  #"평점 더보기" 버튼 클릭 횟수(모든 리뷰 출력을 위한) 반올림
for i in range(click_cnt):
    # "평점 더보기" 클릭(30개씩 증가)
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)
time.sleep(5)



# >> 해당 페이지에 모든 리뷰 출력 완료
review_html=driver.page_source
doc=BeautifulSoup(review_html, "html.parser")
review_list=doc.select("ul.list_comment div.cmt_info")

for review_box in review_list:
    score=review_box.select("div.ratings")
    print(f"- 평점:{score}")
    writer=review_box.select("")
    review = review_box.select("")
    review_date = review_box.select("")

# 숙제: 리뷰, 작성자, 작성일자 수집