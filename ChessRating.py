
from bs4 import BeautifulSoup
import sys
import requests
from time import sleep

url = ["https://www.chess.com/members/view/riikkii#games","https://www.chess.com/tactics/stats"]
r = requests.get(url[0])
soup = BeautifulSoup(r.content,"html.parser")
z= soup.find("div",{"class":"clearfix stats-header"})
r= z.find("div",{"class":"right"})
l = r.contents
print("Blitz Rating :"+l[0])
