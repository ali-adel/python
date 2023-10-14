# list 

""" mylist  = list(range(1,100))
a = [100,200,300,400,500] """

#print(mylist[0:100 : 1])  #  => mylist[st : end : steps]
#print(mylist[100:0:-1])   #  => -1 mean revers order 
#print(mylist[49:-4])      #  => -4 mean the last fourth element
#print(mylist.append(600)) #  => append 600 in the last of mylist
#print(mylist.extend(a))    #  => add a list to mylist  

# dictionary 

""" mydict = {"ali" : 12 , "alaa" : 20 , "ahmed" : 30}

print(mydict['ali']) # 12 

mydict['alaa'] = 55  # => exist so it will set it's value
mydict['lol'] = 66 # doesn't exist so it will be added


print(mydict.keys()) # get tge mydict "keys"
print(mydict.values())# get tge mydict "values"
print(mydict.items())# get tge mydict "keys & values"
 """


############################################# type convestion ##################################

 # str() -> convevrt to string 
 
""" x = 100

print(type(x))

print(type(str(x)))


print("#" * 50) """

 # tuple() -> convevrt to tuple


""" x = "alawy"
w = {"a" , "b" , "c"}
y = ["A" , "B" , "c"]
z = {"one" : 1 , "two" : 2 , "three" : 3}

print(tuple(x))
print(tuple(w))
print(tuple(y))
print(tuple(z))

print("#" * 50) """

 # list() -> convevrt to list

""" x = "alawy"
w = {"a" , "b" , "c"}
y = ("A" , "B" , "c")
z = {"one" : 1 , "two" : 2 , "three" : 3}

print(list(x))
print(list(w))
print(list(y))
print(list(z))

print("#" * 50) """

 # set() -> convevrt to set
""" x = "alawy"
w = ["a" , "b" , "c"]
y = ("A" , "B" , "c")
z = {"one" : 1 , "two" : 2 , "three" : 3}

print(set(x))
print(set(w))
print(set(y))
print(set(z))

print("#" * 50) """

# dict() -> convevrt to dict

""" x = "alawy" #can't convert need ket & value
w = {"a" , "b" , "c"} #can't convert need key & value v also if  {{"A" , "a" } , {"B" , "b"} ,{"C" , "c"} } can't convert
y = (("A" , "a") , ("B" , "b") , ("C" , "c"))  # know it have key and value 
z = [ ["one" , 1 ] ,  ["two" , 2 ] , ["three" , 3 ] ] # know it have key and value 

#print(dict(x))
#print(dict(w))
print(dict(y))
print(dict(z))

print("#" * 50) """


############################################# user input ##################################

# input() -> to take input from the user 

""" fname = input("your first name  is : ")
mname = input("your middle name  is : ")
lname = input("your last name  is : ")

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()

print(f" hello {fname} {mname:.1s} {lname} nice to meet you ") """

#############################################  control flow  ####################################################

""" uname = "Ali"
ucountry = "lol"
cprice = 300
disc = 100

if ucountry == "Egy": 
    disc = 10
    print(f" as you from {ucountry} you have disc {disc}$")
    print(f"the course price is {cprice}$ after discount is {cprice - disc}$")

elif ucountry == "Ksa":
    disc = 100
    print(f" as you from {ucountry} you have {disc} $")
    print(f"the course price is {cprice}$ and your discount is {cprice - disc}$")  

else :
  print("usupprted country")     """


##nested if  

""" uname = "Ali"
isstudent = "ى"
ucountry = "Egy"
cprice = 300
disc = 100

if ucountry == "Egy" or ucountry == "Ksa" : 
   if isstudent == "yes":
      print(f" as you from {ucountry} you have disc {80}$ and you are student")
      print(f"the course price is {cprice}$ after discount is {cprice - 80}$")
   else:
     print(f" as you from {ucountry} you have disc {20}$ ")
     print(f"the course price is {cprice}$ after discount is {cprice - 20}$")

   print("you got your discount")    

elif ucountry == "qatr" :
  print(f" as you from {ucountry} you have disc {20}$")
  print(f"the course price is {cprice}$ after discount is {cprice - 20}$")

else :
  print("usupprted country")  """

