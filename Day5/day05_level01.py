# Ej. 1

lst = list()
print(lst)

# Ej. 2

videogames = ["Minecraft", "Roblox", "God of War", "Red Dead Redemption 2", "The Last of Us", "Rocket League", "Cyberpunk 2077"]
print("A list of 7 videogames: ",videogames)

# Ej. 3

print("Length of the list: ", len(videogames))


# Ej. 4

first_videogame = videogames[0] 
print(first_videogame)  

middle_videogame = videogames[3]
print(middle_videogame)

last_videogame = videogames[6]
print(last_videogame)

# Ej. 5

mixed_data_types = ["José Luis Rangel Zayas", "18", "170", "Single", "Earth"]
print("My name, age, height, marital status and place where I live: ",mixed_data_types)

# Ej. 6

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Ej. 7

print(it_companies)

# Ej. 8

print("Number of companies in the list: ", len(it_companies))

# Ej. 9

first_company = it_companies[0] 
print(first_company)  

middle_company = it_companies[3]
print(middle_company)

last_company = it_companies[6]
print(last_company)

# Ej. 10

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
index = it_companies.index("Apple") 
it_companies[index] = "Improving" 
print(it_companies)

# Ej. 11

it_companies.append('Nvidia')
print(it_companies)

# Ej. 12

it_companies.insert(getmid ,'Intel')
print(it_companies)

# Ej. 13

del it_companies[0]
it_companies.insert(0, 'FACEBOOK')
print(it_companies)

# Ej. 14

it_companies.append ('#;&nbsp; ')
print(it_companies)

# Ej. 15

does_nvidia = 'Nvidia' in it_companies
print(does_nvidia)

# Ej. 16

it_companies.sort()
print(it_companies)

# Ej. 17

it_companies.sort(reverse=True)
print(it_companies)

# Ej. 18
minusthreefcomp = it_companies[3:-1]
print(minusthreefcomp)

# Ej. 19

minusthreelcomp = it_companies[0:-4]
print(minusthreelcomp)

# Ej. 20

sliceoutmidcomp = it_companies[4]
it_companies.remove(sliceoutmidcomp)
print(it_companies)

# Ej. 21

firstcomp = it_companies[0]
it_companies.remove(firstcomp)
print(it_companies)

# Ej. 22

print('22. Remove the middle IT company or companies from the list')

midcomp = it_companies[3]
it_companies.remove(midcomp)
print(it_companies)

# Ej. 23

lastcomp = it_companies[-1]
it_companies.remove(lastcomp)
print(it_companies)

# Ej. 24

it_companies.clear()
print(it_companies)

# Ej. 25

it_companies.clear()
print(it_companies)

# Ej. 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
back_and_front_end = front_end + back_end
print(back_and_front_end)

# Ej. 27

full_stack = ['Python', 'SQL', 'Redux']
stack_end = back_and_front_end + full_stack
print(stack_end)
