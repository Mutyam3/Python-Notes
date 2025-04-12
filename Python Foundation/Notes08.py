
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

x = marks[subject]
print(x)













        
          
     








