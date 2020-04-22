# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =  'http://py4e-data.dr-chuck.net/comments_415350.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
numlist = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('span', None))
    #print('Contents:', tag.contents[0:])
    #print('Attrs:', tag.attrs)
    x = tag.contents[0:1]
    for nums in x:
        numlist.append(nums)
            #Converts strings to integers in numlist
        numlist = [int(nums) for nums in numlist]

print(sum(numlist))
