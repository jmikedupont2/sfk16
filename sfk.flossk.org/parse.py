from bs4 import BeautifulSoup
import re
import unicodedata


f = open ('index.html')
html_doc=""
for l in f.readlines():
    #print l
    html_doc += l
soup = BeautifulSoup(html_doc, 'html.parser')


for d in soup.find_all('div', class_='speaker'):
    #print "Speaker" + d.h4.text

    t=d.h4.text
    t=re.sub(r'\s+','_', t)
    t=unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')
    d['id']="Speaker_" + t.decode('utf-8')
    
for d in soup.find_all('div', class_='event'):
    #print "Talk"+ d.h3.text
    t=d.h3.text
    t=re.sub(r'\s+','_', t)
    t=unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')
    d['id']="Talk_" + t.decode('utf-8')

    

print(soup.prettify())
