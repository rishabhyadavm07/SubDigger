

from urllib import request
from bs4 import BeautifulSoup
import requests

html_txt = requests.get('http://www.columbia.edu/~fdc/sample.html').text
# print(html_txt)
soup = BeautifulSoup(html_txt, 'lxml')
for wrapper in soup.find_all('h3'):
    print(wrapper.text)
