# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  
# for loops=execute a block of code a fixed number of times. 
#u iterate over a range, string, sequence, etc. 

for x in range (1, 23):
    if x == 13:
        break #once you reach 13 you escape the loop
    else:
        print (x)

for x in range (1,11,2): #prints 1(inclusive) to 11(exclusive) and counts by 2s
    print (x)

#WILDLOOPS
#execute code WHILE some conditions remain true

#while loop is execute some code while some condition remains true
#IF ELSE
name = input ("Enter your name")

if name == "":
    print ("You did not enter your name")
else: 
    print (f"Hello {name}")

    name = input ("Enter your name")

# #WHILE ELSE//infinitly asks you your name
name = input ("Enter your name")
while name == "":
    print ("You did not enter your name")
    name = input ("Enter your name")
else: 
    print (f"Hello {name}")

name = input ("Enter your name")
while name == "":
    print ("You did not enter your name")

print (f"Hello {name}") #infinite and does not stop