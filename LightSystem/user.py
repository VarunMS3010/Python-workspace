import area
 
class User:
       
    def selectZone(self,key):
        self.key= key
        area1 = area.Area()  # area obj1 area1 obj2
        if(key == 0):
            print("Select Zones\n")
            print("Enter 1 for  Room\n")
            print("Enter 2 for  Hall\n")
            print("Enter 3 for  Kitchen\n")
            key1 = int(input('Enter the Choice   :  '))
        if(key1 == 1):
            option = int(input("Enter to switch On the Load : "))
            print("Ground Floor, Room  \n ")
            area1.Room(option)
        elif key1 == 2:
            option = int(input("Enter to switch On the Load : "))
            print("ground Floor, Hall \n")
            area1.hall(option)
        elif key1 == 3:
            option = int(input("Enter to switch On the Load : "))
            print("ground Floor, Kitchen \n")
            area1.Kitchen(option)
            




