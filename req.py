import os
import time
os.system("cls") 


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}



def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

time.sleep(3)

msg = '''
[[red]]
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. |
| |      __      | || |  ____  ____  | || | ____    ____ | || |  _________   | || |  ________    | | | |   _____      | || |  ____  ____  | |
| |     /  \     | || | |_   ||   _| | || ||_   \  /   _|| || | |_   ___  |  | || | |_   ___ `.  | | | |  |_   _|     | || | |_  _||_  _| | |
| |    / /\ \    | || |   | |__| |   | || |  |   \/   |  | || |   | |_  \_|  | || |   | |   `. \ | | | |    | |       | || |   \ \  / /   | |
| |   / ____ \   | || |   |  __  |   | || |  | |\  /| |  | || |   |  _|  _   | || |   | |    | | | | | |    | |   _   | || |    \ \/ /    | |
| | _/ /    \ \_ | || |  _| |  | |_  | || | _| |_\/_| |_ | || |  _| |___/ |  | || |  _| |___.' / | | | |   _| |__/ |  | || |    _|  |_    | |
| ||____|  |____|| || | |____||____| | || ||_____||_____|| || | |_________|  | || | |________.'  | | | |  |________|  | || |   |______|   | |
| |              | || |              | || |              | || |              | || |              | | | |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------' 
 
 
 
 
 
'''

print(colorText('[[red]]======================================================================================================================================'))


time.sleep(3)

print(colorText(msg))

import requests

start =False 
# username = "Ahmed-Ly"
username = input(colorText('[[red]]enter [[yellow]]username :'))

Texts = None

url = f"https://api.github.com/users/{username}"
link = f"https://api.github.com/users/{username}/repos"
subscriptions = f"https://api.github.com/users/{username}/subscriptions"


start =True 

user_data = requests.get(url).json()

user_data_more = requests.get(link).json()


user_subscriptions = requests.get(subscriptions).json()

def nameuser():
    return user_data['login']


def emailuser():
    return user_data['email']



def created_at():
    return user_data['created_at']



def iduser():
    return user_data['id']



def locationuser():
    return user_data['location']


def userfollowers():
    return user_data['followers']




def userfollowing():
    return user_data['following']


def avatar_urluser():
    return user_data['avatar_url']



def getFullnameRepo():
  for x in range(1,len(user_data_more)):
         print(user_data_more[x]['full_name'])


def getallinfosubscriptions():
 for y in range(1,len(user_subscriptions)):
         print(user_subscriptions[y]['full_name'],'<===============>',user_subscriptions[y]['url'])

while True:
  if start == True:
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'following':
     f =   userfollowing()
     print(f)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'followers':
     fr =   userfollowers()
     print(fr)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'iduser':
     q =   iduser()
     print(q)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'created_at':
     we =   created_at()
     print(we)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'locationuser':
     wee =   locationuser()
     print(wee)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'email':
     qwer =  emailuser()
     print(qwer)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'nameuser':
     wef =  nameuser()
     print(wef)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'avatar_url':
     fdss =  avatar_urluser()
     print(fdss)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'avatar_url':
     fdss =  avatar_urluser()
     print(fdss)
     Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'repo':
       repi = getFullnameRepo()
       Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))
  if Texts == 'subscriptions':
       repi = getallinfosubscriptions()
       Texts = input(colorText("[[red]]Enter Information [[magenta]]you [[green]]need [[black]]about user : "))





