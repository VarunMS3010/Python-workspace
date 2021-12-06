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
            

area = Area()

            