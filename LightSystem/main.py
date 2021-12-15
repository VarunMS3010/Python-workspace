from user import User


def main():
    print("Enter 0 for options\n")
    key = int(input('Enter the Key:  '))
    if(key == 0):
        user1 = User(key)
        user1.selectZone() 
    elif(key !=0):
            exit

    


    
if __name__ == "__main__":
    main()
        
        

        
        
        
