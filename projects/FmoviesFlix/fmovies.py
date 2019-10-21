#! python3
import requests, webbrowser
from bs4 import BeautifulSoup

print("What would you like to watch")

searchString = input()
print('Finding ...')

res = requests.get("https://fmovies.to/search?keyword="+searchString)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())
m = []
movie = soup.select('a')
for i in movie:
    s = str(i)
    x = s.count("name")
    y = s.count("film")
    if x>0 and y>0:
        m.append(i)
    
#print(m)
names = []
for j in m:
    for i in j:
        names.append(i)

length = len(names)
for i in range(length):
    label = i+1
    print(label," ",names[i])
    
print("")    
print("Which one?")
num = int(input())
num -= 1
theLink = m[num].get('href')
res2 = requests.get("https://fmovies.to"+theLink)
soup2 = BeautifulSoup(res2.text, 'html.parser')

desc = soup2.select('.desc')
description = []
for i in desc[0]:
    description.append(i)
    
descc = str(description[0])
print("Description:")
print(descc)    
print("")
print("Is this  the One?(y/n)")
ans =input()
ans = ans.lower()
if ans=="y":
    webbrowser.open("https://fmovies.to"+theLink)
