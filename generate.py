#! /usr/bin/python

#
# Chamoda Panthage
# chamodac@gmail.com
#

import fileinput
from bs4 import BeautifulSoup

xml = ''

for line in fileinput.input():
    xml += line

soup = BeautifulSoup(xml, 'xml')

elements = soup.find_all(lambda tag: 'android:id' in tag.attrs)

print '\n// Private variables\n'

for element in elements:
    print 'private ' + element.name + ' ' + element['android:id'].split("/")[1] + ';'

print '\n// Initialize elements\n'

for element in elements:
    print element['android:id'].split("/")[1] + ' = (' + element.name + ')findViewById(R.id.' + element['android:id'].split("/")[1] + ');'

print '\n'