#ternary operator

""" age = 15
cnt = 0
#true | if cond |else false
cnt+=1 if age >= 18 else  5 

print(cnt) """



#############################################  practice using control flow  ####################################################
""" print("#" * 50)
print(" you can enter the first letter or the word ".center(80,'#'))
print("#" * 50)

age = input(" Inter your age  ")
unit = input(" what is the format you want : Months , Weeks , Days  ").strip().lower()

age = int(age)
months = age * 12 
weeks  = months * 4
days = age * 365 
if unit == "months" or unit == "m" :

    print(f"your age in months is : {months:,}")
 
elif unit == "weeks" or unit == "w" :

    print(f"your age in Weeks is : {weeks:,}")
else:
        print(f"your age in Days is : {days:,}")
 """

#############################################  membership operator  ####################################################

# in && not in -> it is mean that any thing i want [check if it is a member in any groub of elements]

""" countryone = ["egy" , "suadi" , "qatr" , "syria"]
countrytwo = ["england" , "ksa"]
mycountry = "england"

if mycountry  in countryone: # the (not in) is the inverse
    print("you have disc of 80 $")
 """

 #############################################  practice admin control  ####################################################

""" admins = ["Ali" , "Ahmed" , "Osama" , "Alaa"]

name = input(" inter your name : ").strip().capitalize()

if name in admins:
      option =   input(" you are admin ,Update or Delete ").strip().capitalize()
      if option == "Update" or option == "U" :
       newname = input("inter your new name : ").strip().capitalize()
       admins[admins.index(name)] = newname 
       print("name Updated successfully")
      else:
          admins.remove(name) 
          print("name Deleted successfully")
          
else:
      ch = input(" you are not admin , Add y/n : ").strip().capitalize()
      if ch == "Y" : 
         name = input(" inter your name : ")
         admins.append(name)
         print(" you are Added successfully ")
      else :     
       print(" you are not Added ") """

 ############################################# loops   ####################################################

#while loop
""" a = 0 
while a < 10 : #print from 0 to 9
    print(a)
    a+=1

print("loop is done")    
print("the remaining code") """

#for loop
""""items = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]

for item in items :
    print(item)

#for loop to use index
items = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]

for  i,item in enumerate(items) :
    print( f"#{item}") """

#nested for loop


""" info = {
    "osama" : 
    {
        "html" : "90%",
        "css" : "80%"
    },
    "ali" :
    {
        "c++" : "90%",
        "python" : "60%",
        "c" : "90%",
        "java" : "50%"
    }

}
for key in info :
    print(f"{key}")
    for skill in info[key]:
        print(f" has skills {skill} : {info[key][skill]} ")
    print("\n")     """

 ############################################# continue & break & pass   ####################################################

"""arr = [ 1 , 2 , 3 , 4, 5 , 6 , 7 , 8 , 9 , 10 , 11 ]

 for i in arr :
    
    if i == 4 :
        continue #print all the array except 4
    print(i) """

""" for i in arr :
    
    if i == 4 :
        break #print the array to 3 only
    print(i) """

""" for i in arr :
    pass # to pass a block (skip) (as in this case it will generate error without the "pass")
 """
 ############################################# advanced looping on dictionary ####################################################

""" dict1 = {
    "html" : "90%", 
    "css" : "80%",
    "js" : "70%"
}

for k , v in dict1.items(): # in one dimention
    print(f"{k} => {v}")   """


""" dict2 = {
    "osama" :
    {
    "html" : "90%", 
    "css" : "80%",
    "js" : "70%"
    },
    "ali" : 
    {
        "c" : "80%",
        "c++" : "90%",
        "python" : "99%"

    }

}

for mk , mv in dict2.items() : # in two dimention
    print(f"{mk}")
    for k , v in mv.items(): 
         print(f"{k} => {v}") """


 ############################################# Functions ####################################################

