import json
from time import strftime, gmtime

with open("acdc.json") as f:
    file = json.load(f)
    duration = sum(int(i["duration"]) for i in file["album"]["tracks"]["track"])
    print("Time: ", strftime('%H:%M:%S', gmtime(duration)))
