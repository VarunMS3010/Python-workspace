class Display():
       
    def ShowLoad(self, key1, option):
        self.key1 = key1 # zone selection option
        self.option = option # load selection option
        
        if(self.key1 == 1):
            print("You are in Room\n")
            if(self.option != 0):
                if(self.option == 1) :
                    print("Flurocent Lamp is ON\n" "fan is OFF\n" "Bedlamp  is OFF\n")
                elif(self.option == 2) :
                     print("fan is ON\n" "Flurocent Lamp is OFF\n"  "Bedlamp  is OFF\n")
                elif(self.option == 3) :
                    print("Bedlamp  is ON\n" "fan is OFF\n" "Flurocent Lamp is OFF\n")
                elif(self.option > 3):
                    print("Flurocent Lamp is OFF\n" "fan is OFF\n" "Bedlamp  is OFF\n")
                    
        elif(self.key1 == 2):
            print("You are in hall\n")
            if(self.option != 0):   
                if(self.option ==1):
                    print("Flurocent Lamp is ON\n" "Fan is Off\n" "AC is OFF\n")
                elif(self.option == 2):
                    print("Fan is ON\n" "Flurocent Lamp is Off\n" "AC is OFF\n" )
                elif(self.option == 3):
                    print(" AC is ON\n" "Flurocent Lamp is Off\n" "Fan is OFF\n" )
                elif(self.option > 3):
                    print("Flurocent Lamp is OFF\n" "Fan is Off\n" "AC is OFF\n")
                
            
            
        elif(self.key1 ==3):
            print("You are in Kitchen\n")
            if(self.option != 0):
                if(self.option ==1):
                    print("Flurocent Lamp is ON\n" "Fan is Off\n" "LED Bulb is OFF\n" )
                elif(self.option ==2):
                    print("Fan is ON\n" "Flurocent Lamp  is Off\n" "LED Bulb is OFF\n" )
                elif(self.option ==3):
                    print("LED Bulb is ON\n" "Flurocent Lamp  is Off\n" "Fan is OFF\n" )
                elif(self.option > 3):
                     print("Flurocent Lamp is OFF\n" "Fan is Off\n" "LED Bulb is OFF\n" )
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
            
            