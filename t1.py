# Task 1 - Instant Discount System #
print ("**********  Welcome TO MOhamed Waleed First Task  **********")
total_price_of_client=input("Please Enter The TOtal Price :")
total_price_of_client=float(total_price_of_client)

if total_price_of_client < 100 :
  discount=0
  total_price_after_discount=total_price_of_client
  print ("Your Avaliable Discount Is =" , discount)
  print ("Total price after discount =", total_price_after_discount)
elif total_price_of_client >= 100 and total_price_of_client < 500 :
  discount=0.1
  total_price_after_discount=total_price_of_client - total_price_of_client * (discount)
  print ("Your Avaliable Discount Is =" , discount*100 , "%")
  print ("Total price after discount =", total_price_after_discount)
else :
  discount=0.2
  total_price_after_discount=total_price_of_client - total_price_of_client * (discount)
  print ("Your Avaliable Discount Is =" , discount*100 , "%")
  print ("Total price after discount =", total_price_after_discount)