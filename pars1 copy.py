import requests
from bs4 import BeautifulSoup

url = "http://pifpaf.ml"
r = requests.get(url)
data = r.text

soup = BeautifulSoup(data, 'html.parser')
soup.prettify()

with open('data.html', 'w') as f:
    f.write(str(soup))
