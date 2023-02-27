#Write a program which read 3 grades from a student and the average of grades by the tests this student had taken. 
#After that, use this formula to calculate the average perfomance: 
#averagePerformance = (Grade1 + Grade2*2 + Grade3*3 + averageGrade)/7
#So with the average, inform the concepts according to the items below:
#bigger than or equal to 9
#less than 4.

#Obs: Mrs. Anderson did not put the complete exercise.

Grade1= float(input("Enter with the grade you get in the first test: \n "))
Grade2= float(input("Enter with the grade you get in the seconde test: \n"))
Grade3= float(input("Enter with the grade you get in the last test: \n"))
averageGrade= Grade1 + Grade2 + Grade3 /3
averagePerformance = (Grade1 + Grade2*2 + Grade3*3 + averageGrade)/7

if averagePerformance >= 9:
    print("Congratulations! I'ts an A!")

elif averagePerformance < 4:
    print("Nhe! C")

else:
    print("You get a B!")

#---------------------------------------------------------------------------------------------------------------------------------------

#Create a program that asks for: name, address, zip code, and phone number.
#Print on the screen the values ​​as below:
# name on the first line,
#address on the second line,
#zipcode and telephone number on the third line.

name=(input('Full name \n'))
address=(input('Your Address \n'))
zipcode=int(input('Zip Code \n'))
phoneNumber=int(input("Your phone number \n"))

print(name)
print(address)
print(zipcode, phoneNumber)

#---------------------------------------------------------------------------------------------------------------------------------------


#Write a program that on the screen the image down below:

#XXXXX
#X   X
#X   X
#X   X
#XXXXX

print("XXXXX")
print("X   X")
print("X   X")
print("X   X")
print("XXXXX")

#---------------------------------------------------------------------------------------------------------------------------------------

#Write a program that user must enter the name of the student and his grade.
#And the program display the value as below:

#STUDENT   GRADE
#=======   =====
#ALINE      9.0

studentName=input('Student name \n')
studentGrade=float(input('Grade \n'))

print(' Student   Grade \n', '=======   ===== \n', studentName,'   ',studentGrade)

#---------------------------------------------------------------------------------------------------------------------------------------

#Write a program that show the following menu on the screen:
#Customer rsgistration
#0 - End
#1 - Join In
#2 - Update
#3 - Delete
#4 - Check

# When the user enters a option to display the item, if you enter with a different value from the menu display "item not found".

end= ('0- end')
add= ('1- Join in')
update= ('2- Update')
delete= ('3- Delete')
check= ('4- Check')

print('Welcome to the Customer Registration')
print(end)
print(add)
print(update)
print(delete)
print(check)

customerChoice= int(input('Please, choose an option (Just the number): \n'))

if customerChoice == 0:
    print('BYE BYE!')

elif customerChoice == 1:
    print('Hello, welcome! Let\'t\'s start?')

elif customerChoice == 2:
    print('We are on the uptade menu. Be free to change your data.') 

elif customerChoice == 3:
    print('Are you sure you want to delete every data you had  archive here?') 

elif customerChoice == 4:
    print('Le\'t\'s check your information.') 

else:
    print('Error! Try to select a valid option.')

#---------------------------------------------------------------------------------------------------------------------------------------

#Implement a program that
#draw a "pine tree" on the canvas,
#similar to below. The value of X
#must be provided by the user.

character = input("Enter a character: ")

spaces = " " * 6
tree = character * 1
print(spaces + tree)

spaces = " " * 5
tree = character * 3
print(spaces + tree)

spaces = " " * 4
tree = character * 5
print(spaces + tree)

spaces = " " * 3
tree = character * 7
print(spaces + tree)

spaces = " " * 2
tree = character * 9
print(spaces + tree)

spaces = " " * 1
tree = character * 11
print(spaces + tree)

tree = character * 13
print(tree)

spaces = " " * 5
tree = character * 2
print(spaces + tree)

spaces = " " * 5
tree = character * 2
print(spaces + tree)

spaces = " " * 4
tree = character * 4
print(spaces + tree)

#---------------------------------------------------------------------------------------------------------------------------------------

#If x is a variable of type
#int with value 17 and y a variable
#float with value 3.2, calculate the
#value of the following expressions in
#python:

#a) x / 4 + y
#b) x * y ** 6
#c) (x % 4) , (((int) y * 10) //4)
#d) (x / 6 // x / 3) + 4


x = 17
y= 3.2

