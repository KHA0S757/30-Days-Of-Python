# 'Day 2: 30 Days of python programming'
#Exercise 1
firstname= 'KHAOS'
lastname = 'KiTTy' 
country='USA'
city='CheezyPeakez'
age=37
year=2025
is_married = 'Raeeebabyy'
is_true = "FAWK"
is_light_on = False
personal_info = print(firstname, lastname, age, country, city)
#Exercise 2
#2.1
print(type(firstname))
print(type(lastname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(personal_info))
#2.2
print(len(firstname))
#2.3
print(len(lastname)==len(firstname))
#2.4
num_one = 5
num_two = 4
#2.5
print(num_one+num_two)
#2.6
diff=(num_one - num_two)
#2.7
product = (num_one**num_two)
#2.8
division = (num_one/num_two)
#2.9
remainder = (num_two%num_one)
#2.10
exp = (num_one**num_two)
#2.11
floor_division=(num_one//num_two)
#2.12
pi = 3.14
radius = float(input("radius: "))
area_of_circle = pi * radius**2
print("Area: " + str(area_of_circle))
circum_of_circle = (2*pi*radius)
print(circum_of_circle)
print("current user: ",firstname,lastname,country,age)
firstname, lastname, country, age = input('Input the following separated by spaces First Name:, Last Name: , Country:, Age:').split()
#print (firstname,lastname,country,age)
print("NEW user: ",firstname,lastname,country,age)
help(print)


