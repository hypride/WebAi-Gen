import os
import math
import random
import time
import pyfiglet



def personal():
	personal_theme_list = ['os.system("cd theme/DataSec && python main.py")', 'os.system("cd theme/ColorLib && python main.py")']
	exec(random.choice(personal_theme_list))



def main():
	print("==================================================")
	banner = pyfiglet.figlet_format("WebAi - Gen")
	print(banner)
	print("==================================================")
	time.sleep(2)
	print("Ai: Hello, Select your theme..")
	print("1] Personal Websites")
	print("2] Company Websites")
	print("3] Internet forum")
	print("----Exit----")
	input1 = input("Enter Your Option: ")
	if input1 == "1":
		personal()
	elif input1 == "2":
		print("Not Working... Coming Soon..")
		print("Return in 5 second")
		time.sleep(5)
		main()
	elif input1 == "3":
		print("Not Working... Coming Soon..")
		print("Return in 5 second")
		time.sleep(5)
		main()
	elif input1 == "exit":
		exit()
	else :
		main()

main()
