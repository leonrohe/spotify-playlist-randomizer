import requests
import random
import os
from bs4 import BeautifulSoup

url = input("Enter spotify playlist url \n")
url+="&nd=1"

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

r = requests.get(url)
content = r.text
soup = BeautifulSoup(content, "html.parser")
links = soup.find_all("a")

tracks = []
for link in links:
    url = link["href"]
    if(url[0:1] == "h"):
        tracks.append(url)

random.shuffle(tracks)

copy_str = ""
for track in tracks:
    copy_str+=track+"\n"

with open("shuffled.txt", "w") as f:
    f.write(copy_str)

