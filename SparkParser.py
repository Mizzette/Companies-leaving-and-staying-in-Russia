import warnings
from bs4 import BeautifulSoup
import requests

warnings.filterwarnings("ignore")

'''FUNCTIONS'''

def findInn(req):
    bs = BeautifulSoup(req.text)
    temp = bs.find('div', 'code')
    if temp:
        temp_text = temp.text.split()
        return temp_text[1]

def createQuery(query):
    query_split = query.split(' ')
    query = ''
    for i in query_split:
        query += i + '+'
    query = query[:-1]
    return query

def createUrl(name):
    query = createQuery(name)
    url = 'https://spark-interfax.ru/search?Query=' + query
    return url

def createRequest(url):
    # Свой user_agent можно найти здесь https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
    #user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    req = requests.get(url)
    return req


'''DRIVER CODE(Test)'''

# The name of company
names = ['Acerinox', 'Agrana', 'Agricultural bank of China', 'Air China', 'Samsung']
for name in names:
    url = createUrl(name)
    req = createRequest(url)
    print(findInn(req))
