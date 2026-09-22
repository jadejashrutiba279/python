#2. Data Types

#1. Demonstrate int, float, str, bool, and complex.
a=10
b=10.2
c="shruti"
d=True
e=2+3j

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))


#2. Accept two numbers and display their data types.
a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("first number type:",type(a))
print("second number type:",type(b))

#3. Convert a string number into an integer and float.
num="20"
int_num=int(num)
float_num=float(num)

print("int:",int_num)
print("float:",float_num)

#4. Find the length of a string.
a=input("Enter a string:")
length=len(a)
print("length of string=",length)

#5. Create a list, tuple, set, and dictionary and display their types.
list=[10,20,30,40,50]
tuple=(10,20,30,40,50)
set={10,20,30,40,50}
dict={"name":"shruti","age":21}
print(list)
print(type(list))

print(tuple)
print(type(tuple))

print(set)
print(type(set))

print(dict)
print(type(dict))



