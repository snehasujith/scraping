import requests
from bs4 import BeautifulSoup
website_url = 'https://www.geeksforgeeks.org/python-programming-language/'
res = requests.get(website_url)
#print(res.text)
soup = BeautifulSoup(res.content,'html.parser')
s = soup.find('div', class_= 'page_content')
line = s.find_all('p')
for line in line:
    print(line.text)

