import os
import math

import random
import time
import pyfiglet



def datasec():
	os.system("cd theme/DataSec && python main.py")


def colorlib():
	os.system("cd theme/ColorLib && python main.py")
	
	

	
	
	
	




def main():
	print("==================================================")
	banner = pyfiglet.figlet_format("WebAi - Gen")
	print(banner)
	print("==================================================")
	time.sleep(2)
	print("Ai: Hello, Select your theme..")
	print("1] Colorlib 2] DataSec")
	print("3] Colorlib2 4] DataSec2")
	print("----Exit----")
	input1 = input("Enter Your Option: ")
	if input1 == "1":
		colorlib()
	elif input1 == "2":
		datasec()
	elif input1 == "3":
		print("Not Working... Coming Soon..")
		print("Return in 5 second")
		time.sleep(5)
		main()
	elif input1 == "4":
		print("Not Working... Coming Soon..")
		print("Return in 5 second")
		time.sleep(5)
		main()
	elif input1 == "exit":
		exit()
	else :
		main()

main()