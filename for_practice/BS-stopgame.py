from bs4 import BeautifulSoup as BS
import requests

max_pages = 5
pages = []

for j in range(1, max_pages + 1): # делаем запросы ко всем 5 страницам
    pages.append(requests.get('https://stopgame.ru/topgames/?p=' + str(j)))

for r in pages:
    html = BS(r.content, 'html.parser')     # используем css селекторы
    for i in html.select('.lent-block'):
        a = i.select('.lent-brief>.title>a')
        print(a[0].text) # просим вывести именно текст, а не html элемент

