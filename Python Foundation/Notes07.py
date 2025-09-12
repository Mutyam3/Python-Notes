## Tuple : 

    # => Immutable
    # Tuples basically be used in such programs in such applications 
    # where the definition of an item is required just for one time
    # you cannot perform any operations on it you can only replace that tuple 


p = (1,2,3)

l = ["Mutyam", 1, 5,True]

t = tuple(l)
print(t)

# create an empty tuple 

my_tuple = tuple()

print(type(my_tuple)) # tuple 

my_tuple = ()

print(type(my_tuple)) # tuple

my_tuple = ('Mutyam', 'Bhargav', 'Reddy')

print(my_tuple[0])  # Mutyam


#my_tuple[0] = 'Mahesh' # TypeError : 'tuple object doesnot support item assignment
# the item in the tuple cannot be changed but whole item can be changed i.e replcament is possible (reassignment is possible) 
# my_tuple = ('Hello', 'World')
# print(type(my_tuple)) # <class 'tuple'> 
# # print(my_tuple)  # ('Hello', 'World')

# inbuilt function : 

print(my_tuple.count('Mutyam')) #1 

print(my_tuple.index('Reddy')) #2 






   
