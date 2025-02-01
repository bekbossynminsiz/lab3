#Creating a Function
def my_function():
    print("Hello from a function")

#Calling a Function
def my_function():
    print("Hello from a function")
my_function()

#Arguments
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments
def my_function(fname, Iname):
    print(fname + " " + Iname)
my_function("Emil", "Refsnes")
"""
#This function expects 2 arguments, but gets only 1:
def mu_function(fname, Iname):
    print(fname + " " + Iname)
my_function("Emil")
"""

#Arbitrary Arguments (*)
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments (**)
def my_function(**kid):
   print("His last name is" + kid["Iname"])
my_function(fname = "Tobias", Iname = "Refsnes")

#Default Parameter Value
def my_function(country = "Norway"):
   print("I am from" + country)

my_function("Sweden")
my_function()
my_function("India")
my_function("Brazil")

#Passing a List as an Argument
def my_function(food):
   for x in food:
      print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement
def myfunction():
  pass

#Positional-Only Arguments
def my_function(x, /):
   print(x)
my_function(3)

def my_function(x):
  print(x)

my_function(x = 3)

"""
def my_function(x, /):
  print(x)

my_function(x = 3)
"""

#Keyword-Only Arguments
def my_function(*, x):
   print(x)
my_function(x = 3)

def my_function(x):
   print(x)
my_function(3)

"""
def my_function(*, x):
  print(x)

my_function(3)
"""

#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
   print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
