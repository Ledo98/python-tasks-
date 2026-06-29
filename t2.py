#  Task 2 - Job Eligibility Portal #
print ("**********  Welcome TO MOhamed Waleed Second Task  **********")
the_first_condition=  input("DO You Master Python ? (yes/no)")
the_first_condition= str(the_first_condition)
the_second_condition= input("How many years of experience or projects? ?")
the_second_condition= float(the_second_condition)
the_thrid_condition= input("Does he have a university degree in computing, or has he completed an intensive bootcamp? (yes/no)")
the_thrid_condition= str(the_thrid_condition)

if (the_first_condition == "yes") and (the_second_condition>=2 or the_thrid_condition== "no") :
  print ("Congratulations! You have been accepted for the next stage of interviews.")
else :
  print("Sorry, your current qualifications do not match the job requirements.")

