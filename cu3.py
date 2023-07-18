from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome()

# 페이지 접속
driver.get('http://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N')

# 더보기 버튼이 더 이상 나타나지 않을 때까지 반복
while True:
    try:
        time.sleep(10)
        # 더보기 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, 'div.prodListBtn-w > a').click()
        # 로딩 대기를 위해 약간의 시간 대기
    except NoSuchElementException:
        # 더보기 버튼이 더 이상 나타나지 않으면 반복 종료
        break

# 페이지 소스를 BeautifulSoup으로 파싱

# 크롤러 코드
html = driver.page_source

# 파일로 저장
with open('html_output.html', 'w', encoding='utf-8') as file:
    file.write(html)

# 크롤링이 완료되었으므로 드라이버 종료
driver.quit()
