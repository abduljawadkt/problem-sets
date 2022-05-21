email = input()
#enter email
branch = email[:2] 
degree = email[3: 5] 
year = email[6:8] 
roll = email[9:13] 
institute = email[-10:-6] 
#above 5 lines will collect respective data from the email
print(branch) 
print(degree) 
print(year) 
print(roll) 
print(institute) 
