# By Timothy Metzger

"""Using webscraping to filter results on Ebay so that only what is exactly desired is output"""

def print_hi(name):
    # To run this, download the BeautifulSoup zip file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    import urllib.request, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    listings = soup.find_all(class_='s-item')
    titles = soup.find_all(class_='s-item__title')
    prices = soup.find_all(class_='s-item__price')
    imgs = soup.find_all(class_='s-item__image-img')
    listingLinks = soup.find_all(class_='s-item__image', )

    for item in listings:
        try:
            if '56cm' in item.find(class_='s-item__title').string.lower():
                print('Title: ', item.find(class_='s-item__title').string)
                print('Price: ', item.find(class_='s-item__price').string)
                print('Image: ', item.find(class_='s-item__image-img')['src'])
                print('Listing: ', item.find('a')['href'])
                print('\n\n')
        except AttributeError:
            print('Attribute Error')

            # https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=specialzed+56+cm+tarmac+sl7&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=specialized+56cm+tarmac


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
