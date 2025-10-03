print (True)
print (False)

print('Addition :' , 1+2)  #Result: 3
print('Subtraction :', 3-2)  #Result: 1
print('Multiplication :', 2*3)  #Result: 6
print('Division :', 6/3)  #Result 2.0
print('Division without the remainder :', 7//2)  #Result: 3, not 3,5
print('Modulus :', 3%2)  #Result: 1
print('Exponentition :', 2**3)  #Result 2*2*2 -> 8


#Floating num
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)


#Complex num
print('Complex nu:', 1+1j)
print('Multiplying comlex numbers:', (1+1j)*(1-1j))


#Example 1 
a = 3
b = 4

total = a+b
diff=a-b
product=a*b
devision=a/b
remainder=a%b
floor_division=a//b
exp=a**b

print(f"total={total}, diff={diff}, product={product}, division={devision}, remainder={remainder}, floor_division={floor_division}, exp={exp}")


#Example 2
print('==Addtion, Subtraction, Multiplication, Division')
num_a=10
num_b=2

total = num_a+num_b
diff=num_a-num_b
prod=num_b*num_a
div=num_a/num_b

print('total :', total)
print('difference :', diff)
print('product :', prod)
print('division :', div)

#Task 1: Calculationg area of a circle.
radius = 35
area_of_circle = 3.14*radius**2  #Here I am using the basic formula
print('Area of circle is :', area_of_circle)


#Task 2: Calculating are of a rectangle.
length = 25
width = 10
area_of_rectangle=length*width
print('Area of the rectangle is :', area_of_rectangle)

#Task 3: Calculating a weight of an object.
mass=100
gravity=9.81
weight=mass*gravity
print('Weight is :', weight)

#Task 4: Calculate the density of a liquid
mass_liquid = 100
volume = 0.075 #in cubic meter
density= mass_liquid/volume #1000 Kg/m^3
print('Density of liquid is :',density)


#Comparison Operators
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)


print('1 is 1', 1 is 1) #True
print ('1 is 2', 1 is 2) #False
print('1 is not 2', 1 is not 2) #True
print('N in Nikol', 'N' in 'Nikol') #True
print('V in Nikol', 'V' in 'Nikol') #False
print('Nikol' in 'My name is Nikol') #True
print('a in an:', 'b' in 'ban') #True
print('4 is 2**2 :', 4 is 2**2) #True



#Exercises - Day 3, task 1: Find the area of a triangle:
base_triangle=int(input('Write the base of triangle :'))
height_triangle=int(input('Write the height of the triangle :'))
triangle_result=0.5*base_triangle*height_triangle
print('The area of the triangle is :', triangle_result )

#Exercises - Day 3, task 2: Find the perimeter of a triangle
side_a=10
side_b=20
side_c=10
result_perimeter=side_a+side_b+side_c
print('The perimeter of the triangle is :', result_perimeter)

#Exercises - Day 3, task 3:



