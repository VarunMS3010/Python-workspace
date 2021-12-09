class Area: 

    def Room(self,option1):# zone1 
        self.option1 = option1
        if(option1 == 1):
            print("Flurocent Lamp is On\n")

        if(option1 == 2):
            print("fan is On\n")

        if(option1 == 3):
            print("Bedlamp  is On\n")

    def hall(self,option2):
        self.option2 = option2
        if(option2 == 1):
            print("Flurocent Lamp is On\n")

        if(option2 == 2):
            print("fan is On\n")

        if(option2 == 3):
            print("AC  is On\n")

    def Kitchen(self,option3):
        self.option3 = option3
        if(option3 == 1):
            print("Flurocent Lamp is On\n")

        if(option3 == 2):
            print("fan is On\n")

        if(option3 == 3):
            print("AC  is On\n")
            
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
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON AC \n")
            option1 = int(input("Enter to switch On the Load : "))
            print("Ground Floor, Room  \n ")
            area.Room(option1)
        elif key1 == 2:
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON AC \n")
            option2 = int(input("Enter to switch On the Load : "))
            print("ground Floor, Hall \n")
            area.hall(option2)
        elif key1 == 3:
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON AC \n")
            option3 = int(input("Enter to switch On the Load : "))
            print("ground Floor, Kitchen \n")
            area.Kitchen(option3)

print("Enter 0 for options\n")
key = int(input('Enter the Key:  '))
user = User()
area = Area()
user.selectZone(key)

class Display(Area): #
    
    def show(self):
        if(area.option1 == 1):
            print("Display\n")
            print("Ground Floor, Room\t")
            print("Flurocent Lamp is On\n")
        elif(area.option1 == 2):
            print("Display\n")
            print("Ground Floor, Room\t")
            print("fan is On\n")
        elif(area.option1 == 3):
            print("Display\n")
            print("Ground Floor, Room\t")
            print("AC is On\n")
            
    # def show1(self):
        elif(area.option2 == 1):
                print("Display\n")
                print("ground Floor, Hall \t")
                print("Bedlamp Lamp is On\n")
        elif(area.option2 == 2):
                print("Display\n")
                print("ground Floor, Hall \t")
                print("Fan is On\n")
        elif(area.option2 == 3):
                print("Display\n")
                print("ground Floor, Hall \t")
                print("AC is On\n")
                
    # def show2(self):
        elif(area.option3 == 1):
                print("Display\n")
                print("ground Floor, Kitchen \t")
                print("Bedlamp Lamp is On\n")
        elif(area.option3 == 2):
                print("Display\n")
                print("ground Floor, Kitchen \t")
                print("Fan is On\n")
        elif(area.option3 == 3):
            print("Display\n")
            print("ground Floor, Kitchen \t")
            print("AC is On\n")
            
            
display = Display()

# if area.option1 != 0:
display.show()
# elif area.option2 != 0:
#     area.display.show1(option2)
# elif area.option3 != 0:
#     area.display.show2(option3)