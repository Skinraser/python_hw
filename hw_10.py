date_of_birth_and_death = 'Marcus Aurelius*121-08-28*180-11-20'
lst = date_of_birth_and_death.split('*')
name = lst[0]
date_of_birth = lst[1]
date_of_death = lst[2]
date1 = date_of_birth.split('-')
date2 = date_of_death.split('-')
years_of_birth = int(date1[0])
years_of_death = int(date2[0])
age = years_of_death - years_of_birth
print(name, age)
