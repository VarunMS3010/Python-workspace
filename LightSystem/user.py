import area
import display

class User:

    def __init__(self, key):
        self.key = key


    def selectZone(self):
        area1 = area.Area()  # area obj1 area1 obj2
        disp = display.Display()
        if(self.key == 0): # check
            print("Zone's Available \n")
            print(" 1 -> Room\n")
            print(" 2 -> Hall\n")
            print(" 3 ->  Kitchen\n")
            key1 = int(input('Select the Zone:  '))  # key 1 is for zone selction

        if(key1 == 1):
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON Bedlamp \n")
            option = int(input("Enter Keypad Number to turn ON Load : ")) # option for load selection
            print("Ground Floor, Room  \n ")
            area1.Room(option)    #Calling Area.Room() fun
            print("To get status of Room zone")
            showDisplay = int(input("Enter '1' to get Load status\n"))
            if(showDisplay ==1):
                disp.ShowLoad(key1,option)
            elif(showDisplay !=1):
                exit

        elif key1 == 2:
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON AC \n")
            option = int(input("Enter Keypad Number to turn ON Load : "))
            print("ground Floor, Hall \n")
            area1.hall(option)
            print("To get status of Hall zone")
            showDisplay = int(input("Enter '1' to get Load status\n"))
            if(showDisplay ==1):
             disp.ShowLoad(key1,option)
            elif(showDisplay !=1):
                exit

        elif key1 == 3:
            print("Enter 1 to turn ON Flurocent Lamp\n")
            print("Enter 2 to turn ON fan \n")
            print("Enter 3 to turn ON LED Bulb \n")
            option = int(input("Enter Keypad Number to turn ON Load : "))
            print("ground Floor, Kitchen \n")
            area1.Kitchen(option)
            print("To get status of Kitchen zone")
            showDisplay = int(input("Enter '1'to get Load status\n"))
            if(showDisplay ==1):
                disp.ShowLoad(key1,option)
            elif(showDisplay !=1):
                exit

        # elif key1 ==4:
        #     disp.ShowLoad(key1,option)

        elif key1> 4:
            print("Invaild Load option")
            endoption = int(input( "Enter '0' to exit and '1' to continue "))
            if(endoption == 0):
                exit
            elif(endoption == 1):
                User.selectZone(self)




