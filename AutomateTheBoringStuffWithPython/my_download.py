# Download all images from gallery.

import requests, os, bs4

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
pageUrl = 'https://'

# iterate each page on the website
while True:
    res = requests.get(pageUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # iterate through each album on current page
    albums = soup.select('.item-link.popunder')
    for album in albums:
        albumLink = album.get('href')
        albumUrl = 'https://' + albumLink

        # find how many pages the album has
        res = requests.get(albumUrl, headers=headers)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        pageElem = soup.select('.pagination-list span')
        numPages = len(pageElem) // 2

        # create new folder for the album
        albumName = soup.select('.article-header h1')[0].text.replace(':', '').strip()
        os.makedirs(albumName, exist_ok=True)
        print("Opening " + albumName + " ...")

        # download all images from one album
        for page in range(1, numPages + 1):
            curUrl = albumUrl + "?page=" + str(page)

            res = requests.get(curUrl, headers=headers)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, "html.parser")
            photoElem = soup.select('.article-fulltext img')

            if not photoElem:
                print('Could not find image.')
            else:
                for i in range(len(photoElem)):
                    print("Downloading page " +  str(page) + " - image " + str(i+1))
                    photoUrl = photoElem[i].get('src')
                    res = requests.get(photoUrl)
                    res.raise_for_status()
                    imageFile = open(os.path.join(albumName, os.path.basename(photoUrl)), 'wb')
                    for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
        print("Download for " + albumName + " is complete.\n")

    # get next url
    res = requests.get(pageUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    nextLink = soup.select('.pagination-next')[0].get('href')
    if nextLink == "javascript:;":
        break
    pageUrl = 'https://' + nextLink

print('Done.')
