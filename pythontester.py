print("a")
a = 100+100 
print("a =", a, sep ="  ") 
#on line three there is an autospace between = and a value;200

a =a/2 # one slash leaves in decimal form/ double form

print("a =", a, sep ="  ") 

a =a/2 # int form????
a = int(a)
print("a =", a, sep ="  ") 

#min and max 
x=min(3,4)
b = max(3,4)
print("x =", x, sep ="  ") 
print("b =", b, sep ="  ") 
#Python seems to prioritze int over double


#no need for a scanner 
#Uncomment these for scanner help
#print("Enter a number: ")
#x = input()

#print("you entered:", x)

#String is different in pythin for exampke .length in java is not len(string)
s = "here"
print("Lenght =", len(s))


#Substring method  
z ="input"
print("Lenght of input word=", len(z))
print("Substring =", z[2:]) #first tho letters
print("Substring =", z[1:3]) #2nd and 3rd letter
print("Substring =", z[-2:]) #last (hence the negatiuve) tho letters

#contains 
print("Contains = ", ("p" in z)) #boolean



#List class
list = [] #the [] shows its a list while "list" means nothing

list.append("a")
list.append("b")
list.append("c")

print(list)
print("length", len(list)) #length
print("index", list[1])
list.insert(1,"grouse") #focusses on index of being places
print(list)

#remove
del(list[1])#delete at index 1
print(list)
del(list[1:3]) #important 3 is not apart of the index choice siilair to java
print(list)
list.append("b")
list.append("c")

#resetting the list

#entend methid adds lists together
list2 = []
list2.append("d")
list2.append("e")
list2.append("f")

ist3 = []
list3 =list+list2

list.extend(list2) #lkst one gets the additon of list 2
print(list) #changed
print("should be as line aboove ",list3)
print(list2) #list 2 does not change

list4 =[]
list4.append("a")
list4.append("s")

list5 =[]
list5.append("d")
list5.append("f")

list4.append(list5)
list4.append(list3) #adding lists to the list meaning itll be (list5, list 3)
print(list4)
print(list4[1])
print(list4[1][0])#index of 1 place of list and the sero value in theire

#lists are mutabel/changable while tuple and strings are immutable
print("tuple") #type of data 
e =2,3,4,5
print(e)

y=e,6,7 #adding tuples together
print(y)

alk= 5, #this is a tuple bc of the comma

#String .equals eqivilent, == , "is"

x="4"
y="5"

print(x==y) #functions like java

#sdf = input() #checks input
yi = "house"

print(x is y)
#print(sdf is yi)  #Equvidlent to the .equlas method



#negation
print("negation test ",not (4>5))
# not is like a !
#also can right out or and and

print("AND AND OR test",4<5 and 6<7)

#if statemntd
if 4 > 5: # the : acts like a {}
    print("accepted")

#Important
elif 5==5:
    print("partial accepted")
#else statemtn
else:
    print("not accepted")



#while loop
aws = 0
while aws<5:
    print(aws, end = " ")
    aws = aws+1


#for loop
aps =0
for aps in range(5,20,5): #starts at zero and goes to 5 like index
    print (aps, end =" ")



#for nested loop
lister = [1,2,3,4]

for xix in list:
    print(xix,end = " ")

