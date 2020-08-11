import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/"
headers = {'User-Agent': 'Mozilla/5.0'}
#headers를 안넣으면, requests로 접근하는 걸 비정상적인 접근으로 보고 차단해버린다..
result = requests.get(url=url, headers=headers, verify=False)
bs_obj = BeautifulSoup(result.content, "html.parser")
#print(bs_obj)

#1. 제품명을 뽑아보자. 
#개발자 도구를 열고, 제품 이름이 있는 부분을 선택한다. (ex. Isntree Hy ...)
#이 부분을 bs4로 추출한다.
ul = bs_obj.find("ul", {"class":"prdList grid4"})
#print(ul)

#하나의 상품은 div로 감싸져 있다.
boxes =ul.findAll("div", {"class":"box"})
#상품명은 p 태그 중 class가 "name"인 곳 안에 있다.
#span 태그로 감싸져 있다.
for box in boxes:
    ptag = box.find("p", {"class":"name"})
    span = ptag.find("span")
    #print(span.text)


#2. 제품명, 가격을 뽑아보자.
#name, price (함수를 만들어서 뽑아보자!)
for box in boxes:
    ptag = box.find("p", {"class":"name"})
    span = ptag.find("span")
    name = span.text

    ul = box.find("ul", {"class":"xans-element- xans-product xans-product-listitem"})
    prices = ul.findAll("span")
    price = prices[1].text 

    result = {"name":name, "price":price}
    #print(result)


#3. 2번을 함수로 만들고, 결과값을 리스트로 만들기
def get_product_info(box):
    ptag = box.find("p", {"class":"name"})
    span = ptag.find("span")
    name = span.text

    ul = box.find("ul", {"class":"xans-element- xans-product xans-product-listitem"})
    prices = ul.findAll("span")
    price = prices[1].text 

    result = {"name":name, "price":price}
    return result

#for문으로 list만드는 법은 python 문법 구글링 참고
product_info_list = [get_product_info(box) for box in boxes]
#print(product_info_list)

#4. 1페이지 부터 5페이지까지 데이터 받아오기
#먼저, url을 주면 priduct_info_list를 반환하는 함수를 만든다.
def get_page_products(url):
    result = requests.get(url=url, headers=headers, verify=False)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    ul = bs_obj.find("ul", {"class":"prdList grid4"})

    boxes = ul.findAll("div", {"class":"box"})
    product_info_list = [get_product_info(box) for box in boxes]

    return product_info_list

page_products = get_page_products(url)
#print(page_products)

#2page로 이동하면 url에 ?page=2가 붙는 것을 볼 수 있다.
#1~5page 까지 뽑아보자.
urls = ["http://jolse.com/category/tonermist/43/"]*5
for i in range(5):
    url = urls[i]+"?page="+str(i+1)
    page_products = get_page_products(url)
    print(page_products)
