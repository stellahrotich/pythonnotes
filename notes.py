##Arithmetic Operators

#basic arithmetic(Follows PEMDAS)
number = 3 + 2 * 3 / 4.0
print(number)

#Modulo/Remainder
remainder = 7 % 2
print(remainder)

#power
square = 5 ** 2
cube = 2 ** 3
print(square)
print(cube)

##Strings
#concatenation
helloworld = "hello" + " " + "world"
print(helloworld)

#string multiplication
home = "Bomet" * 15
print(home)

#lists
even_numbers = [2,4,6,8,10,12,14,16,18,20]
odd_numbers = [1,3,5,7,9,11,13,15,17,19]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#list multiplication
print([1,2,3] * 3)

#Excercise
/* The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, 
respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating
the two lists you have created.*/

x = object()
y = object()

# create two lists x=list and y=list as follows
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
    
#basic argument specifiers 

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)

