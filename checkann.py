import smtplib, ssl
import configvars as cv
import datetime

timenow = datetime.datetime.now()
timenowdate = timenow.strftime("%d/%m/%Y %A")
timenowtime = timenow.strftime("%H:%M")

port = 465
password = cv.passcode

context = ssl.create_default_context()
sender_email = cv.sendmail
receiver_email = cv.recmail

prefmessage = cv.message

def alarm(arr):
    for row in range(12):
        for cur in cv.currency:
            if arr[row][0] == cur:
                buy = float(arr[row][1])
                sell = float(arr[row][2])
                tar = cv.target[cv.currency.index(cur)]
                if buy >= tar:
                    message = (prefmessage.format(cur, timenowdate, timenowtime, buy, sell, tar))
                    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                else:
                    print("wait mf")
