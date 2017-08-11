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

	def help_add(self):
		print("I've done it")

	

offo = MyCommandInterpreter()
offo.cmdloop()