#intro interphase
#selecting service
service=['1.Individual input','2.Daily input','3.Report']
print("choose the service from the following")
print(service)

net_income=0
net_expense=0
balance=0
#choosing service and redirecting to it
serv=int(input("Enter Here: "))
while (serv>3 or serv<1):
  print("invalid syntax")
  serv=int(input("Enter Here: "))

#adding service 1
if serv==1:
  out1=0
  serv1=int(input("Enter Income/Expense here(use negative sign if it is expense): "))
  balance=balance+serv1
  if serv1>0:
    net_income=net_income+serv1
    balance=balance+net_income
  else:
    net_expense=net_expense+serv1
    balance=balance+net_expense
  
#daily input
elif serv==2:
  net=0
  x=int(input("Enter your Today's Expense : "))
  y=int(input("Enter your Today's income Here: "))
  net_expense=net_expense+x
  net_income=net_income+y
  balance=balance+net


#calculating percentage
ratio=net_expense/net_income  
perc=ratio*100
#showing balance
print("your current bank balance is Rs.", balance)


#basic final report with if else
if serv==3:
  if (ratio>=y*0.6):
   print("congrats,your today's expense is only",perc,"percentage of your income,keep saving,we will introduce you better financial plannings soon")
  elif(ratio>=0.3 and ratio<0.6):
   print("Good,your today's expense is only",perc,"percentage of your income,keep maintaining your expenses")
  elif(ratio>=0 and ratio<0.3):
   print("Alert!!!...you spent almost",perc,"percentage of the income today.think before spending")
  else:
   print("Alert....your today's expense is morethan income.you have better to reduce the expenses or increase the income daily")
  #end 
