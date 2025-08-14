##accept an age input from the user and a full name
#if the age is less than 18 and the average is equal to 20
#print (name), you are not allowed to vote
#if the age is greater than or equal to 20, print (name), you are allowed to vote 
#if the age is greater than or equal to 18 or thge average is 18 , print (name), you are not allowed to vote



name = input("enter your\n")
age = int(input("enter your age\n"))
if age < 18 and int(average) == 20:
    print(f"{name}, you are not allowed to vote")