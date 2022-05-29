

import http
from urllib import request
from bs4 import BeautifulSoup
import requests

# html_txt = requests.get('http://www.columbia.edu/~fdc/sample.html').text
# # print(html_txt)
# soup = BeautifulSoup(html_txt, 'lxml')
# for wrapper in soup.find_all('h3'):
#     print(wrapper.text)
### now starting project phase 1 on dnsdumpster
get_req_csrf = requests.get('https://dnsdumpster.com/')
# print("Status code: ", get_req_csrf.status_code)
print(type(get_req_csrf))
print(type(get_req_csrf.content))
# print("Content: ", get_req_csrf.content)
# print("Text is : ", get_req_csrf.text)
# print("json is : ", get_req_csrf.json)
# print("Response hearder: ", get_req_csrf.headers)
# print(" ")
# print(" ")
# print("cokkies: ", get_req_csrf.cookies)
# get_cookie = get_req_csrf.cookies
# print(get_cookie)