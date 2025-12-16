# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)
for subject in subjects:
    if subject == "History":
        break #stops the list from printing 
    print(subject)

for subject in subjects: 
    if subject == "Science":
        continue #skips over science but continues with the rest of the list
    print (subject)


# applicants_for_credit = ["Alice", "Bob", "Charlie", "David", "Eve"]
# credit_score = [720, 680, 590, 618, 750]

# for applicant, score in zip(applicants_for_credit, credit_score):
#     if score < 600:
#             continue
#     print (applicant + " approved for credit with score: " +str (score))

#Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"

for index in range (len(subjects)): 
      print ("Subject " + str(index) + ":" + subjects[index])
# Challenge:

# Given:

numbers = [5, 10, 15, 20]
total = 0 
#start with baseline
for number in numbers: 
    total += number#shortcut for total = total + number
print ("total :", total)


# Use a for loop to add all the numbers and print the total.
new_numbers = list(range(1,260001))
total = 0
for number in new_numbers:
     total += number
print ("total : " , total)