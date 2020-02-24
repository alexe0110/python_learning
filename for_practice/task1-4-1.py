from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html') # скачиваем файл
soup = BeautifulSoup(resp, 'html.parser') # делаем суп
cnt = 0

a=soup.get_text()
b=a.split('\n')
for i in range(b.count('')):
    b.remove('')

for j in b:
    cnt += int(j)

print(cnt)