""" def function_name1(): #function structure 
    print("my fun1") # just print doesn't return 

def function_name2(): #function structure 
  return  "my fun2" #  return 

#unction_name1()   #function call
print(function_name2())  #function call and print the returned value """

#parametars and arguments

""" 
def full_name(first , second) :  #first , second => parametars
    print(f" hello {first.strip().capitalize()} {second.strip().capitalize():.1s} ")
    

full_name("ali", "sayed")       #"ali", "sayed"=>arguments
 """

#packing and unpacking  
# => use it if didn't know the number of arguments that i will send it to the function 


""" def myfun(n , *sk): # use ( * ) to make the unpack (it makes me treat the elements separately)
    print(f"hello {n} your skills is : ")
    for i in sk :
        print(i)
    

myfun("ali" ,"html" ,"css" ,"js" ) """

 ############################################# global and local variable ####################################################

""" x = 1

def fun1():
    x = 3 
    print(f"it will print the x which in it's scope {x}") # x = 3

def fun2():
   
    print(f"here no local var called x so i will print the global one {x}") # x = 1

def fun3():
    global x  # it tell that i will treat with he global x
    x = 5 # set the global var x to 5
    print(f"will print the global x  {x}") # x = 5


print(f"x here is a global var as the print see the global var {x}") #x = 1
fun1()
fun2()
fun3() """

 ############################################# Recursion ( don't scare :) ) ####################################################

# ex to undersand recursion


""" def clear_word(word) : # it is a fun to clear the repetted letters in a worrd like "wwwwoorlllddd"
     
     if len(word) == 1 : # if it one letter just return it (this is the base case )
      return word     
     
     if word[0] == word[1]:   # if the first to letters the same the fun call itself but without the first letter "wwwwoorlllddd" => ".wwwoorlllddd" 
        return clear_word(word[1:])
     
     return word[0] + clear_word(word[1:]) # here the first letter is reterned and call the function again from the second leter 
     
  
print(clear_word("wwwwoorlllddd")) """

 #############################################  Lambda Function  ####################################################


""" def say_h(name):              ## normal function used for a block of code 
   return print(f"hello {name}")


hello = lambda name :  print(f"hello {name}") ## lambda function used for single line (Simple) expression  not for a block of code 

me = lambda x :  print(f"{x}")

hello("lol")
me(200) """

 #############################################  file handling  ####################################################

# "r" -> read from a file (default) 
# "w" -> write from a file 
# "x" -> create a file 
# "a" -> append on file 

"""
import os
print(os.getcwd()) # get current working path
 

print(os.path.abspath(__file__)) # get current file path


print(os.path.dirname(os.path.abspath(__file__)))# get current file path(folders)

os.chdir(os.path.dirname(os.path.abspath(__file__)))#change the current working path

file1 = open("C:\\Users\\Legion\\Desktop\\python\\lol.txt")#(absolute path => you give the full path )  open a file to read (default operation)
file2 = open("lol.txt") #(relative path => depend on the  current woring path)# open a file to read (default operation) 
"""


# read option


""" myf = open("C:\\Users\\Legion\\Desktop\\python\\lol.txt","r") 

print(myf) # file data object 

print(myf.read()) # read the content of the file default (-1 -> all file )
print(myf.read(20)) # read 20 character from the file 

print(myf.readline()) # read one line
print(myf.readline(20)) # read 20 char from the second line

print(myf.readlines()) # return list of all lines in the file (ake the pointer of reading at the end of the file)
print(myf.readlines(20)) # so this it will be empty as it read 20 char from the end of the file  


for line in myf :# looping on all the lines in the file and if startwith("i") => break
    
    if line.startswith("i"):
        break 
    print(line)x

myf.close() ## should close the file after any edit"""

# write and append option
  
