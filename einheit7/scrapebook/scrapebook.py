from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'

response = urlopen(url).read()

soup = BeautifulSoup(response)

for link in soup.findAll('a'):
    if link.string == 'See full profile':
        profile_link = 'http://scrapebook22.appspot.com' + link['href']
        # hier geht's weiter
        profile_html = urlopen(profile_link).read()
        soup_profile = BeautifulSoup(profile_html)
        # suche alle span-elemente
        span_elements = soup_profile.findAll('span')
        print span_elements[-1].string
