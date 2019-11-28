import datetime

now = datetime.datetime.now()
now2 = now.strftime("%d-%m-%Y")

swearing = {}
if now2 not in swearing:
    swearing[now2] = 0

if now2 in swearing:
    print(swearing[now2])

print (swearing)