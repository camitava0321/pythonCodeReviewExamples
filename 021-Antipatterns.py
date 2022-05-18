#Accessing a protected member from outside the class
#Accessing a protected member (a member prefixed with _) of a class from outside that class usually calls for trouble, since the creator of that class did not intend this member to be exposed.
class Rectangle(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.area = width * height
#Assigning a lambda expression to a variable
#The sole advantage that a lambda expression has over a def is that the lambda can be anonymously embedded within a larger expression. If you are going to assign a name to a lambda, you are better off just defining it as a def.

#The following code assigns a lambda function which returns the double of its input to a variable. This is functionally identical to creating a def.

        f = lambda x: 2 * x

#Assigning to built-in function
#Python has a number of built-in functions that are always accessible in the interpreter. Unless you have a special reason, you should neither overwrite these functions nor assign a value to a variable that has the same name as a built-in function. Overwriting a built-in might have undesired side effects or can cause runtime errors. Python developers usually use built-ins ‘as-is’. If their behaviour is changed, it can be very tricky to trace back the actual error.

#In the code below, the list built-in is overwritten. This makes it impossible, to use list to define a variable as a list. As this is a very concise example, it is easy to spot what the problem is. However, if there are hundreds of lines between the assignment to list and the assignment to cars, it might become difficult to identify the problem.
# Overwriting built-in 'list' by assigning values to a variable called 'list'
        list = [1, 2, 3]
# Defining a list 'cars', will now raise an error
        cars = list()
# Error: TypeError: 'list' object is not callable        

r = Rectangle(5, 6)
# direct access of protected member
print("Width: {:d}".format(r._width))

#Bad except clauses order
#When an exception occurs, Python will search for the first exception clause which matches the exception type that occurred. It doesn’t need to be an exact match. If the exception clause represents a base class of the raised exception, then Python considers that exception clause to be a match. E.g. if a ZeroDivisionError exception is raised and the first exception clause is Exception, then the Exception clause will execute because ZeroDivisionError is a sub class of Exception. Therefore, more specific exception clauses of sub classes should always be placed before the exception clauses of their base classes to ensure that exception handling is as specific and as helpful as possible.
#The code below performs a division operation that results in a ZeroDivisionError. The code contains an except clause for this type of error, which would be really useful because it pinpoints the exact cause of the problem. However, the ZeroDivisionError exception clause is unreachable because there is a Exception exception clause placed before it. When Python experiences an exception, it will linearly test each exception clause and execute the first clause that matches the raised exception. The match does not need to be identical. So long as the raised exception is a sub class of the exception listed in the exception clause, then Python will execute that clause and will skip all other clauses. This defeats the purpose of exception clauses, which is to identify and handle exceptions with as much precision as possible.

try:
    5 / 0
except Exception as e:
    print("Exception")
# unreachable code!
except ZeroDivisionError as e:
    print("ZeroDivisionError")
    
    
#Bad first argument given to super()
#super() enables you to access the methods and members of a parent class without referring to the parent class by name. For a single inheritance situation the first argument to super() should be the name of the current child class calling super(), and the second argument should be self (that is, a reference to the current object calling super()).

#Python raises a TypeError when it attempts to execute the call to super() below. The first argument should be the name of the child class that is calling super(). The author of the code mistakenly provided self as the first argument.
class Square(Rectangle):
    def __init__(self, length):
        # bad first argument to super()
        super(self, Square).__init__(length, length)

s = Square(5)
print(s.area)  # does not execute    


#Security Antipattern
#use of exec
#The exec statement enables you to dynamically execute arbitrary Python code which is stored in literal strings. Building a complex string of Python code and then passing that code to exec results in code that is hard to read and hard to test. Anytime the Use of exec error is encountered, you should go back to the code and check if there is a clearer, more direct way to accomplish the task.

#Anti-pattern
#Program uses exec to execute arbitrary Python code
#The sample code below composes a literal string containing Python code and then passes that string to exec for execution. This is an indirect and confusing way to program in Python.
s = "print(\"Hello, World!\")"
exec (s)


#Performance Antipattern
#Using key in list to check if key is contained in list
#Using key in list to iterate through a list can potentially take n iterations to complete, where n is the number of items in the list. If possible, you should change the list to a set or dictionary instead, because Python can search for items in a set or dictionary by attempting to directly accessing them without iterations, which is much more efficient.

#The code below defines a list l and then calls if 3 in l to check if the number 3 exists in the list. This is inefficient. Behind the scenes, Python iterates through the list until it finds the number or reaches the end of the list.
l = [1, 2, 3, 4]

# iterates over three elements in the list
if 3 in l:
    print("The number 3 is in the list.")
else:
    print("The number 3 is NOT in the list.")
    
    
#Using an unpythonic loop
#PEP 20 states “There should be one– and preferably only one –obvious way to do it.” Creating a loop that uses an incrementing index to access each element of a list within the loop construct is not the preferred style for accessing each element in a list. The preferred style is to use enumerate() to simultaneously retrieve the index and list element.
#The code below uses an index variable i in a for loop to iterate through the elements of a list. This is not the preferred style for iterating through a list in Python.
l = [1,2,3]

# creating index variable
for i in range(0,len(l)):
    # using index to access list
    le = l[i]
    print(i,le)