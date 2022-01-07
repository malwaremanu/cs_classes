from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import requests, json, os
from bs4 import BeautifulSoup
import datetime
from django.views.decorators.csrf import csrf_exempt

fetch_details_api = "https://live.eurekaacademy.co.in/?route=common/ajax&mod=liveclasses&ack=getVideoDatabyClassId&classId="
get_cookie_api = "https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&fromWeb=1&stream="
    
def index(request):

    fi = open('list_of_classes.json')
    st = ''
    for f in fi:
        st += str(f).strip()        
    
    #js_data = json.loads(fi.readlines())
    js_data = json.loads(st)

    context = {
        'jdata' : js_data
    }

    return render(request, "return_link.html", context)

def fetch_all(request):
    os.system('clear')
    page = requests.get('https://live.eurekaacademy.co.in/net-computer-science')
    list_of_pgt_cs = []

    soup = BeautifulSoup(page.text, 'html.parser')

    data = {}
    data['data'] = []

    for d in soup.find_all("div", "video"):        
        for a in str(d).split("data-item="):            
            if a[1:8] != "div cla":
                #data['id'] = a[1:8]
                data[a[1:8]] = {
                    "link" : [], 
                    'title' : '',
                    'raw_data' : ''                    
                }

            #list_of_pgt_cs.append(d)
        so = BeautifulSoup(str(d), 'html.parser')
        
        data[a[1:8]]['link'].append(so.div.a.attrs['href'])         
        data[a[1:8]]['title'] = so.div.img.attrs['alt']

        #data[a[1:8]]['raw_data'] = str(d)
        #data['data'].append(so.div.img.attrs)            
        list_of_pgt_cs.append(data)
    

    for d in soup.find_all("div", "video locked"):        
        for a in str(d).split("data-item="):            
            if a[1:8] != "div cla":
                #data['id'] = a[1:8]
                data[a[1:8]] = {
                    "link" : [], 
                    'title' : '',
                    'raw_data' : ''                    
                }

            #list_of_pgt_cs.append(d)
        so = BeautifulSoup(str(d), 'html.parser')
        
        data[a[1:8]]['link'].append(so.div.a.attrs['href'])         
        data[a[1:8]]['title'] = so.div.img.attrs['alt']

        #data[a[1:8]]['raw_data'] = str(d)
        #data['data'].append(so.div.img.attrs)            
        list_of_pgt_cs.append(data)
    
    context = {
        "data" : list_of_pgt_cs
    }
    #print(context)
    #return render(request, "all.html")
    wf = open('list_of_classes.json', 'w')
    #wf.write(json.dump(context))
    json.dump(context, wf, indent = 6)
    wf.close()

    return JsonResponse({
        "msg" : "saved to file.",
        'time' : datetime.datetime.now()
    })

def all(request):
    fi = open('list_of_classes.json')
    st = ''
    for f in fi:
        st += str(f).strip()        
    
    #js_data = json.loads(fi.readlines())
    js_data = json.loads(st)
    #print(js_data)
    
    return JsonResponse(js_data)

def fetchs(id):
    r = requests.get(fetch_details_api + str(id))
    # print(r.text)
    return r.text

@csrf_exempt
def fetch(request):
    if not request.POST:
        return redirect(index)
        # return HttpResponse("Invalid access.")
    else:
        if "?" in request.POST["link"]:
            id = request.POST["link"].strip().split("?")[0].split("-")[-1] 
        else:
            id = request.POST["link"].strip().split("-")[-1]

        datas = json.loads(fetchs(id))
        print(datas)

        m3u8_file = datas["data"]["primPlaybackUrl"]
        if m3u8_file != None:
            coo = get_cookie_api + datas["data"]["primPlaybackUrl"]
        else:
            coo = "Video upload pending."
        
        context = { "title" : datas["data"]["primaryStream"],
        "video" : datas["data"]["primPlaybackUrl"], 
        "cookie_url" : coo
         }

        return render(request, "video.html", context)