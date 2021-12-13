import area
 
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
            
        return key1




