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
        
r = Rectangle(5, 6)
# direct access of protected member
print("Width: {:d}".format(r._width))




