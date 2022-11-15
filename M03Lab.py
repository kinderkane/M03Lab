class Vehicle:
	def __init__(self,type):   
		self.type=type 


class Automobile(Vehicle):
	def __init__(self,type,year,make,model,doors,roof):
		super().__init__(type) 
		self.year=year
		self.make=make
		self.model=model
		self.doors=doors
		self.roof=roof

type=input("Please enter the type of vehicle: ")
year=input("Enter the year: ")
make=input("Enter the make: ")
model=input("Enter the model: ")
doors=input("Enter how many doors(2 or 4): ")
roof=input("Enter roof type (solid or sun roof): ")

type.upper()
make.upper()
model.upper()
roof.upper()

print('\n')
print('\n')
print("Vehicle Type: " + type)
print("Year: " + year)
print("Make: " + make)
print("Model: " + model)
print("No of doors: " + doors)
print("Type of roof: " + roof)