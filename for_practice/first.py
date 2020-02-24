from abc import abstractclassmethod
from urllib.request import urlopen
import re
from collections import Counter

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
print(html.count('C++'))
print(html.count('Python'))
regex = '<code>(.*?)</code>'
l = sorted(re.findall(regex, html))
a = Counter(l)
print(a)
print(a.most_common(4))