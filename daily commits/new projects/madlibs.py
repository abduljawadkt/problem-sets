#string concatenation
#suppose we want to create a string that says 'subscribe to _____'
#3 ways we checking
#youtuber="tech travel eat"

#print("subscribe to" + youtuber)
#print("subsctibe to {}".format(youtuber))
#usage of fstring
#print(f"subscribe to {youtuber}")


#lets move into madlib now
#job analysis
job=input("Enter specified job: ")
feel0=input("your opinion about that job: ")
feel1=input("How you feels about it: ")
person=input("who is that person famous in this field: ")
feel2=input("How you feel about him: ")
madlib = f"{job}ing is a verymuch {feel0} process.i {feel1} to that job.sometimes i feel {feel2} about {person} that he is doing {job}ing."
print(madlib)