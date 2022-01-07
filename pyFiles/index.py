import os, sys, requests, json
from requests import cookies

# get offline or online 
mode = "offline"
if mode == "online":
    import classes
    all_classes = classes.data_json
if mode == "offline":
    data_file = open("classes.json")
    all_classes = json.load(data_file)
else:
    print("[x] Error in mode. Exiting.")
    sys.exit()

os.system("clear")

def auth_get(x,y):
    video_title = str(x)
    fetch_url = "https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=" + str(y) + "&fromWeb=1"
    session = requests.Session()
    # print(session.cookies.get_dict())
    resp=session.get(fetch_url)
    cc = session.cookies
    
    v_url = y
    v = requests.get(v_url, cookies=cc)
    #print(v.text)

    with open("m3u8/" + x + ".m3u8", "w") as writeto:
        writeto.write(v.text)

c = 1
for x,y in all_classes.items():
    auth_get(x,y)

print("Downloaded all m3u8 files to m3u8 folder.")
print("Need to convert them tp mp4 now :) ")