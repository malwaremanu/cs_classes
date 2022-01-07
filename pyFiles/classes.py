import os, sys, requests, json
os.system("clear")
import list_from_site

fid = sorted(list_from_site.list_of_pgt_cs)
list_url = "https://live.eurekaacademy.co.in/?route=common/ajax&mod=liveclasses&ack=getVideoDatabyClassId&classId="

def fetch(id):
    r = requests.get(list_url + str(id))
    # print(r.text)
    return r.text
# https://live.eurekaacademy.co.in/computer-science-digital-electronics-class-8-2374230?frompkg=tgt-computer-science-new-batch-2021

data_json = {}

for a in fid:
    datas = json.loads(fetch(a))
    try:
        title = datas["data"]["classUrl"]
        if "computer" in title.split("-"):
        # if title:            
            # print(title)
            data_json[title] = datas["data"]["primPlaybackUrl"]
    except:
        pass

with open("classes.json", "w") as data_file:
    data_file.write(json.dumps(data_json))



