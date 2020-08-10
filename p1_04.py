# Naver에서 특정 글자 추출하기 : 네이버를 시작 페이지로

import urllib.request as ur
import bs4

url = "https://www.naver.com/"
html = ur.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")
#print(bs_obj)

div = bs_obj.find("div", {"class":"service_area"})
my_find1 = div.find("a")
print(my_find1.text)

#Naver 메뉴 이름 뽑아내기 : 메일, 카페, 블로그, ...
ul = bs_obj.find("ul", {"class":"list_nav type_fix"})
lis = ul.findAll("li")
for li in lis:
    my_find2 = li.find("a")
    print(my_find2.text)

#Naver 뉴스 제목 가져오기(헤드라인)
url = "https://news.naver.com/"
html = ur.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"hdline_article_list"})
lis = ul.findAll("li")
for li in lis:
    my_find3 = li.find("a")
    print(str.strip(my_find3.text))
