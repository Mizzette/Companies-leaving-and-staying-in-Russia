from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://inkocoin.ru/spisok-kompanij-ushedshih-iz-rossii-2022-iz-za-ukrainy-i-sankcij/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, 'lxml')
names = soup.findAll("ul")
all_companies = {}
i = 0
for ul in names:
    if 5 < i < 36 :
        for li in ul.findAll('li'):
            text = li.text
            if (text.find('\xa0—') != -1):
                if text[text.find('—')-1] == '\xa0':
                    text = text.split('\xa0—')
                else:
                    text = text.split ( ' —' )
                all_companies[text[0]] = text[1][1:-1]
            else:
                all_companies[text] = "-"
    i += 1

print(all_companies, sep='\n')


data = pd.DataFrame( {"Name" : [], "Action" : []} )

for i in all_companies:
    temp = []   
    temp.append(i)
    temp.append(all_companies.get(i))
    data.loc[len(data)] = temp
    temp.clear()

data.to_csv("List of companies", encoding='utf-8')

print(data)
