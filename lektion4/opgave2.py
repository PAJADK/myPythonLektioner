while True:
    age = int(input("\nHow old are you?: "))
    if age < 3:
        print("The ticket is free.")
        #break
    elif 3 <= age <= 12:
        print("The ticket is $10")
       # break
    else:
        print("The ticket is $15")
        #break

