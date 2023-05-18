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
movie_id=160244
url=f"https://movie.daum.net/moviedb/grade?movieId={movie_id}"   # Protocal Address Data

result=requests.get(url)
print(result.text)
doc=BeautifulSoup(result.text, "html.parser")
reviews=doc.select("ul.list_comment li")
print(reviews)

########################################
# 1.Install ChromeDriver for selenium #
#########################################
# Selenium -> webdriver필요 우린 chrome사용

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)