a= x / 4 + y 
b= x * y ** 6
c= (x % 4) , ((int(y) * 10) //4)
d= (x / 6 // x / 3) + 4

print(a)
print(b)
print(c)
print(d)

#---------------------------------------------------------------------------------------------------------------------------------------

#Consider the formula:
#S = n*(a1+an)/2.
#it is the sum of terms of an arithmetic progression.
#Make a program where the user must enter the number of terms (n), initial value (a1) and final value (an).
#The sum result should be shown on the screen.

numOfTerms= float(input('Enter with the number of the terms: \n'))
initialValue= float(input('Enter with the initial value: \n'))
finalValue= float(input('Enter with the final value: \n'))

S = numOfTerms*(initialValue + finalValue)/2

print('The result is: ', S)

#---------------------------------------------------------------------------------------------------------------------------------------

#Consider the formula:
#Sn = initialValue*(ratio**numberOfTerms -1) / (ratio-1)

#Write a program where the user must enter the initial value (initialValue), the number of terms (numberOfTerms) and the ratio.
#  For our exercise the ratio should be bigger or equal to 2.

initialValue=float(input('Enter with the initial value: \n'))
numberOfTerms= float(input('Enter with the number of the terms: \n'))
ratio= float(input('Enter with the ratio: \n'))
    

if ratio < 2:
    print('ERROR! Try to enter a ratio bigger than or equal to 2.')

else:
   print(initialValue*(ratio**numberOfTerms -1) / (ratio-1))

#---------------------------------------------------------------------------------------------------------------------------------------

#Write a program to read a person's year of birth and write a message that says whether or not they can vote this year (no need to consider the month they were born).

birthYear=int(input('Enter with the year you were born: \n'))

if birthYear <= 2007:
    print('You can vote!')

else:
    print("You can't vote this year! ")

#---------------------------------------------------------------------------------------------------------------------------------------

#A program based on my Mrs. Anderson solution, where we include a Library to solve. This code is way better than mine (above) because we automatize the year cause the library so its any year.:

from datetime import date

currentYear = date.today().year
birthYear = int(input("Enter with your birth date: "))
age = currentYear - birthYear

if age >= 16:
    print("You can vote this year. Your age is: ", age)
else:
    print("You can't vote this year. Your age is: ", age)

#---------------------------------------------------------------------------------------------------------------------------------------


#Write a program that checks the validity of a user-supplied password. Valid password is number 8765.
# The following messages must be printed:
#ACCESS ALLOWED if the password is valid.
#ACCESS DENIED if the password is invalid.

passcode=int(input('Hi! Please type the passcode!\n' ))

if passcode == 8765:
    print('Access Allowed.')

else:
    print('Access Denied.')

#---------------------------------------------------------------------------------------------------------------------------------------


#Taking as input the height and gender: (coded as follows: 1:female 2:male) of a person, build a program that calculates and prints your ideal weight, using the following Formulas:
#- for men: (72.7 * Height) – 58
#- for women: (62.1 * Height) – 44.7

height= float(input('Hello! Please, type your height: \n'))
sex= int(input('Now, your sex (Type the number): \n 1-Female \n  2- Male \n' ))
 
male = (72.7 * height) - 58
female= (62.1 * height) - 44.7

if sex == 1:
    print('Your ideal weight is:', female)

elif sex == 2:
    print('Your ideal weight is:', male)

else:
    print('ERROR! Try to type a valid option (1-2) in sex.')

#---------------------------------------------------------------------------------------------------------------------------------------

#Write a program to read the number of sides of a polygon regular. 
#Calculate and print the following:

#− If the number of sides is equal to 3 write TRIANGLE and the value from the area
#− If the number of sides is equal to 4 write SQUARE and the value of your area.
#− If the number of sides is equal to 5 write PENTAGON.
#After that, add the following messages for the solution:
#− If the number of sides is less than 3 write "NOT A POLYGON.
#− If the number of sides is bigger than 5 write "POLYGON NO IDENTIFIED"


polygon= int(input('Type how many side numbers did your polygon have? \n'))

if polygon < 3: 
    print("Not a polygon.")

elif polygon == 3:
   print("I'ts a triangle! And your area is: A = b*h/2")

elif polygon == 4:
    print("It's a square! And your area is: A= a **2")

elif polygon == 5:
    print("It's a pentagon! And your area is: A= p * a/2")

else:
    print("Polygon not identified.")

#---------------------------------------------------------------------------------------------------------------------------------------
#Or we have the solution down below: - 
# This solution is more complete. We have input to insert data about the area after choose wich polygon did you 'have'.

polygon= int(input('Type how many side numbers did your polygon have? \n'))

if polygon < 3:
    print("It's not a polygon.")

elif polygon == 3:
    print("I'ts a triangle! And the formula of area is: A = b*h/2. Should we calculate?")
    print('')
    base= float(input('Enter with the value of the base: \n'))
    height= float(input('Enter with the value of the height: \n'))
    area= base * height / 2
    print('The triangle area is:', area )
    

elif polygon == 4:
    print("It's a square! And your area is: A= a **2. Should we calculate?")
    print('')
    side= float(input("Enter with the value of the side: \n" ))
    area = side ** 2
    print("The square area is:", area)


elif polygon == 5:
    print("It's a pentagon! And your area is: A= p * a/2. Should we calculate?")
    print("")
    perimeter = float(input("Enter with the value of the perimeter: \n"))
    apothem= float(input("Enter with the value of the apothem: \n"))
    area = perimeter * apothem / 2 
    print("The pentagon area is:", area)


else:
    print("Polygon not identified.")

