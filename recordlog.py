import datetime
import os

acttime = datetime.datetime.now()
actdate = acttime.strftime("%d-%m-%Y")
acttime = acttime.strftime("%H-%M-%S")

fpath = os.path.abspath(__file__)
parentdir = os.path.dirname(fpath)
path = os.path.join(parentdir,"logs",actdate)

def recrecent(arr):
    try:
        os.mkdir(path)
    except OSError:
        print("day has already started")
    f = open(os.path.join(path, acttime+".txt"), "w+")
    for row in range(13):
        if row != 0:
            exname = arr[row][0]
            exname = exname[:-25]
            arr[row][0] = exname.strip()
        f.write("%s %s %s\n" %(arr[row][0],arr[row][1],arr[row][2]))
    f.close()
    