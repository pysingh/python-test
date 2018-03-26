class Dog:
		
	dog_count = 0

	def __init__(self, dog_id, name, birthday, owner_id):
		self.dog_id = Dog.dog_count + 1
		self.name = name
		self.birthday = birthday
		Dog.dog_count = Dog.dog_count + 1
		self.owner_id = owner_id

	def createDog():
		print("\nEnter name: ")
		name = input()
		print("\nEnter birthday: ")
		birthday = input()
		return Owner(name, birthday)

	def readDog(self):
		print("Dog_details: \n\t name: %s, \n\t birthday: %s" % (self.name, self.birthday));

	def updateDog(self, name, birthday, owner):
		self.name = name
		self.birthday = birthday
		self.owner_id = owner
	
	def deleteDog():
		# delete dog here
		#cur.execute("DELETE from PETS where ID=owner_id AND type='DOG';")
		pass

	def getDogCount():
		return Dog.dog_count;