""" ff = open("C:\\Users\\Legion\\Desktop\\python\\lol.txt","w") # write option (delet the content of the file if exists )

 ff.write("hello my bro\n") # to write in the file and make the cursor in the beginning of the new line
ff.write("hello my bro2") # write this statement in the beginning of the new line


lis = ["ali\n" , "adel\n" ,"sayed\n"]
ff.writelines(lis) # write a list in the file  """


""" ff = open("C:\\Users\\Legion\\Desktop\\python\\lol.txt","w") # append option (add what you want to the content which exist in the file (don't delete it))

ff.write("alawy habeb glby\n") 
ff.write("alawy habeb glby abo 7sen \n") # the two lines added to the file (both) """

#  additional functions in files 

"""f2 = open("C:\\Users\\Legion\\Desktop\\python\\lol.txt","a")
 f2.truncate(18) # leave a 18 char and delete the remaining  
print(f2.tell()) # tell you the position of the cursor """

""" f3 = open("C:\\Users\\Legion\\Desktop\\python\\lol.txt","r")
f3.seek(13) # chang the position of the cursor
print(f3.read()) """

""" import os
os.remove("C:\\Users\\Legion\\Desktop\\python\\lol.txt") # to delete the file  """

 #############################################  built in functions  ####################################################
 #all this fun should use it with iterable var like (list ,tuble , dict)
# all() # check if all elements true
# any()# check if at least one element true
#bin()#return the binary number
#id()# return the id of the memory address
###########################################################

#sum()
#round()
#print()
#range()

#########################################


#abs() -> give you the positive value 
#pow() ->ofcourse you know it
#min() -> this too
#max() -> this too
#slice() ->this give you a slice of (list ,tuble,..) =>but should write the end

""" lis = [1,2,3,4,[]]

if any(lis):
    print(" all elements are true ")
else:
    print("at least one element is false")     """

#sum(iterable,st)
""" arr = [1,2,3,4,5]
print(sum(arr)) # 15
print(sum(arr,5)) # 20 """
#round(num , num of digits)
""" print(round(100.455,1)) """

#range(st , end, steps)
""" print(list(range(0,11,2))) #[0, 2, 4, 6, 8, 10] """

#print() => sep 
""" print(" hello my bro ")
print("hello" , "my" , "bro" ,sep=" | ")
 """
#print() => end 
""" print(" hello my bro ",end="\n") # default end="\n"
print(" econd line ") """

#abs()
""" print(abs(-100)) # 100
print(abs(100)) # 100
 """

#pow(base,exp,mod)

""" print(pow(2,3)) # 2 * 2 *2
print(pow(2,3,2)) # (2 * 2 *2) % 2 => 0
 """
#min(item,item,..,or iterator)
""" print(min(1,2,-20,10))
tup = ("a","b","c")
print(min(tup)) """
#max(item,item,..,or iterator)

""" print(max(1,2,-20,10))
tup = ("a","b","c")
print(max(tup)) """

#slice(st,end,steps)

""" arr = [1,2,3,4,65,100]

print(arr[slice(4)]) # [1, 2, 3, 4]
print(arr[slice(2,5)]) # [3, 4, 65] """


 #############################################  map  ####################################################
 # map(function , iterable) -> it apply the function to all elements

""" def formater(name) :
    return f" {name} ".strip().capitalize()

mya = ["ali", "adel" ,"sayed"]
hold =  map(formater,mya)

for i in hold :  # apply this function on all mya elements
    print(i)  """

 #############################################  filter  ####################################################
 ## it is the same like map but it return the item if the function returned true only
#filter(function, iterable)

""" def chnum(num):
    return num > 3

numbers = [1,2,3,4,5,6]

myf = filter (chnum , numbers)

for num in myf :
    print(num)

    def chnum(num):
    return num > 3
 """

