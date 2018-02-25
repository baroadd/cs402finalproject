import requests
from bs4 import BeautifulSoup
import re

#url = "http://localhost/testHtml.html"

def findMethod(url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all("button")
    for x in data:
        if x.get('onclick'):
            funcName = x.get('onclick')
            return funcName
    
def findAllScript(url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all("script")
    for x in data:
        return x.get_text()


