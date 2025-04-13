
# Problems on Dictionaries : 
#---------------------------

person = { 
           'firstname' : 'Harry',
           'lastname' : 'Potter',
           'age' : 30,
           'gender' : 'male',
           'skill' : 'Reactjs',
           'expertise' : 'Beginner'
        }

    
""" Questions : 
           
      1. Print  the firstname 
      2. Print the lastname 
      3. Print the fullname ('Harry Potter')
      4. If the age is less than 18, then print 'false'. If the age is more than 18, then print "true". """

#1. print the firstname 

print(person['firstname'])

#2. Print the lastname 

print(person['lastname'])

#3. Print the fullname 

print(f"{person['firstname']} {person['lastname']}" )

#4. if the age is less than 18, then print 'false', if the age is more than 18, then print 'true'.

if person['age'] < 18:
    print('false')
else:
    print('true')


marks = {
           "maths" : 34,
           "english" : 56,
           "science" : 32,
           "hindi" : 75,
           "social science" : 65
        }

"""
  Questions : 

  1. Print the marks of all the subjects : 
  2. Print the names of all the subjects from the given object.
  3. Count the number of subjects from the given object.
  4. Print the percentage of the marks of the subject. 
  5. Print only those subjects where the student scored more than 35
  6. Print the pass/fail status of the subjects provided 35 is the pass mark 
  7. Print only the passed subjects 
  8. Count the number of passed subjects 
  9. Print only the failed subjects 
  10. Count the number of failed subjects 
  11. Print the least scored subject 
  12. Print the highest scored subject
  13. Check whether the student has passed in all the subjects or not. 
  14. Take the subject name from the student through prompt box and print the subject marks and pass/fail status 
"""

print('-------------------------')
#1. Print the marks of all the subjects 

for (subjects,mark) in marks.items():
     print(mark) 

#2. Print the names of all the subjects from the given object 

for (subj,mark) in marks.items():
     print(subj) 

#3. Count the number of subjects from the given object 

count = 0 

for (subj,mar) in marks.items():
     count = count + 1 

print(f"no of subjects : {count}")

#4. Print the percentage of the marks of the subject.  

sum = 0

for (subj, mark) in marks.items():
     sum = sum + mark 
    
percentage = (sum / 500) * 100 

print(percentage)
     
#5. Print only those subjects where the student scored more than 35 

for (subj, mark) in marks.items():
     if mark > 35:
          print(subj)

#6. Print the pass/fail status of the subjects provided 35 is the pass mark 

for (subj, mark) in marks.items():
     if mark >= 35 : 
          print(f"{subj} pass")
     else:
          print(f"{subj} fail")

#7.  Print only the passed subjects  

for (subj, mark) in marks.items():
     if mark >= 35: 
          print(subj)

#8. Count the number of passed subjects

count_passed = 0
for (subj, mark) in marks.items(): 
     if mark >=35:
          count_passed += 1 
print(f"passed subjects count : {count_passed}")

#9. Print only the failed subjects  

for (subj, mark) in marks.items():
     if mark < 35:
          print(subj)

#10.Count the number of failed subjects

count_failed = 0 

for(subj, mark) in marks.items():
     if mark < 35:
          count_failed += 1

print(count_failed)

#11. Print the least scored subject 

min = float('inf')
sub = ''
for(subj, mark) in marks.items():
     if mark < min:
          min = mark 
          sub = subj
    
print(f"least scored subject : {min}")

#12. Print the highest scored subject 

max = float("-inf")
sub = ""

for(subj, mark) in marks.items():
     if mark > max:
          max = mark
          sub = subj 

print(f"highesr scored subjects : {max}")


#13. Check whether the student has passed in all the subjects or not 

count = 0 
index = 0

for (subj, mark) in marks.items():
     index +=1
     if mark >= 35:
          count += 1 

if count == index:
     print("passed all the subjects")
else:
     print("Not Passed in all the subjects")

#14.Take the subject name from the student through prompt box and print the subject marks and pass/fail status  

subject = input("Enter your subject name :")



for (subj, mark) in marks.items():
     if subj == subject:
          if mark > 35:
               print(f"{subj} : {mark} pass")
          else:
               print(f"{subj} : {mark} fail")




"""                       ****   List of Dictionary Problems  ****
"""

products =         [
                            {
                                "name": "Duracell - AAA Batteries (4-Pack)",
                                "type": "HardGood",
                                "price": 5.49,
                                "category": "Household Batteries",
                                "manufacturer": "Duracell",				
                            },
                            {
                                "name": "Hard Rock TrackPak - Mac",
                                "type": "Software",
                                "price": 29.99,
                                "category": "Recording Equipment",
                                "manufacturer": "Hal Leonard",				
                            },
                            {
                                "name": "Duracell - AA 1.5V CopperTop Batteries (4-Pack)",
                                "type": "HardGood",
                                "price": 5.62,
                                "category": "Household Batteries",
                                "manufacturer": "Duracell",				
                            },
                            {
                                "name": "Energizer - MAX Batteries AA (4-Pack)",
                                "type": "HardGood",
                                "price": 5.32,
                                "category": "Household Batteries",
                                "manufacturer": "Energizer",				
                            },
                            {
                                "name": "METRA - Antenna Cable Adapter - Black",
                                "type": "HardGood",
                                "price": 13.99,
                                "category": "Antennas & Adapters",
                                "manufacturer": "Metra",				
                            },
                            {
                                "name": "WipeDrive Six - Mac|Windows",
                                "type": "Software",
                                "price": 23.99,
                                "category": "Maintenance Software",
                                "manufacturer": "White Canyon",				
                            }
                        ]