""" def chname(name):
    return name.startswith("a")

names = [ "ali" , "alaa" , "osama" , "abdala" ]

myf = filter (chname,names)

for name in myf :   # ali alaa  abdala
    print(name)

 """
 #############################################  reduce  ####################################################
# like map and filter but it take two items and make fun on them and the result with the next item and so on

""" from functools import reduce

def sum(num1,num2):
    return num1 + num2 

arr = [1,2,3,4,5]

res = reduce(sum,arr)
print(res) # ((((1+2)+3)+4)+5) => 15 """

 ############################################# some important function  ####################################################

 # enumrate() => add a counter for the loop
 #help() => give you info about functions
 #reversed() => reverse an iterable var(string , list , tube , dict )

# enumrate()
""" myl = [ "ali" , "adel" , "sayed" , "ahmed" ]

mylistwithcnt = enumerate(myl) # add a cnt with the list

for  item in myl :   # ali adel sayed ahmed 
    print(f"{item}")


for cnt , item in mylistwithcnt :    # 0 , ali   1 , adel    2 , sayed  3 , ahmed
    print(f"{cnt} , {item}") """

 #help() 

""" help(print) """ # all info about the print function

 #reversed()

""" st = reversed("alawy")

for i in st : # print alawy reversed 
    print(i) """


 ############################################# modules  ####################################################
# a file has a set of functions ready too use 

""" import random # import all module 

print(f"the random float value is {random.random()}") # return a random float value  """


""" from random import randint , random # import one or more function from the module 

print(f"the random int is : {randint(1,100)}" ) # return random int num from 1 to 100 (use it directly without(random.randint()))
print(f"the random float is : { random() } " ) # return random flaot num from 1 to 100 (use it directly without(random.randint()))

 """


# make your own module 

""" import sys
print(sys.path)# all dirrectories which can import modules from it 
sys.path.append("C:\\Users\\Legion\\Desktop\\lol") # add this path to read any dir from it  """

"""
import alawy 

print(dir(alawy)) # print all function in this module 

 print(alawy.good("ali"))
print(alawy.hello("lol")) """

# alias for module 
""" import alawy as ay

print(ay.good("ahmed"))
 """
# alias for fun in a module  

""" from alawy import good as gg

print(gg("osama")) 
 """

 ############################################# package ####################################################
# package => have some modules (pip -> package manager for python (website for packages pypi.com ))

#pip install termcolor => install  termcolor package (execute in terminal)
#pip install pyfiglet => install  pyfiglet package (execute in terminal)


""" import pyfiglet
import termcolor
print(dir(pyfiglet))
print(termcolor.colored(pyfiglet.figlet_format("ALAWY"),color="yellow"))  """

 ############################################# date and time ####################################################

#import datetime


""" print(datetime.datetime.now()) # the current datetime   """ 
""" print(datetime.datetime.now().year) # the current year and the  month / day the same """
""" print(datetime.datetime.now().time()) # the current time """
""" print(datetime.datetime.now().time().hour) # the current hour / minute and second the same  """

""" # the start and ed of time
print(datetime.datetime.min)
print(datetime.datetime.max) """

""" #print a spesific time and date 
print(datetime.datetime(2003,2,7)) """

# format datetime

""" myb = datetime.datetime.now().time()

print(myb.strftime("%H : %M ")) # 03 : 18 => time with 24 h system
#print(myb.strftime("%d %b %Y ")) #07 Feb 2003 (from strftime directive website)
 """

 ############################################# iterable an iterator  ####################################################
 # iterable => object contain data can be iterated upon
 # iterator =>object use it to iterate on iterable object using next() fun(can turn iterable object to iterator by using iter() fun )
  

name = "ALAWY"

""" for i in name :
 print(f" {i} ",end=" ")
"""

""" newname = iter(name)
 
print(next(newname)) # A
print(next(newname)) # L
print(next(newname)) # A
print(next(newname)) # W
print(next(newname)) # Y
print(next(newname)) # StopIteration """

 ############################################# generator  ####################################################
