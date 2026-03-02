import requests
import re
from urllib.parse import urljoin
target = "http://192.168.159.153/"
target_url = "http://192.168.159.153/mutillidae/"
target_links = []
def extract_url(url):
    response = requests.get(url)  #here in this regex first is location to identify and then the string
    return re.findall('(?:href=")(.*?)"', str(response.content))

def crawl(url):
    href_link = extract_url(url)
    for link in href_link:
        link = urljoin(url,link)
        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)




