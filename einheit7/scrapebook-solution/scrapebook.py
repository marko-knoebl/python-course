import urllib2
from BeautifulSoup import BeautifulSoup

url = 'https://scrapebook22.appspot.com/'
response = urllib2.urlopen(url).read()

soup = BeautifulSoup(response)

print soup.html.head.title.string

for link in soup.findAll('a'):
    if link.string == 'See full profile':
        person_url = 'https://scrapebook22.appspot.com' + link['href']
        person_html = urllib2.urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        print person_soup.findAll('span')[-1].string

        print person_soup.findAll('h1')[1].string
