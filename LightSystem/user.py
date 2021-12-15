import area
import display
 
class User:
    
    def __init__(self, key):
        self.key = key
        
       
    def selectZone(self):
        area1 = area.Area()  # area obj1 area1 obj2
        disp = display.Display()
        if(self.key == 0): # check
            print("Select Zones\n")
            print("Enter 1 for  Room\n")
            print("Enter 2 for  Hall\n")
            print("Enter 3 for  Kitchen\n")
            key1 = int(input('Enter the Choice   :  '))
            
        if(key1 == 1):
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON Bedlamp \n")
            option = int(input("Enter to switch On the Load : "))
            print("Ground Floor, Room  \n ")
            area1.Room(option)
            print("To get status of Room zone")
            showDisplay = int(input("Enter 1 to get Load status\n"))
            if(showDisplay ==1):
                disp.ShowLoad(key1,option) 
            elif(showDisplay !=1):
                exit
            
        elif key1 == 2:
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON AC \n")
            option = int(input("Enter to switch On the Load : "))
            print("ground Floor, Hall \n")
            area1.hall(option)
            print("To get status of Hall zone")
            showDisplay = int(input("Enter 1 to get Load status\n"))
            if(showDisplay ==1):
             disp.ShowLoad(key1,option) 
            elif(showDisplay !=1):
                exit
            
        elif key1 == 3:
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON LED Bulb \n")
            option = int(input("Enter to switch On the Load : "))
            print("ground Floor, Kitchen \n")
            area1.Kitchen(option)
            print("To get status of Kitchen zone")
            showDisplay = int(input("Enter 1 to get Load status\n"))
            if(showDisplay ==1):
                disp.ShowLoad(key1,option) 
            elif(showDisplay !=1):
                exit
            
        elif key1> 3:
             exit   
            



