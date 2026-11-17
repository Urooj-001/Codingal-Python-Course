#Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.

#What you need to use
#------------------------------------------------------------------------
#1.  dictionary      →  store at least 5 student name-score pairs
#2.  for loop        →  to calculate the class average
#3.  max() min()     →  to find the top and bottom scorer
#4.  .get()          →  to look up a student by name
#5.  input()         →  to let the user search for a student

grade_book = { "Alice" : 89 , "Miya" : 78 , "Alex" : 90 , "Rory" : 96 , "Xavier" : 65 }
total = 0
for i in grade_book.values():
    total = total + i

class_avg = total / len(grade_book)
print(class_avg)

top_score = max(grade_book.values())
print(top_score)
bottom_score = min(grade_book.values())
print(bottom_score)

search = input("Enter students name: ")