# it is fun but with "yield" keyword not "return" 
# it return iterator for each yield and we can use many yield 
# it resume from last yield called 

""" def gn():
    yield 1
    yield 2
    yield 3
    yield 4

mygn = gn()
 """
""" print(next(mygn))    #1
print(next(mygn))   #2
print("hello") #hello
print("hello") #hello
print(next(mygn)) #3
print("hello")    #hello
print(next(mygn))    #4 """

""" for i in mygn :
    print(f" {i} " ,end ="") #  1  2  3  4  as it return iterator  """

############################################# decorators  ####################################################

# func which take a parameter fun and make decoration then return  ( higher order function )

"""  # fun without parameters 
def decorator(func):  
    def nested():  
       print("make a decoration here *** ")

       func()#call our function 

       print(" *** make a decoration here")
    return nested
   

   
@decorator
def hello():
   print( " say hello func is here ")


hello()  
# make a decoration here *** 
# say hello func is here 
# *** make a decoration here  """

# fun with parameters 

""" def decorator(func):  
    def nested( l , m):  
       
       print(" first , from decorator one  ")

       func(l , m)#call our function 
    
       print(" second , from decorator one  ")
    return nested
   
def decoratortwo(func):  
    def nested( l , m):  
       
        print(" first , decorator two ")

        func(l , m)#call our functio

        print(" second , decorator two ")
    return nested
   

@decoratortwo  
@decorator
def plus(x , y):
   print( x + y)


plus(-100,200)     
# first , decorator two 
# first , from decorator one  
# 100
# second , from decorator one  
# second , decorator two  """



############################################# speed test using decorator  ####################################################


""" from time import time 

def speed(fun):
    def nested():
        st = time()
        fun()
        end = time()
        res = end - st 
        print(f"speed is = {res}")
    return nested    

@speed
def myloop():
    for i in range(1,20000):
        print(i)


myloop()  # speed is = 2.079014539718628   (fun myloop() takes this num  running )    """

#############################################   zip()       ####################################################
# use it to iterate on more than one object 
# and it take the lowest length

""" list_1 = [1,2,3,4]
tupl_1 = ("ali" , "adel")

hold = zip(list_1 , tupl_1) # llen is the lowest obj which is thhe tuple_1 => 2 so the zip len is 2

for item1 ,item2 in hold :   
    print("list_1 => " ,item1)
    print("tuple_1 => " ,item2)

# list_1 =>  1
# tuple_1 =>  ali
# list_1 =>  2
# tuple_1 =>  adel """


#############################################   documenting       ####################################################

# it is a document which explain (function , class , module ) using  '''  content   ''' 

""" def fun(name):
    ''' 
    it is a function to say hello to the user 
    params : name of the person 
    
    '''
    print(f" hello {name} from the func ")


print(fun.__doc__) #  it is a function to say hello to the user 
help(fun) """

#############################################   Exceptions       ####################################################
# it is a runtime error reporting 
# if exception happen don't resume the code stop here 

# raise => use it to make our exception 

""" x = -10 

if( x < 0) :
    raise Exception("negative value not allowed ")  # here i will print this message and stop until solve it
  

print("the remainning code  ") """


# exception handling 


""" try: # we write our code here 

    print( 10 / 0)
    print(int("osama"))

except ZeroDivisionError: # here we write what will we do if (ZeroDivisionError) any error
    print("can't divide by zero ")

except ValueError: # here we write what will we do if there (ValueError) error
   print(" can't convert string to int ") """

############################################# debugging ###########################################################

# make you folllow your code in effiecient way (google it )

""" lists = [ 1 , 2 ,  3 , 4 , 5]

for i in lists :
    print(i)
 """
#############################################   type hinting   ###########################################################

""" def congrats(name) -> str  :   # that means it takes str vlaue ( it is just a hint )
    print(f"congratulations {name}") """


#############################################   regular expression  ###########################################################
# I will provide some important functions in the re and y can watch the videos for more info (from elzero)


