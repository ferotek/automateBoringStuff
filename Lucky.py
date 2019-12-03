import requests, sys, webbrowser, bs4
address = ""
for i in range(1, len(sys.argv)):
    address += ' ' + sys.argv[i]
    
address2 = 'https://www.google.com/search?q=' + address
res = requests.get(address2)
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
linkElems = noStarchSoup.select('a')
for i in range(39, 43):
	webbrowser.open(linkElems[i].get('href')[7:])
