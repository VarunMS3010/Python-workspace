from user import User


def main():
    print("Enter 0 for options\n")
    key = int(input('Enter the option:  '))
    if(key == 0):
        user1 = User(key)
        user1.selectZone()
    elif(key !=0):
        print("Invaild option")
        zonekey = int(input("Enter '0' to exit and '1' and to continue "))
        if(zonekey == 0):
            exit
        elif(zonekey == 1):
            main()





if __name__ == "__main__":
    main()






