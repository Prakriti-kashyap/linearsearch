t1 =("C", 123, 1000, 67.9, "245", "quant", 56.0)
t2 = (45.9, "ruby", "c++")
print(t1)
print(t2)

#INDEXING
print(t1[3])


#CONCATENATION
print(t1+t2)

#SLICING
print(t1[1:3])
print(t2[0:3])


#REPETITION
print(t1*3)


#MEMBERSHIP

a= 245
if ( a in t1 ):
    print ("element 2 is in list1")
else:
    print ("element 2 is not in list1")
