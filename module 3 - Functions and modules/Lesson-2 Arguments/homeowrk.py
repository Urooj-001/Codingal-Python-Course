def shutdown():
    choice=input("Do you want to shut down your computer? (yes/no): ").lower()
    if choice == "yes":
        print("COMPUTER SHUTTING DOWN. Have a good day.")
    elif choice == "no":
        print("OKAY COMPUTER NOT SHUTTING DOWN.")
    else:
        print("Sorry, invalid input.")

shutdown() 