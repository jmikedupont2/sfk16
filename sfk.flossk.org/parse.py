from bs4 import BeautifulSoup
f = open ('index.html')
html_doc=""
for l in f.readlines():
    #print l
    html_doc += l
soup = BeautifulSoup(html_doc, 'html.parser')


for d in soup.find_all('div', class_='speaker'):
    #print "Speaker" + d.h4.text
    d.id_="Speaker_" + d.h4.text

for d in soup.find_all('div', class_='event'):
    #print "Talk"+ d.h3.text
    d.id_="Talk_" + d.h3.text
    

print(soup.prettify())
