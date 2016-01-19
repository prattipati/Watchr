import json
import urllib.request

# POST method starts Kimono Api Webcrawl
url = "https://www.kimonolabs.com/kimonoapis/7kwrt2m6/startcrawl"
key = {"apikey" : "m7HpuKp7CCQdG3yGRArJQzu7nqDWczAX"}
key = urllib.parse.urlencode(key)
key = key.encode('ascii')
req = urllib.request.Request(url, key)
with urllib.request.urlopen(req) as response:
    message = response.read
