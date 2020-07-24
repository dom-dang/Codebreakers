# A fun group project where we made a fortune teller that takes input for a user's birthday


def fortune_teller():
    user_input = input ("What month is your birthday?")
    
    if (user_input == "January" or user_input == "january"):
        print("No snowflake in an avalanche ever feels responsible")
    
    elif (user_input == "February" or user_input == "february"):
        print("A dubious friend may be an enemy in camouflage.")
    
    elif (user_input == "March" or user_input == "march"):
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    
    elif (user_input == "April" or user_input == "april"):
        print("Error 404: Fortune not found.")
        
    elif (user_input == "May" or user_input == "may"):
        print("If you eat something and nobody sees you eat it, it has no calories.")
        
    elif (user_input == "June" or user_input == "june"):
        print("Don’t worry; prosperity will knock on your door soon.")
        
    elif (user_input == "July" or user_input == "july"):
        print("Embrace the glorious mess that you are.")
        
    elif (user_input == "August" or user_input == "august"):
        print("Do it now! Today will be yesterday's tomorrow... or something")
        
    elif (user_input == "September" or user_input == "september"):
        print("When a door closes, another opens.")
        
    elif (user_input == "October" or user_input == "october"):
        print("Good news will come to you by mail.")
        
    elif (user_input == "November" or user_input == "november"):
        print("New ideas could be profitable.")
        
    elif (user_input == "December" or user_input == "december"):
        print("You have been choosen for the Hunger Games.")
    
    else:
        print("Fortune Not Found: Abort, Retry, Ignore?")
    
    

    user_input2 = int(input("What day is your birthday(int)?"))
        
    if (user_input2 %2 ==0 and user_input2 <=31 and user_input2>0):
        print("Change is happening in your life, so go with the flow!")

    elif (user_input2 %2 ==1 and user_input2 <=31 and user_input2>0):
        print("You are in good hands this evening.")
        
    else:
        print ("Fortune Not Found: Abort, Retry, Ignore?")
    
    
    
    user_input3 = int(input("What year were you born?"))
    
    if (user_input3 <= 2005 and user_input3 > 2001):
        print("Ignore the previous cookie.")
    
    elif (user_input3 > 2005 and user_input3 < 2021 ):
        print("Here are the winning lottery numbers for December 27, 2032: 2, 17, 9, 25, 40, 7.")
    
    elif (user_input3  <= 2001):
        print("You are the crispy noodle in the vegetarian salad of life.")
      
    else:
        print("Fortune Not Found: Abort, Retry, Ignore?")
        
        
    print("Thank you for utilizing our automatic fortune teller. Come back again!")
