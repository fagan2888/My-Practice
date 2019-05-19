

##############################################
########### Web Scraping Practice ############
##############################################


from bs4 import BeautifulSoup as soup
from urllib.parse import urljoin
import requests
import validators

# initialize variables
url = 'http://www8.gsb.columbia.edu/'
urls = {}
urls[url] = 1
seen = {}
opened = []
maxNumUrl = 50
keywords=['finance', 'engineering', 'business', 'research']

while len(urls)>0 and len(opened)<maxNumUrl:
    
    # remove the highest scoring url from urls and assign it to curr_url
    curr_url = max(urls, key = urls.get)
    del urls[curr_url]
    
    if validators.url(curr_url):  # check if the url exists
        
        # add this curr_url to opened if it can be opened
        opened.append(curr_url)
        
        # extract the text using BeautifulSoup
        web = requests.get(curr_url)
        web_text = web.text
        text = soup(web_text)
        
        # assign the body text to htmltext
        htmltext = text.find('body').get_text()
        web.close()
        
        # count the number of occurences of words in list of keywords
        count = 0
        for word in keywords:
            count += htmltext.lower().count(word)  
        seen[curr_url] = count
        
        if count > 0:
            links = text.find_all('a')
            if len(links) > 0:
                for link in links:
                    if link.has_attr('href'):
                        href = link.attrs['href']
                        if not href.startswith('http'):
                            href = urljoin(curr_url, href)
                
                        # check if the tag is not in seen
                        if not href in seen:
                            urls[href] = count

print('The number of urls seen is {}'.format(len(seen)))
print('The number of urls opened is {}'.format(len(opened)))

url_copy = urls
score_list = {}

for i in range(25):
    max_score = max(url_copy, key = url_copy.get)
    score_list[max_score] = url_copy[max_score]
    del url_copy[max_score]

for key, value in score_list.items():
    print(key, value)
