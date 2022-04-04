import requests
from bs4 import BeautifulSoup
import re
import recordlog
import checkann

url = "https://www.isbank.com.tr/doviz-kurlari"

page = requests.get(url).text

soup = BeautifulSoup(page, "lxml")

results = soup.find_all("table", class_="dk_MT")

table1 = results[0]

body = table1.find_all("tr")

body_rows = body[1:] # All other items becomes the rest of the rows

arr = []

for j in range(13):
    column = []
    for i in range(3):
        column.append(0)
    arr.append(column)

arr[0][0] = "Name"
arr[0][1] = "Buy"
arr[0][2] = "Sell"

for row_num in range(len(body_rows)): # A row at a time
    i = 0
    for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
        aa = re.sub(r"(\xa0)|(\n)|(\r)|(\')|(^\s+)|(\s+$)|(\t)","",row_item.text)
        aa = aa.replace(",",".")
        aa = aa.strip()
        arr[row_num+1][i] = aa
        i+=1

recordlog.recrecent(arr)

checkann.alarm(arr)

