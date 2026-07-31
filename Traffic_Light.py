while True:
    Colour= input("Enter the traffic colour you see: ").lower ()
    
    match Colour:
        
        case "red":
            print("Stop! wait till the light is green.")
            
        case "yellow":
            print("Slow down!, wait till the light is green.")
            
        case "green":
            print("You can go now. ")
            
        case _:
             print("Traffic light might be broken.")
             
    choice = input("Do you want to try again? \n(Yes/No): ").lower ()
    
    if choice == "no":
        print("Have a great day!")
        break
        
    elif choice in ["yes"]:
        print("Starting next round...\n")
        
    else:
        print("Invalid choice, but let's try again anyway!\n")
                 
