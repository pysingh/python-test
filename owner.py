class Owner:
	
	owner_count = 0

	def __init__(self, owner_id, first_name, last_name, birthday):
		self.owner_id = Owner.owner_count + 1
		self.first_name = first_name
		self.last_name = last_name
		self.birthday = birthday
		Owner.owner_count = Owner.owner_count + 1

	def createOwner():
		print("\nEnter first_name: ")
		first_name = input()
		print("\nEnter last_name: ")
		last_name = input()
		print("\nEnter birthday: ")
		birthday = input()
		return Owner(first_name, last_name, birthday)

	def readOwner(self):
		print("Owner_details: \n\t first_name: %s, \n\t last_name: %s, \n\t birthday: %s" % (self.first_name, self.last_name, self.birthday));

	def updateOwner(self, first_name, last_name, birthday):
		self.first_name = first_name
		self.last_name = last_name
		self.birthday = birthday
	
	def deleteOwner():
		pass

	def getOwnerCount():
		return Owner.owner_count;