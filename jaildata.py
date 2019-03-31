import urllib2, csv
##the above line pulls in the toolkit "urllib2", which allows us to use python to visit websites.
##I think it also pulls in the "csv" library which allows us to read and write csv files as well.
from bs4 import BeautifulSoup
##the above line is pulling in the toolkit "BeautifulSoup" from the BeautifulSoup library.

outfile = open('jaildata.csv', 'w')
##the above line names whatever data we are gonna export in the format of csv 'jaildata.csv', and I'm guessing the 'w' means a mode to overwrite the original file?
##note to self:
## "Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files." per Stackoverflow
writer = csv.writer(outfile)
##this is using the method "writer" from the csv object. It means: prepare to receive data and convert them in whatever way that's dictated in the 'outfile' line of code.

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
##this is where the data comes from.
html = urllib2.urlopen(url).read()
##using the urlopen method from urllib2 to open the above url and read in data.

##note to self:
##the basic way per docs.python.org to use urllib2 breaks the above code in two steps
##e.g.
##import urllib2
##response = urllib2.urlopen('http://python.org/')
##html = response.read()

soup = BeautifulSoup(html, "html.parser")
##using BeautifulSoup method to parse the data, specifically, the code says we want to use 'html.parser', which is python's built-in html parser.

tbody = soup.find('tbody', {'class': 'stripe'})
##this is to use the find method to:
##1)search for a 'tbody' element, which is the body of the information in a table. 
##2)further adding conditions to the search. I want tbody where the class says 'stripe'.

rows = tbody.find_all('tr')
##set up a class of rows. This finds all the 'tr' tags in the html document.
##tr defines a row in an html table, per google.

for row in rows:
	##suggests a for loop

    cells = row.find_all('td')
    ##each cell would now correspond to each 'td' tag found in the document.
    ##td represents a standard cell in an html table, per google

    data = []##creates a new empty list
    for cell in cells:
        data.append(cell.text.encode('utf-8'))
        ##this loop adds to the empty list we just created and encode each cell in the utf-8 format.

    writer.writerow(data)
    ##using the writerow method to write rows into the data list.