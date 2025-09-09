
# Sets : 

    # unordered 
    # iterable 
    # mutable 
    # no duplicate elements 
    # based on a datastructure knowm as hash table 

# Defining an empty set 

set_var = set()
print(set_var) # set_var 
print(type(set_var)) # <class 'set'> 

set_var = {1,2,3,4,3}
print(set_var) # {1,2,3,4} - no duplicates allowed 

set_var = {"Avengers", "IronMan", "Hitman"}
print(set_var) # {"IronMan", "HitMan", "Avengers"}
print(type(set_var)) # set 


# *** Indexing *** => set doesnot support indexing 

# set_var['Avengers'] # Error ==>Type Error :  Indexing set object is not subscriptable 

# *** Inbuilt function in sets *** 

set_var.add('Hulk') 
print(set_var) # {'IronMan', 'HitMan', 'Avengers', 'Hulk'}

# Difference 

set1 = {'Avengers', 'IronMan', 'Hitman'}
set2 = {'Avengers', 'IronMan', 'Hitman', 'Hulk'}

# Intersection 

set2.intersection_update(set1)

print(set2) # {'Avengers','Hitman', 'IronMan'}


# Difference 

print(set2.difference(set1))  # {Hulk}

print(set2) # {'Avengers', 'Hitman', 'IronMan', 'Hulk'}

# Difference update 

set2.difference_update(set1)

print(set2) # {Hulk}













