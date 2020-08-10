from urllib.request import urlopen
import bs4

url = "https://www.naver.com"
html = urlopen(url)
#print(html.read())

bs_obj = bs4.BeautifulSoup(html, "html.parser")
print(type(bs_obj))
#print(bs_obj)

print(bs_obj.find("div"))
print(bs_obj.find("ul"))
print(bs_obj.find("h3"))

div = bs_obj.find("div")
print(div)
span = div.find("span")
print(span)
print(span.text)

spans = div.findAll("span")
print(spans)
for value in spans:
    print(value.text)

#태그, 속성, 속성값
#<ul class="value">
#태그 : <ul>
#속성 : class
#속성값 : "value"

li = bs_obj.findAll("li")
print(li)
li_class = bs_obj.find("li", {"class":"air_item"})
print(li_class)

atag = bs_obj.findAll("a")
print(atag)
for value in atag:
    print(value['href'])

