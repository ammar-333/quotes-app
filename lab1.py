import random
import sys


def starting():
  print("\n*********************************************************************")
  print("\nmenu:"),
  print("1. Add a new quote"),
  print("2. Quote of the day"),
  print("3. Print all quotes with likes"),
  print("4. Print the most preferable quote"),
  print("5. Exit"),


def call():
  a=(input("Enter your choice:"))
  print(" ")
  if a=='1':
    add()
  elif a=='2':
    quote_of_day()
  elif a=='3':
    print_all()
  elif a=='4':
    most_preferable()
  else:
    exit()


def add():
  x=input("Enter the new quote: ")
  quotes.append(x)
  likes.append(0)
  print("Quote added successfully!")


def quote_of_day():
  print("Quote of the day:")
  x=quotes[random.randint(0,len(quotes)-1)]
  print(x)
  y=input("Did you like this qoute? (yes/no):")
  if y=='yes':
    print("Thank you for liking the qoute!")
    likes[quotes.index(x)] +=1
  else:
    print("Thank you")


def print_all():
  print("All Quotes:")
  for i in range(len(quotes)):
    print(quotes[i]," likes:",likes[i])


def most_preferable():
  print("most preferable quote:")
  x=likes.index(max(likes))
  print(quotes[x]," likes:",max(likes))


def exit():
  print("Exiting the program, Goodbye\n\n")
  sys.exit()



quotes=["Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"]
likes=[0,0,0]



'''*****************************************************************starting of execution************************************************************************'''
print(quotes[random.randint(0,len(quotes)-1)])
while True:
  starting()
  call()