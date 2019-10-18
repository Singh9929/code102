name=input("Enter Your name:")
age=int(input("Enter your age:"))
if age==0:
	print("You can not watch")
elif 0<age<=10:
	print("half price")
elif 10<age<=50:
	print("full price")

else:
	print("Sponsered")		
