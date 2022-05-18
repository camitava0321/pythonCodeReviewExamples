#Accessing a protected member from outside the class
#Accessing a protected member (a member prefixed with _) of a class from outside that class usually calls for trouble, since the creator of that class did not intend this member to be exposed.
class Rectangle(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
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