#split(pattern , string , max split) # seprates the string with the pattern you want
#import re

""" str = "hello my friend"
hold = re.split("\s" , str,1)

print(hold)

for i in hold :
    print(i)

#hello
#my friend """

#sub(pattern , replace , string  , rplacecnt) #replace the string pattern with what you want

""" mystr = "hello my friend i didn't find any thing to write" 
 """
""" hold  = re.sub("\s" , "-" , mystr )
print(hold)#hello-my-friend-i-didn't-find-any-thing-to-write
 
hold2  = re.sub("\s" , "-" , mystr , 1 )
print(hold2)#hello-my friend i didn't find any thing to write"""

#############################################   regular expression  ###########################################################

#*************************************************************************************************************

#####################################################################################################################
#############################################   OOP  ###########################################################
######################################################################################################################

#class => it is the (blue print) or the source of the objects any thing i intersted in in our system should be a class which have attributes and functions to do 
#attribute => the properities of our object
#functions => the is this object do 
#object => created from the class and ofcourse have attributes an functions like it

""" class first : 
    def  __init__ (self) : # give the intial value to the object  and the "self" refer to the current object
      self.name = "osama" #instant attributes

obj1 = first() # create obj from the "first" class

print(obj1.name) #access the attribute "name"
 """

#****************************************************************************
# instant attribute -> related to the object
""" class first : 
    def  __init__ (self , fname , mname , lname ) : # give the intial value to the object  and the "self" refer to the current object
      self.fname = fname
      self.mname = mname
      self.lname = lname 

    def full_name(self):
       print(f"{self.fname} {self.mname} {self.lname}")  

obj1 = first("ali" , "adel" ,"said") # create obj from the "first" class
obj2 = first("ahmed" , "adel" ,"said")# create obj from the "first" class
obj3 = first("osama" , "mo" ,"said")# create obj from the "first" class


obj1.full_name() #ali adel said
obj2.full_name() #ahmed adel said
obj3.full_name() #osama mo said
"""
#***************************************************************************************************
#class attribute -> related to the class
#classmethod ->  related to the class takea "cls" as param
#staticmethod -> related to the class doesn' take any thing
#instancemethod -> related to the instant take "self" as params

""" class first : 
    users = 0 #class attribute

   

    def  __init__ (self , fname , mname , lname ) : # give the intial value to the object  and the "self" refer to the current object
      
      if first.users == 5:
         raise ("exeed number of users ")
      else :
        self.fname = fname
        self.mname = mname
        self.lname = lname
        first.users += 1 

    @classmethod
    def sayusersnum(cls):
       print(f"we have {cls.users} users")

    @staticmethod
    def sayhello():
       print("say hello from static method")   

    
    def full_name(self):   
       print(f"{self.fname} {self.mname} {self.lname}")  


obj1 = first("ali" , "adel" ,"said") # create obj from the "first" class
obj2 = first("ahmed" , "adel" ,"said")# create obj from the "first" class
obj3 = first("osama" , "mo" ,"said")# create obj from the "first" class

first.sayusersnum() # we have 3 users

first.sayhello() # say hello from static method """



#magic methods 

#__init__() => called outomatically when instansiate an object (called auto)
#__str()__ => give readable message (called auto)
#__len()__ => use it to can use the normal "len()" fun (called when use the normal one on our obj)

""" class first : 

    def  __init__ (self,name ) : # 
            self.name = name
            self.myl = [1,2,3,4,5]

    def __str__(self) :  
          return f"we have name {self.name}"
    
    def __len__(self):
          return len(self.myl) 
          


obj = first("lol") 
print(obj)# we have name lol

print(len(obj)) # 5
 """


# inheritance 


