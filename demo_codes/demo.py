
class Person:

    def __init__(self, first, last, place):
        self.firstname = first
        self.lastname = last
        self.place = place

    def Name(self):
        return self.firstname + " " + self.lastname + " , " +self.place
    


class Employee(Person):

    def __init__(self, first, last, place, Eid,Bu,WLocation):
        Person.__init__(self, first, last, place)
        self.Eid = Eid
        self.Bu = Bu
        self.WLocation = WLocation

    def GetEmployee(self):
        print("Employee data")
        return self.Name() + ", " + self.Eid + ", " + self.Bu + ", " + self.WLocation



y = Employee("Ajay", "Kumar", "Hpt" , "990056", "IPC", "Mysuru")
y1 = Employee("Ravi", "Kumar", "bangalore" , "990057", "IPC", "Mysuru") 

print(y.GetEmployee())
print(y1.GetEmployee())


#ctor example program


# class Addition:
#    first = 0
# 	second = 0
# 	answer = 0
	
# 	# parameterized constructor
# 	def __init__(self, f, s):
# 		self.first = f
# 		self.second = s
	
# 	def display(self):
# 		print("First number = " + str(self.first))
# 		print("Second number = " + str(self.second))
# 		print("Addition of two numbers = " + str(self.answer))

# 	def calculate(self):
# 		self.answer = self.first + self.second

# # creating object of the class
# # this will invoke parameterized constructor
# obj = Addition(1000, 2000)

# # perform Addition
# obj.calculate()

# # display result
# obj.display()
