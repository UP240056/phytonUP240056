# Ejercicio 1

first = "Thirty"
second = "Days"
third = "Of"
foruth = "Phyton"
space = " "
total_phrase = first + space + second + space + third + space + foruth

print(total_phrase)


# Ejercicio 2

fir = "Coding"
sec = "For"
thi = "All"
tot_phr = fir + space + sec + space + thi

print(tot_phr)


# Ejercicio 3

company = "Coding for All"


# Ejercicio 4

print (company)


# Ejercicio 5

print(len(company))


# Ejercicio 6

company = company.upper()  
print(company)  


# Ejercicio 7

company = company.lower()
print(company)


# Ejercicio 8

company = company.capitalize()
print(company)

company = company.title()
print(company)

company = company.swapcase()
print(company)


# Ejercicio 9

company = company.split()
print(company)


# Ejercicio 10

company = "Coding for All"
contains_coding = "Coding" in company
print(contains_coding)


# Ejercicio 11

company = 'Coding for All'
print(company.replace('Coding', 'Phyton'))


# Ejercicio 12

company = "Phyton for All"
print(company.replace('Phyton', 'Everyone to Phyton'))


# Ejercicio 13

company = "Coding for All"
company = company.split(" ")
print(company)


# Ejercicio 14

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(", ")
print(split_companies)


# Ejercicio 15

company = "Coding For All"
company0 = company[0]
print(company0)


# Ejercicio 16

company = "Coding for All"
print(len(company) - 1)


# Ejercicio 17

company = "Coding For All"
company10 = company[10]
print(company10)


# Ejercicio 18

company = "Python For Everyone"
acronym = ''.join([word[0] for word in company.split()])
print(acronym)


# Ejercicio 19

company = "Coding for All"
acronym2 = ''.join([word[0] for word in company.split()])
print(acronym2)

# Ejercicio 20

position1 = company.index("C")
print(position1)


# Ejercicio 21

position2 = company.index("f")
print(position2)


# Ejercicio 22

company99 = "Coding For All People"
last_position = company99.rfind("l")
print(last_position)


# Ejercicio 23

sentence = "You cannot end a sentence with because because because is a conjunction"
sentence_pos = sentence.index("because")
print(sentence_pos)


# Ejercicio 24

sentence = 'You cannot end a sentence with because because because is a conjunction'
last_position = sentence.rindex("because")
print(last_position)

# Ejercicio 25

start_index = sentence.index('because')  # Returns 21

phrase = 'because because because'

end_index = start_index + len(phrase)

sliced_phrase = sentence[start_index:end_index]
print(sliced_phrase)


# Ejercicio 26

sentence = "You cannot end a sentence with because because because is a conjunction"
sentence_pos = sentence.index("because")
print(sentence_pos)


# Ejercicio 27

start_index = sentence.index('because')  # Returns 21

phrase = 'because because because'

end_index = start_index + len(phrase)

sliced_phrase = sentence[start_index:end_index]
print(sliced_phrase)


# Ejercicio 28

company = "Coding for All"
print(company.startswith('Coding'))


# Ejercicio 29

print(company.endswith('Coding'))


# Ejercicio 30

spaces = " Coding For All "
newspace = spaces.strip(" ")
print(newspace.isalpha( ))
print (newspace)


# Ejercicio 31

f1 = '30DaysOfPython'
print(f1.isidentifier()) 

f2 = 'thirty_days_of_python'
print(f2.isidentifier())


# Ejercicio 32

libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
hash = ' #'.join(libraries)
print(hash)


# Ejercicio 33

print("I am\nenjoying\nthis challenge.\nI just\nwonder what\nis next.")


# Ejercicio 34

print("Name\tAsabeneh\nAge\t250\nCountry\tFinland\nCity\tHelsinki")


# Ejercicio 35

r = 10
pi = 3.14
area = pi * r ** 2
fs = 'The area of a circle with a radius {} is {:.2f}.'.format(r, area)
print(fs)


# Ejercicio 36

a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a,b,a**b))