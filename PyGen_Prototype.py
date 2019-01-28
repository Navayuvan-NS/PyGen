import os 

def create_add_program():
	with open("add.py", "w") as add:
		prgm = []
		prgm.append("x = int(input(\"Enter the number 1:\"))")
		prgm.append("y = int(input(\"Enter the number 2:\"))")
		prgm.append("print(\"The Result is \", x + y)")
		for x in prgm:
			add.write(x + "\n")

def create_sub_program():
	with open("sub.py", "w") as add:
		prgm = []
		prgm.append("x = int(input(\"Enter the number 1:\"))")
		prgm.append("y = int(input(\"Enter the number 2:\"))")
		prgm.append("print(\"The Result is \", x - y)")
		for x in prgm:
			add.write(x + "\n")

def create_mul_program():
	with open("mul.py", "w") as add:
		prgm = []
		prgm.append("x = int(input(\"Enter the number 1:\"))")
		prgm.append("y = int(input(\"Enter the number 2:\"))")
		prgm.append("print(\"The Result is \", x * y)")
		for x in prgm:
			add.write(x + "\n")


def create_mul_program():
	with open("div.py", "w") as add:
		prgm = []
		prgm.append("x = int(input(\"Enter the number 1:\"))")
		prgm.append("y = int(input(\"Enter the number 2:\"))")
		prgm.append("print(\"The Result is \", x / y)")
		for x in prgm:
			add.write(x + "\n")


print("\t\t\t\tWelcome to Python Program Generator")
print("\t\t\t\t-----------------------------------")
while(True):
	print("File Options \n1. Create program file \n2. Delete program file \nEnter any other option to Exit")
	m_input = int(input("Choose your option:"))
	if m_input == 1:

		print("Program Generator Options")
		print("1. Addition of Two numbers program \n2. Subraction of Two numbers program \n3. Multiplication of Two numbers program \n4. Division of Two numbers program \n")

		generator_option = int(input("What is your choice?"))

		if generator_option == 1:
			print("Generating Addition of Two numbers Program.....")
			create_add_program()
			print("Program Generated Successfully !!! \n\n\n")
			run_option = input("would you want to run it? (Y / N)")
			if run_option.lower() == "y":
				os.system("python add.py")


		elif generator_option == 2:
			print("Generating Subraction of Two numbers Program......")
			create_sub_program()
			print("Program Generated Successfully !!! \n\n\n")	
			run_option = input("would you want to run it? (Y / N)")
			if run_option.lower() == "y":
				os.system("python sub.py")

		elif generator_option == 3:
			print("Generating Multiplication of Two numbers Program......")
			create_mul_program()
			print("Program Generated Successfully !!! \n\n\n") 
			run_option = input("would you want to run it? (Y / N)")
			if run_option.lower() == "y":
				os.system("python mul.py")

		elif generator_option == 4:
			print("Generating Division of Two numbers Program...")
			create_div_program()
			print("Program Generated Successfully !!! \n\n\n")
			run_option = input("would you want to run it? (Y / N)")
			if run_option.lower() == "y":
				os.system("python div.py")

	elif m_input == 2:
		print("\t\t\t\tWelcome to File Destructor")
		print("\t\t\t\t--------------------------")
		print("Options available to delete \n1. add.py \n2. sub.py \n3. mul.py \n4. div.py \n5. Delete all files generated")
		del_option = int(input("Enter your choice :"))

		if del_option == 1:
			try:
				os.remove("add.py")
				print("File deleted Successfully \n\n\n")
			except:
				print("File not found !!!")

		elif del_option == 2:
			try:
				os.remove("sub.py")
				print("File deleted Successfully \n\n\n")
			except:
				print("File not found !!!")

		elif del_option == 3:
			try:
				os.remove("mul.py")
				print("File deleted Successfully \n\n\n")
			except:
				print("File not found !!!")

		elif del_option == 4:
			try:
				os.remove("div.py")
				print("File deleted Successfully \n\n\n")
			except:
				print("File not found !!!")

		elif del_option == 5:
			try:
				os.remove("add.py")
				os.remove("sub.py")
				os.remove("mul.py")
				os.remove("div.py")
				print("Files deleted Successfully \n\n\n")
			except:
				print("File not found !!!")
	else:
		break
