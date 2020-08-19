# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import requests
from urllib.parse import urlparse

#자신의 API 토큰과 시크릿을 입력해주세용
client_id = "CLIENT ID"
client_secret = "CLIENT SECRET"

keyword = "망포역"
url = url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(), 
                      headers={"X-Naver-Client-Id":client_id,
                               "X-Naver-Client-Secret":client_secret},
                      verify=False)
#print(result.json())
json_obj = result.json()
#호출한 JSOn 에 들어있는 항목들 : lastBuildDate, total, start, display, items
#print(json_obj['lastBuildDate'])
#print(json_obj['total'])
#print(json_obj['start'])
#print(json_obj['display'])

#items 항목 보기
#title, link, description, bloggername, bloggerlink, postdate
#for item in json_obj['items']:
#    print(item)
#for item in json_obj['items']:
#    print(item['title'].replace("<b>","").replace("</b>",""),
#          item['link'])

#검색결과 10개에서 100개로 늘리고 싶다면?
#현재 API 기본 값이 10개 (default)
#네이버 개발자센터 --> 검색 --> API 매뉴얼 --> 검색 --> 요청변수-display 참고
#display  요청 변수를 추가하면 된다.
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100"
result = requests.get(urlparse(url).geturl(), 
                      headers={"X-Naver-Client-Id":client_id,
                               "X-Naver-Client-Secret":client_secret},
                      verify=False)
#print(result.json())
json_obj = result.json()
#호출한 JSOn 에 들어있는 항목들 : lastBuildDate, total, start, display, items
#print(json_obj['display'])
#print(len(json_obj['items']))

#최대 100개까지 한 번에 호출이 가능하다.
#나는 500개 하고 싶은데?
#호출함수를 만들어서 편하게 호출해보자. (페이지 시작번호를 지정해준다.)
def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + \
          "&display=" + str(display) + \
          "&start=" + str(start)

    result = requests.get(urlparse(url).geturl(),
             headers = {"X-Naver-Client-Id":client_id,
                        "X-Naver-Client-Secret":client_secret},
            verify=False)
    return result.json()

def call_and_print(keyword, start_page):
    json_obj  = get_api_result(keyword, 100, start_page)
    for item in json_obj['items']:
        #일부러 @를 중간중간에 넣어서 출력해보자.
        title = item['title'].replace("<b>","").replace("</b","")
        print(title+"@"+item['bloggername']+"@"+item['link'])

keyword = "망포역"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)
