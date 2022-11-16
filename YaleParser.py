import warnings
from bs4 import BeautifulSoup
import requests
import pandas as pd

warnings.filterwarnings("ignore")

url = 'https://som.yale.edu/story/2022/over-1000-companies-have-curtailed-operations-russia-some-remain'
req = requests.get(url)
bs = BeautifulSoup(req.text)

data = pd.DataFrame({'Name' : [], 'Action' : [], 'Industry' : [], 'Country' : []})

def buyingTime(data):
    temp_text = bs.find('section', {'id' : 'buyingtime'}).text
    temp_arr = temp_text.split('\n')
    temp_arr = temp_arr[24:-7]
    temp_arr = [i for i in temp_arr if i != '']

    counter = 0
    t = []
    for i in temp_arr:
        t.append(i)
        counter += 1
        if counter == 4:
            data.loc[len(data)] = t
            t = []
            counter = 0

def scalingBack(data):
    temp_text = bs.find('section', {'id' : 'scalingback'}).text
    temp_arr = temp_text.split('\n')
    temp_arr = temp_arr[24:-7]
    temp_arr = [i for i in temp_arr if i != '']
    temp_arr.insert(109, 'NaN')
    temp_arr.insert(586, 'NaN')
    counter = 0
    t = []
    for i in temp_arr:
        t.append(i)
        counter += 1
        if counter == 4:
            data.loc[len(data)] = t
            t = []
            counter = 0

def suspension(data):
    temp_text = bs.find('section', {'id' : 'suspension'}).text
    temp_arr = temp_text.split('\n')
    temp_arr = temp_arr[24:-7]
    temp_arr = [i for i in temp_arr if i != '']
    temp_arr.insert(305, 'NaN')
    counter = 0
    t = []
    for i in temp_arr:
        t.append(i)
        counter += 1
        if counter == 4:
            data.loc[len(data)] = t
            t = []
            counter = 0

def withdrawal(data):
    temp_text = bs.find('section', {'id' : 'withdrawal'}).text
    temp_arr = temp_text.split('\n')
    temp_arr = temp_arr[24:-7]
    temp_arr = [i for i in temp_arr if i != '']
    counter = 0
    t = []
    for i in temp_arr:
        t.append(i)
        counter += 1
        if counter == 4:
            data.loc[len(data)] = t
            t = []
            counter = 0

buyingTime(data)
scalingBack(data)
suspension(data)
withdrawal(data)
