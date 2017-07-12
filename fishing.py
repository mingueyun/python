#   DRILL: 

# demonstrates the following concepts:

#1. Assign an integer to a variable
#6. Use of logical operators: and, or, not
bob = 1
jack = 2
if bob > 8:
    print('bob > 8')
if bob > 6 and jack >6:
    print('bob and jack >6')
if bob >=4 or jack >= 3:
    print ('bob is >=3,4')
elif  not bob>  2 and jack > 2:
    print('bob or jack is greater then 2')
else:
    print('nobody is greater then 2')



Lure_List = ['Blue Fox','Mepps','Flying C','Rooster Tail','Vibrax','Mepps']
# [:] removed  all the elements
New_lure_List = Lure_List[:]
New_lure_List.sort()
# prev is what used to be the old 
prev = New_lure_List[0]
del New_lure_List[0]
count = 0
while count < len(New_lure_List) and New_lure_List[count] != prev:
    prev = New_lure_List[count]
    count = count +1
if count < len(New_lure_List):
    print (' Match:', prev)





#5. Use each of these operators +, - , * , / , +=, ­= , %
def addBy1 (x):
    return 1 + x
print (addBy1(3))

def subBy9 (x):
    return 9 - x
print (subBy9(6))

def mulBy5(x):
    return 5 * x
print (mulBy5(9))

def divBy15(x):
    return 15 / x
print (divBy15(5))

def modBy12(x):
    return 12 % x
print (modBy12(7))



a = 12
b = 7
a += b
print ("Line 2 ", a)
a -= b
print ("Line 3 ", a )


#9. Use of a for loop
#10. Create a list and iterate through that list using a for loop to print each item out on a new line
Lure_List = ['Blue Fox',
             'Mepps',
             'Flying C',
             'Rooster Tail',
             'Vibrax',]
for j in Lure_List:
    print (j)



#11. Create a tuple and iterate through it using a for loop to print each item out on a new line
C1 = ('Mike', 'Push', 'Own', 30);
C2 = ('Jake', 'Rob', 'Rent', 40);
C3 = ('Sue', 'Feeler', 'Lease', 50);


for i in (C1,C2,C3): 
    print (i[0])

    
#3. Assign a float to a variable
#4. Use the print function and .format() notation to print out the variable you assigned  
#2. assign a string to a variable    
#7. Use of conditional statements: if, elif, else
#8. Use of a while loop
#12. Define a function that returns a string variable
#13. Call the function you defined above and print the result to the shell
def fishing(lure=0,jig=0,worth=0,name=''):
    name = enter_store(name)
    lure,jig,worth,name = lure_jig(lure,jig,worth,name)

def enter_store(name):
    if name != "":
        print("\nWelcome back!, {}!".format(name))
    else:
        stop = True
        while stop:
            if name =="":
                name = input("\Tell customer Rep your name? ").capitalize()
                if name != "":
                    print("\nWelcome to our store, {}!".format(name))
                    print("\nToday we have a blowout sale on lures and jigs.")
                    print("\nFolow me and I will show where they are.")              
                    stop =  False
    return name

def lure_jig(lure,jig,worth,name):
    stop = True
    while stop:
        show_total(lure,jig,worth,name)
        pick = input("\nThe customer shows you the lures and jigs. will you choose lures or jig l/j:").lower()
        if pick == "l":
            lure = (lure + 1)
            worth = float(worth + 4.67)
            stop = False
        if pick == "j":
            jig = (jig + 1)
            worth = float(worth + 4.55)
            stop = False
        
        total(lure,jig,worth,name)
       
        
def show_total(lure,jig,worth,name):
    print("\n{}, you currently have ({}, lure) and  ({}, jig) and (${}, worth) of items." .format(name,lure,jig,worth))
    
def total(lure,jig,worth,name): 
    if lure >= 5:
        pay(lure,jig,worth,name)
    if jig >= 5:
        pay(lure,jig,worth,name)
    if worth >= 45:
        pay(lure,jig,worth,name)
    else:
        lure_jig(lure,jig,worth,name)

def worth_total(lure,jig,worth,name):
    print("\nSir! you currently have ({}, lure) and  ({}, jig) and ({}, total worth) of items." .format(lure,jig,worth))

def pay(lure,jig,worth,name):
        stop = True
        while stop:
            worth_total(lure,jig,worth,name)
            choice = input("\nDo you want to pay wit creditcard or cash? cc/c: ").lower()
            if choice == "cc":
                stop = False
                print("\nHere is your card and your items and have a good day!") 
            if choice == "c":
                print("\nHere is your change and your items and have a good day!")
                stop = False
                exit()
           

fishing()