"""
    Questions : 

  1.  Print all the product names.
  2.  Print all the hardgoods.
  3.  Print all the softwares.
  4.  Print all the categories.
  5.  Print only the products manufactured by Duracell.
  6.  Print the product names in ascending order of their prices.
  7.  Print only those products whose price is more than 14.99.
  8.  Print only those products whose price is less than 9.99.
  9.  Print the total price of all the hardgoods.
  10. Print the average price of the softwares.
"""

print('-------------------------------------------')
# 1. Print all the product names 

for (index, product) in enumerate(products):
     print(product['name'])


#2. Print all the hardgoods 

for (index, product) in enumerate(products):
     if product['type'] == 'HardGood':
          print(product)

#3. Print all the softwares 

for (index, product) in enumerate(products):
     if product['type'] == 'Software':
          print(product)

#4. Print all the categories 

for (index, product) in enumerate(products):
     print(product['category'])


#5. Print only the products manufactured by Duracell 

for (index, product) in enumerate(products):
     if product['manufacturer'] == 'Duracell':
        print(product)

#6. 


#7. Print only those products whose price is more than 14.99. 

for (index, product) in enumerate(products):
     if product['price'] > 14.99:
          print(product)

#8. Print only those products whose price is less than 9.99. 

for (index, product) in enumerate(products):
     if product['price'] < 9.99:
          print(product)

#9. Print the total price of all hardgoods 

total_price = 0

for (index , product) in enumerate(products):
     if product['type'] == 'HardGood':
        total_price += product['price']

print(total_price)
     

#10.Print the average price of the softwares. 

total_price = 0
total_products= 0

for(index, product) in enumerate(products):
     if product['type'] == 'Software':
        total_products += 1
        total_price += product['price']

average = total_price / total_products
print(average)
     

people = [
                            {
                            "firstname": "praveen",
                            "lastname": "gubbala",
                            "age": 36,
                            "gender": "male",
                            "city": "hyd",
                            "salary": 10000
                            },
                            {
                            "firstname": "srikanth",
                            "lastname": "gubbala",
                            "age": 32,
                            "gender": "male",
                            "city": "bengaluru",
                            "salary": 20000
                            },
                            {
                            "firstname": "pradeep",
                            "lastname": "reddy",
                            "age": 21,
                            "gender": "male",
                            "city": "hyd",
                            "salary": 25000
                            },
                            {
                            "firstname": "mounika",
                            "lastname": "mudiraj",
                            "age": 20,
                            "gender": "female",
                            "city": "nalgonda",
                            "salary": 30000
                            },
                            {
                            "firstname": "nikhil",
                            "lastname": "m",
                            "age": 22,
                            "gender": "male",
                            "city": "guntur",
                            "salary": 2000
                            },
                            {
                            "firstname": "riya",
                            "lastname": "bhadouria",
                            "age": 14,
                            "gender": "female",
                            "city": "indore",
                            "salary": 40000
                            }
                            ]


"""
Questions : 
-----------
1. Print all the firstnames.
2. Print all the full names.
3. Print only those names whose age is more than 25.
4. Print all female names.
5. Print only those names whose salary is more than 25000 and increase their salaries by 15%.
6. Using prompt, print only those names whose city is "hyd".
7. Print the total salary of all the people.
8. Print all the female names.
9. Print all the firstnames whose salary is more than 25000.
10.Using prompt, print all names whose city is "hyd".
11.Print all the fullnames in the alphabetical order.
12.Print all the fullnames in the increasing order of their age.
13.Print all the fullnames in the reverse alphabetical order.
14.Print all the fullnames in the decreasing order of their salaries.
15.Print all the cities in which the people live. There should not be any duplicate cities.
16.Print all the male names whose age is greater than 25.
17.Print all names that starts with "p" and the firstname should be in UPPERCASE. e.g. PRAVEEN gubbala.
"""


#1. Print all the firstname 

for (index, person) in enumerate(people):
     print(person['firstname'])

#2. Print all the fullName 

for (index, person) in enumerate(people):
     print(f"{person['firstname']} {person['lastname']}")


#3. Print only those names who age is more than 25 

for (index, person) in enumerate(people):
     if person['age'] > 25:
           print(f"{person['firstname']} {person['lastname']}")

#4. Print all female names 

for (index, person) in enumerate(people):
     if person['gender'] == 'male':
          print(f"{person['firstname']} {person['lastname']}")

#5. Print only those names whose salary is more than 25000 and increase their salaries by 15%. 

percentage = 15 / 100
for (index, person) in enumerate(people):
     if person['salary'] > 25000:
          increment = person['salary'] * percentage
          person['salary'] += increment
          print(person)


#6.  Using prompt, print all names whose city is "hyd".

city_name = input('Enter your city name : ')

for (index, person) in enumerate(people):
     if person['city'] == city_name:
          print(f"{person['firstname']} {person['lastname']}")

#7. Print the total salary of all the people. 

total_salary = 0
for (index, person) in enumerate(people):
     total_salary += person['salary']

print(total_salary)

#9. Print all the firstnames whose salary is more than 25000.

for (index, person) in enumerate(people):
     if person['salary'] > 25000:
          print(person['firstname'])
     

#15. Print all the cities in which the people live. There should not be any duplicate cities.

for (index, person) in enumerate(people):
     print(person['city'])


#16.Print all the male names whose age is greater than 25.

for (index, person) in enumerate(people):
     if (person['age'] > 25 and person['gender'] == 'male'):
          print(f"{person['firstname']} {person['lastname']}")

#17. Print all names that starts with "p" and the firstname should be in UPPERCASE. e.g. PRAVEEN gubbala.

for (index, person) in enumerate(people):
     if person['firstname'][0] == 'p':
          print(f"{person['firstname'].upper()} {person['lastname']}")




     













        
          
     








