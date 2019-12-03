import requests, os, bs4
url = 'http://xkcd.com'   
i = 1           
os.makedirs('xkcd', exist_ok=True)   
while not url.endswith('#'):
    # Download the page.
    
    url2 = url + '/' + str(i) + '/'
    res = requests.get(url2)
    print(url2)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    img = soup.select('img')
    comicurl = 'http://'+ img[2].get('src')[2:]
    res = requests.get(comicurl)
    res.raise_for_status()
    
    xkcdimg = open(os.path.join('xkcd/', str(i) + 'xkcd.png'), 'wb')
    for chunk in res.iter_content(100000):
    	xkcdimg.write(chunk)
    xkcdimg.close()
    i = i + 1
    if i == 404:
    	i +=1


