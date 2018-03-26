import owner
import dog
import cat
import psycopg2

conn = psycopg2.connect(database="bxd", user = "postgres", password = "root", host = "127.0.0.1", port = "5432")

def creat_admin_table():
	cur = conn.cursor()
	cur.execute('''CREATE TABLE OWNER
      (ID SERIAL PRIMARY KEY     NOT NULL,
      first_name           CHAR(100)    NOT NULL,
      last_name            CHAR(100)     NOT NULL,
      birthday        DATE);''')
	conn.commit()
	conn.close()

def creat_pets_table():
	cur = conn.cursor()
	cur.execute('''CREATE TABLE PETS
      (ID SERIAL PRIMARY KEY     NOT NULL,
      name           CHAR(100)    NOT NULL,
      owner_id       INT  UNIQUE     NOT NULL,
      type CHAR(50) NOT NULL,
      birthday        DATE);''')
	conn.commit()
	conn.close()

try:
	creat_admin_table()
except Exception as e:
	pass

try:
	creat_pets_table()
except Exception as e:
	pass

owner_list = []
dog_list = []
cat_list = []

def main():
	print "Select the correct category:\n 1. Owner\n 2. Dog \n 3. Cat "
	category = int(raw_input())
	if(category< 1 or category > 3):
		exit()
	if(category == 1):
		print "\n\nSelct desired operation:\n 1. Create\n 2. Read\n 3. Update\n 4. Delete "
		operation = int(raw_input())
		if(operation<1 or operation>3):
			exit()
		if(operation == 1):
			print "\nEnter first_name: "
			first_name = raw_input()
			print "\nEnter last_name: "
			last_name = raw_input()
			print "\nEnter birthday: "
			birthday = raw_input()
			tempOwner = Owner(first_name, last_name, birthday)
			owner_list.append(tempOwner)
		elif(operation == 2):
			if owner_list.length == 0:
				print "\nNo owner present\n"
			else :
				print "\nEnter owner Id to get the details"
				tempId = int(raw_input())
				temp = owner_list[0].getOwnerCount()
				if(tempId > temp):
					exit()
				owner_list[tempId].readOwner()
		elif operation == 3:
			if owner_list.length == 0:
				print "\nNo owner present\n"
			else :
				print "\nEnter owner Id to get the details"
				tempId = int(raw_input())
				temp = owner_list[0].getOwnerCount()
				if(tempId > temp):
					exit()
				print "\nEnter first_name: "
				first_name = raw_input()
				print "\nEnter last_name: "
				last_name = raw_input()
				print "\nEnter birthday: "
				birthday = raw_input()
				owner_list[tempId].updateOwner(first_name, last_name, birthday)
		else:
			if owner_list.length == 0:
				print "\nNo owner present\n"
			else :
				print "\nEnter owner Id to get the details"
				tempId = int(raw_input())
				temp = owner_list[0].getOwnerCount()
				if(tempId > temp):
					exit()
				owner_list = owner_list[:tempId] + owner_list[tempId+1:]
	elif category == 2:
		print "\n\nSelct desired operation:\n 1. Create\n 2. Read\n 3. Update\n 4. Delete "
		operation = int(raw_input())
		if(operation<1 or operation>3):
			exit()
		if(operation == 1):
			print "\nEnter name: "
			name = raw_input()
			print "\nEnter birthday: "
			birthday = raw_input()
			tempDog = Dog(name, birthday)
			dog_list.append(tempDog)
		elif(operation == 2):
			if dog_list.length == 0:
				print "\nNo Dog present\n"
			else :
				print "\nEnter dog Id to get the details"
				tempId = int(raw_input())
				temp = dog_list[0].getDogCount()
				if(tempId > temp):
					exit()
				dog_list[tempId].readDog()
		elif operation == 3:
			if dog_list.length == 0:
				print "\nNo Dog present\n"
			else :
				print "\nEnter dog Id to get the details"
				tempId = int(raw_input())
				temp = dog_list[0].getDogCount()
				if(tempId > temp):
					exit()
				print "\nEnter name: "
				name = raw_input()
				print "\nEnter birthday: "
				birthday = raw_input()
				dog_list[tempId].updateDog(name, birthday)
		else:
			if dog_list.length == 0:
				print "\nNo Dog present\n"
			else :
				print "\nEnter dog Id to get the details"
				tempId = int(raw_input())
				temp = owner_list[0].getDogCount()
				if(tempId > temp):
					exit()
				dog_list = dog_list[:tempId] + dog_list[tempId+1:]
	else:
		print "\n\nSelct desired operation:\n 1. Create\n 2. Read\n 3. Update\n 4. Delete "
		operation = int(raw_input())
		if(operation<1 or operation>3):
			exit()
		if(operation == 1):
			print "\nEnter name: "
			name = raw_input()
			print "\nEnter birthday: "
			birthday = raw_input()
			tempCat = Cat(name, birthday)
			cat_list.append(tempDog)
		elif(operation == 2):
			if cat_list.length == 0:
				print "\nNo Cat present\n"
			else :
				print "\nEnter cat Id to get the details"
				tempId = int(raw_input())
				temp = cat_list[0].getCatCount()
				if(tempId > temp):
					exit()
				cat_list[tempId].readCat()
		elif operation == 3:
			if cat_list.length == 0:
				print "\nNo Cat present\n"
			else :
				print "\nEnter cat Id to get the details"
				tempId = int(raw_input())
				temp = cat_list[0].getCatCount()
				if(tempId > temp):
					exit()
				print "\nEnter name: "
				name = raw_input()
				print "\nEnter birthday: "
				birthday = raw_input()
				cat_list[tempId].updateCat(name, birthday)
		else:
			if cat_list.length == 0:
				print "\nNo Cat present\n"
			else :
				print "\nEnter cat Id to get the details"
				tempId = int(raw_input())
				temp = cat_list[0].getCatCount()
				if(tempId > temp):
					exit()
				cat_list = cat_list[:tempId] + cat_list[tempId+1:]
		