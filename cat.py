class Cat:
		
	cat_count = 0

	def __init__(self, cat_id, name, birthday, owner_id):
		self.cat_id = cat.cat_count + 1
		self.name = name
		self.birthday = birthday
		Cat.cat_count = Cat.cat_count + 1
		self.owner_id = owner_id

	def createcat():
		print("\nEnter name: ")
		name = input()
		print("\nEnter birthday: ")
		birthday = input()
		return Owner(name, birthday)

	def readcat(self):
		print("cat_details: \n\t name: %s, \n\t birthday: %s" % (self.name, self.birthday));

	def updatecat(self, name, birthday, owner):
		self.name = name
		self.birthday = birthday
		self.owner_id = owner
	
	def deleteOwner():
		pass

	def getCatCount():
		return Cat.cat_count;