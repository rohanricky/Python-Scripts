import notify2
from bs4 import BeautifulSoup

notify2.init("Demo application")

 
n = notify2.Notification("Summary", "Body text goes here",
            "notification-message-im") 

n.show()

