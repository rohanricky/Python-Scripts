
# Basic script to implement command line interface

from cmd import Cmd
import os
import webbrowser
from cmd import Cmd

class MyCommandInterpreter(Cmd):
	def do_add(self,s):
		l = s.split()
		if(len(l)!=2):
			print("Invalid Arguments")

		try:
			 l = [int(i) for i in l]

		except ValueError:
			print("Arguments should be numbers")
			return

		print(l[0]+l[1])

	def do_web(self,s):
		url = "https:www."+ s +".com/"
		webbrowser.open_new_tab(url)

	def do_whatsapp(self,s):
		url = "https://web.whatsapp.com/"
		webbrowser.open_new_tab(url)


offo = MyCommandInterpreter()
offo.cmdloop()

	def help_add(self):
		print("I've done it")



offo = MyCommandInterpreter()
offo.cmdloop()
