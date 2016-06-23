import urllib2
from BeautifulSoup import BeautifulSoup

url = 'https://scrapebook22.appspot.com/'
response = urllib2.urlopen(url).read()

soup = BeautifulSoup(response)

# import the csv module
import csv
# open a new file for writing
output_file = open('output.csv', 'w')

for link in soup.findAll('a'):
    if link.string == 'See full profile':
        person_url = 'https://scrapebook22.appspot.com' + link['href']
        person_html = urllib2.urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.findAll('span')[-1].string
        name = person_soup.findAll('h1')[1].string

        # split first name and last name
        first_name, last_name = name.split(' ')

        # save data as CSV file
        
        # create a CSV writer
        writer = csv.writer(output_file)
        writer.writerow([first_name, last_name, email])

output_file.close()
