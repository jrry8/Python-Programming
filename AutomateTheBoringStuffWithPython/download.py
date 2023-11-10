# Download the last dozen XKCD comics.

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

for _ in range(12):
    # request page
    if url.endswith('#'):
        break
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    # download image
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s...' %comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get next url
    prevLink = soup.select('a[rel="prev"]')
    url = 'http://xkcd.com' + prevLink[0].get('href')

print('Done.')