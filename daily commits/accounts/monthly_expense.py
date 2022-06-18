#building a monthly expense calculator

#Greeting
print("Welcome to budget estimator!!!")

#total income of the month
income=float(input("Enter your monthly income: "))
additionals=float(input("Enter your additional income in this month: "))

total_income=income+additionals

print("your total income of the month is ",str(total_income))

print("Now let's Get some expenses....")

#total expense of the month 

#defining function to collect all the expenses
def gather_expense():
  housing=float(input("Enter your home budget of this month: "))
  food=float(input("Enter your monthly food related expenses: "))
  travel=float(input("Enter your total travel expense of the month: "))
  additional=float(input("Enter you additional expenses of this month: "))
  total_expense=housing+food+travel+additional
  return total_expense

monthly_expense=gather_expense()  

print("Your total expense of this month is",str(monthly_expense))
#margin_section
margin=total_income-monthly_expense

if margin>=0:
  print("Your total surplus of next month will be",margin)
else:
  print("You will come up" +str(margin)+ "negative")

#end
print("Thank you for using monthly budget calculator") 