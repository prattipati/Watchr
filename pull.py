import json
import urllib.request

def data():
    # GET request for data
    results = json.loads(urllib.request.urlopen("https://www.kimonolabs.com/api/7kwrt2m6?apikey=m7HpuKp7CCQdG3yGRArJQzu7nqDWczAX").read().decode("utf-8"))
    #print(message)
    return(results)
