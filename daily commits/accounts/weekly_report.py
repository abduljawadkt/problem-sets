def days():
  print("1.Sunday")
  print("2.Monday")
  print("3.Tuesday")
  print("4.Wednesday")
  print("5.Thursday")
  print("6.Friday")
  print("7.saturday")


#intially we are summing up the expenses
x=int(input("Enter your Today's Expense : "))
y=int(input("Enter your Today's income Here: "))

net=y-x

#print(net)
#setting balance
balance=0
balance=balance+net

#calculating percentage
ratio=x/y
perc=ratio*100
#showing balance
print("your current bank balance is Rs.", balance)

#basic final report with if else
if (ratio>=y*0.6):
  print("congrats,your today's expense is only",perc,"percentage of your income,keep saving,we will introduce you better financial plannings soon")
elif(ratio>=0.3 and ratio<0.6):
  print("Good,your today's expense is only",perc,"percentage of your income,keep maintaining your expenses")
elif(ratio>=0 and ratio<0.3):
  print("Alert!!!...you spent almost",perc,"percentage of the income today.think before spending")
else:
  print("Alert....your today's expense is morethan income.you have better to reduce the expenses or increase the income daily")
  #end 
#weekly report problem
days()
choice=input()
for l in days():
  
    