list1=["python", 7.79,100,567,"APPLE", 101,"hello",234]
list2=["god",6.78,9]
print(list1)
print(list2)
       

#LIST CONCATENATION
print( list1+list2)

#LIST SLICING
print(list1[1:3])
print(list2[0:1])

#LIST REPETITION
print (list2*3)


#LIST MEMBERSHIP
a = 100
if ( a in list1 ):
    print ("element 2 is in list1")
else:
    print ("element 2 is not in list1")
