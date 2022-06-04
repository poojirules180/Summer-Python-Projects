import random

print('Welcome To The Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]\;.?0123456789'

numbers = input('Amount of passwords to generate? : ') #Asks the user how many passwords to create using the chars 
numbers = int(numbers) #turns the value given in line 7 into int value

length = input('Who long should the password be? : ') # Asks the user the length of their auto-gen password
length = int(length) #turns the value given in line 10 into int value

print('\nhere are your passwords: ')

for possibleValue in range(numbers): #runs the loop for # value given in line 7
    password = ' ' #stores the password
    for lenValue in range(length): #runs the loop for # value given in line 10 for each password
        password += random.choice(chars) #using the length value it randomizes the char to create the password til the value is satisfied.
    print(password) 
