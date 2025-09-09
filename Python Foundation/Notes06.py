
# Lists : 

print(type([]))

lst_example = []

print(type(lst_example)) 

lst = list()

print(type(lst))

lst = ['mathematics', 'science', 100,200,300]

type(lst)

# In-built functions

#  **** Append ****

# append is used to add elements in the list. 
lst = ['Bhargav', 100,200,300]

lst.append('Mutyam')

print('after appending the element', lst)

lst.append(['John', 'cena']) # it get append nested list to that list

#Indexing in list 

print(lst[4]) 
print(lst[1:])
print(lst[1:4]) # 'Bhargav to 300 | Mutyam won't included 

# **** Insert **** 

# insert in a specific order 

lst.insert(1,"Reddy")

print(lst)

lst.insert(1, ['Balu', 'Bombay'])

print(lst)


#    **** Extend **** 

lst = [1,2,3,4,5,6]

lst.extend([8,9])

print(lst) # [1,2,3,4,5,6,8,9]


# Various Operations that we perform in list:

lst = [1,2,3,4,5]

print(sum(lst)) #15 

#  *** Pop() Method *** => removes last element 


print(lst.pop()) # 5 

print(lst) # [1,2,3,4]

lst.pop(0) # 1  when u give index for pop method that value is removed from the list.

print(lst) # [2,3,4]


# *** Count() *** ==> Calculate total occurrence of given element of List 

lst = [1,1,2,3,4,5]
print(lst.count(1)) # 2 

# *** length *** => Calculates total length of list 

print(len(lst)) # 6 


# *** index() *** => Returns the index of first occurrence. Start and End Index are not necessary parameters 

print(lst.index(1,0,4)) # 0 index 1 value is present ==> First parameter is value,  second parameter is start index , third parameter is stop index 


# *** min() and max *** => returns the minimum element and maximum element from the list 

print(min(lst)) # 1 

print(max(lst)) # 5 



































nums =  [23, 34, 54, 0, 4, 7]
for (i,v) in enumerate(nums):
        if i != 0: 
         print(v)

num = [23, 34, 54, 0, 4, 7]
  
i = 0

while i < len(nums)-1 :
    print(nums[i])
    i = i + 1 


   