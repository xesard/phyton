import requests
from bs4 import BeautifulSoup

def get_subdomains(url):
    subdomains = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    for link in links:
        if link and link.startswith("http"):
            subdomain = link.split("//")[1].split(".")[0]
            if subdomain not in subdomains:
                subdomains.append(subdomain)
    return subdomains

url = "https://targetURL_PEPINILLO.com"
print(get_subdomains(url))
