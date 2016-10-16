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
    print ("\n\nSpeaker" + d.h4.text    )
    t=d.h4.text
    t=re.sub(r'\s+','_', t)
    t=unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')
    d['id']="Speaker_" + t.decode('utf-8')

    detail=d.figure.figcaption.a['href']
    f3 = open ("sfk16/" + detail)
    details = ""
    for l in f3:
        details += l
    soup2 = BeautifulSoup(details, 'html.parser')
    #print(d.prettify())    
    print(soup2.prettify())    
    
    
for d in soup.find_all('div', class_='event'):
    #print "Talk"+ d.h3.text
    t=d.h3.text
    t=re.sub(r'\s+','_', t)
    t=unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')
    d['id']="Talk_" + t.decode('utf-8')

    

#print(soup.prettify())
