username= input("Please enter your name: ")
miles_driven= int(input("Enter how many miles you went: "))
gallons_used= int(input("Enter how many gallons of gas you used: "))
mpg=miles_driven/gallons_used
print()
print("Hello",username, end=',')
print(" here is your gas mileage:",mpg,"mpg")