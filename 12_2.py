# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= 'http://py4e-data.dr-chuck.net/known_by_Ciarian.html'
# if len(url) < 1 : name = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

hrefs = []
for link in soup.find_all('a'):
    href = link.get('href')
    hrefs.append(href)
#Test to see if I got the right data-Aniqua
#print(hrefs[0])

repeat = 1
input_repeat = input('Enter count: ')
input_repeat = int(input_repeat)
while repeat < input_repeat:
    # print('Repeat-Start:', repeat) # debug
    new_url = hrefs[17]
    new_html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(new_html, 'html.parser')
    hrefs.clear()
    hrefs = []
    for link in soup.find_all('a'):
        href = link.get('href')
        hrefs.append(href)
    print(hrefs[17])
    repeat = repeat + 1

    #print('Repeat-End:', repeat) # debug
