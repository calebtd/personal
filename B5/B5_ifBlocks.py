#Caleb Dillenbeck
#B5 Programming
#Demo of IF statements
#I did not copy anyone or anything but Mr. Blair :D

import shutil

#steve is lucky
name = input("What's your name?: ").lower()

if name == "steve":
  print("Congrats! You just won a free movie pass!")

yearInSchool = input("\nWhat year in school are you?: ").lower()

if yearInSchool == "freshmen":
  excited = input("\nAre you excited to go to Lone Peak?: ").lower()

elif yearInSchool == "sophomore":
  ready = input("\nAre you ready to drive?: ").lower()

#elif yearInSchool == "junior":

#elif yearInSchool == "senior":

#elif yearInSchool == "super senior"




columns = shutil.get_terminal_size().columns
print("\n\n\n\n")
print("G a m e   O v e r".center(columns))
