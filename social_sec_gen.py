#!usr/bin/python3.7
# Date: Mon 27 May 2019 09:24:24 CEST 
# Author: Nicolas Flandrois
# Description: Script creating a French social security number
from random import randrange, choice

#First digit: sex/gender
sex = randrange(1, 3)

#Second 2 digits: Year of birth
birth_year = randrange(0,100)

#Third 2 digits: Month of birth
birth_month = randrange(1, 13)

#Fourth 2 digits: Birth department area
# dep = [] 
# #Department area code for Corsica Noth/South
# #Department area code number 20 is replaced by 2A & 2B
# for i in range(1, 100):
# 	if i == 96:
# 		continue
# 	# elif i == 20:
# 	# 	dep.append("2A")
# 	# 	dep.append("2B")
# 	# 	continue
# 	dep.append(i)

# #Over seas departments are 972, 971, 973, 974, 976 - How to check the next nb.
# birth_dep = choice(dep)

birth_dep = randrange(1, 100) #for easier computing, and fake numbers anyway

#3 next digits define the 'commune' code between 1 and 999
#NB: Over seas departments are 972, 971, 973, 974, 976 (or from 970 to 989, 
#counting overseas territories)
#How to make it dependant from department, in range from 1 to 99?
#How to define the city/place of bith for international numbers within 99?
#For all above questions, make it random. Association with a place/city 
#or country of birth will be define in building the database in corelation with 
#official list
birth_city = randrange(1, 1000)

#3 last digits of ID or "N° d'ordre"
birth_id = randrange(1, 1000)


ss_int = int('{}{:02d}{:02d}{:02d}{:03d}{:03d}'.format(
	sex, birth_year, birth_month, birth_dep, birth_city, birth_id))

control_key = int(97-(ss_int-((round((ss_int/97), 0))*97)))

ss_str = '{} {:02d} {:02d} {:02d} {:03d} {:03d} - {:02d}'.format(
	sex, birth_year, birth_month, birth_dep, birth_city, birth_id, control_key)
print('auto: ', ss_str)
#print('manual verification: ',
# sex, birth_year, birth_month, birth_dep, birth_city, birth_id, control_key)