""" class Food :

    def __init__ (self , name , price) :
        self.name = name
        self.price = price
     
        print(f" {self.name} from food base class and the price is {self.price}")




class Apple(Food) : # inherit from food calss

    def __init__(self , name , price , amount):

        super().__init__(name,price) # use the constructor of the base calss so (will call the constructor of the base class then resume it's work)
        self.amount = amount
        print(f" {self.name} from Applle derived class and the price is {self.price} and the amount is {amount}")
        




#myfroot = Food("apple" , 100) #  apple from food base class and the price is 100

#myapp = Apple("apple" , 100 , 1000)
# apple from food base class and the price is 100
# apple from Applle derived class and the price is 100 and the amount is 1000 """


# multiple inheritance => which the class inherit from multiple classes
# mro() => method resolution order (give you the order of the inheritance)

""" class b1 :

   def __init__(self) :
      print(" from init b1 ")


class b2 :

   def __init__(self) :
      print(" from init b2 ")


class ch (b1  , b2) : #multiple inheritance

   pass 
         
myo = ch()

print(myo) #  from init b1 
print(ch.mro())    #[<class '__main__.ch'>, <class '__main__.b1'>, <class '__main__.b2'>, <class 'object'>] """


#polymorphism & override => if the behavior of the function is different from obj to another we should use override this function and it is called polymorephism



""" class shape :
    def area(self):
        raise NotImplementedError("you should implement this function") # if this class inherited you should override this fnction

class square(shape) :
      def area(self, x , y):# this is the area of square
         self.a = x * y
         return self.a
      
class triangle (shape) :
    def area(self,base , height): # this is the area of triangle
        self.a = 0.5 * base * height
        return self.a
    


sq = square()
print(sq.area(3,4)) # 12

tr = triangle()
print(tr.area(3,4)) # 6 """

#ُEncapsulation => use the (public & private & protected) to restrict access in different levels
#public => all can access it even from the outside
#private(__name) => the class only can access it
#protected(_name) => the class and it's children 

#public
""" class b1 :

    def __init__(self,name):
        self.name = name    


obj1 = b1("lol")
print(obj1.name) #  "name" is public i can access it from outside the class
 """

#protected
""" class b2:
       

    def __init__(self):
        self._name = "lol"

class chforb2(b2):
    def  ccessparent(self):
        self._name = "sayed"
        return self._name  # name is protected can access from child


chb2 = chforb2()

print(chb2.ccessparent()) #sayed """


#private
""" 
class base :

    def __init__(self) :
        self.__age = 13

ob = base()

print(ob.__age) #can't access private attribute (can access only from it's class) """



# setters & getters 

""" class base :

    def __init__(self) :
        self.__age = 13

    def set_age (self,new_age): # to set the value of the privalte attribute
        self.__age = new_age

    def get_age(self):         # to get the value of the privalte attribute
        return self.__age    




ob = base()
print(ob.get_age()) # 13

ob.set_age(21) 
print(ob.get_age()) # 21 """


# @property

""" class base :

    def __init__(self,n_name) :
        self.name = n_name


    def get_age(self):         # if the fun have just the "self" we can give it "@property" to treat with it like "attribute" 
        return self.name 
    
    @property
    def   say_hello(self):            
        return f"hello {self.name}"


obj = base("ali")


print(obj.say_hello) # hello ali "treated as property"
print(obj.get_age)  # can't print it's return (as it a function) """

# abstract class  => have one or mor abstract method ( which is methods should be implemented in the child)

""" from abc import ABCMeta , abstractclassmethod 

class vehicle(metaclass  = ABCMeta) :
      
    @abstractclassmethod
    def type_veihcle(self):  # should implement (override) this function in each children
        pass


class car(vehicle) :

    def type_veihcle(self):
        return "car"
    

class truck(vehicle) :
    def type_veihcle(self):
        return "truck"
    


carobj = car()

print(carobj.type_veihcle()) """


#***********************************************************************************************************
######################################### Advanced #########################################################
############################################################################################################

#__name__  => it is a built in function and it's value is "__main__" (tell you if the file running directly or imported )

# if __name__ = "__main__" => so the file runing directly else it is imported



