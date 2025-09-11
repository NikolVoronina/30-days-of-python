first_name = "Nikol"
last_name = "Voronina"
age = 21
city = 'Oslo'
is_married = False
skills = ['HTML', 'CSS', 'JavaScript', 'Next.js']
person_info = {
    'firstname' : 'Nikol',
    'lastname' : 'Voronina',
    'city':'Oslo',
    'country' : 'Norway'
}


print('Hello, World!')
print('Hello' ,',', 'World', '!')
print(len('Hell, World!')) #How many symbols we have in the argument; Result - 12


print('First name:', first_name)
print('First name length:', len (first_name))
print('Last name: ', last_name)
print('Last name length:', len (last_name))
print('Country:', city)
print('Age', age)
print('Married:', is_married)
print('Skills:', skills)
print('Personal ifo:', person_info)


#Multiple variable in a Line
first_name, last_name, city, age, is_married, = 'Nikol', 'Voronina', 'Oslo', 21, False
print(first_name, last_name, city, age, is_married)
print('First name:', first_name)
print('Last name', last_name)
print('Age:', age)
print('City', city)
print('Married :' , is_married)


#Gettitng user input() built-in function
your_name = input('What is your name?')
your_age = input('How old are you?')

print('Your name is:',your_name)
print('Your age is:', your_age)


