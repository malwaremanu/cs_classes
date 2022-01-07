import os, sys, json, requests
from bs4 import BeautifulSoup

os.system("clear")

site_url = "https://live.eurekaacademy.co.in/tgt-computer-science-new-batch-2021"

r = requests.get(site_url).text

list_of_pgt_cs = []

soup = BeautifulSoup(r, 'html.parser')
for d in soup.find_all("div", "liveClassesList"):
    for a in str(d).split("data-item="):
        code = a[1:8]
        if code != "div cla":
            list_of_pgt_cs.append((a[1:8]))

def get_list():
    return list_of_pgt_cs

print(list_of_pgt_cs)