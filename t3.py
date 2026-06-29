# Task 3 - Smart ATM Simulator #
print ("**********  Welcome TO MOhamed Waleed Thrid Task  **********")
print ("Please Enter Your Pin")
pin=input()

if pin == "1234" :
    print ("########## Welcome To your Account Profile At Ledo Bank ##########")
    print ("What Would You Like To Do ?")
    first_condition= print("1. Withdraw")
    second_condition=print("2. Check Balance")
    choice=input()
    choice=int(choice)
    if choice ==1 :
      print ("How Much Would You Like To Withdraw ?")
      withdraw=input()
      withdraw=int(withdraw)
      if withdraw>5000 :
        print ("Sorry, your balance is insufficient.")
      else:
        print("The transaction was successful. Your remaining balance is" , 5000-withdraw , "$")

    else :
      Balance= int(5000)
      print ("Your Balance Is =" , Balance , "$")

else :
  print("Incorrect Pin , please enter the correct pin")
