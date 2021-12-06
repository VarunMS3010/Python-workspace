class Area: 

    def Room(self,option):
        self.option = option
        if(option == 1):
            print("Flurocent Lamp is On\n")
            print("Enter 1 for other Load to On: ")
            key3 = int(input())
            if(key3 == 1):
                area.Room(option)

        if(option == 2):
            print("fan is On\n")

        if(option == 3):
            print("Bedlamp Lamp is On\n")

    def hall(self,option):
        self.option = option
        if(option == 1):
            print("Flurocent Lamp is On\n")

        if(option == 2):
            print("fan is On\n")

        if(option == 3):
            print("AC Lamp is On\n")

    def Kitchen(self,option):
        self.option = option
        if(option == 1):
            print("Flurocent Lamp is On\n")

        if(option == 2):
            print("fan is On\n")

        if(option == 3):
            print("AC Lamp is On\n")
            
class User:
    
    def selectZone(self,key):
        self.key= key
        if(key == 0):
            print("Select Zones\n")
            print("Enter 1 for  Room\n")
            print("Enter 2 for  Hall\n")
            print("Enter 3 for  Kitchen\n")
            key1 = int(input('Enter the Choice   :  '))
        if(key1 == 1):
            option = int(input("Enter to switch On the Load : "))
            print("Ground Floor, Room  \n ")
            area.Room(option)
        elif key1 == 2:
            option = int(input("Enter to switch On the Load : "))
            print("ground Floor, Hall \n")
            area.Hall(option)
        elif key1 == 3:
            option = int(input("Enter to switch On the Load : "))
            print("ground Floor, Kitchen \n")
            area.Kitchen(option)

print("Enter 0 for options\n")
key = int(input('Enter the Key:  '))
user = User()
area = Area()
user.selectZone(key)