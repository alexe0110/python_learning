from bs4 import BeautifulSoup
import requests

url = 'http://mignews.com/mobile'
page = requests.get(url)
print(page.status_code)

new_news = []
news = []
soup = BeautifulSoup(page.text, "html.parser")

# В ранее созданный список 'news' (к которому я обещал вернуться), сохраняем все с тэгом 'а' и классом 'news'.
news = soup.findAll('a', class_='lenta')
print(news)

for i in range(len(news)):
    if news[i].find('span', class_='time2 time3') is not None:
        new_news.append(news[i].text)

for i in range(len(new_news)):
    print(new_news[i])