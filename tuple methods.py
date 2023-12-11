t1 =("C", 123, 1000, 67.9, "245", "quant", 56.0)
t2 = (45.9, "ruby", "c++")

#METHOD1 COUNT
a = t1.count(1)
print (a)

#METHOD2 INDEX
b= t1.index(1000)
print(b)


#METHOD 3 MAX
tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)
print ("Max value element : ", max(tuple1))
print ("Max value element : ", max(tuple2))

#METHOD 4 MIN
print ("Min value element : ", min(tuple1))
print ("Min value element : ", min(tuple2))


#METHOD 5 LEN
print ("First tuple length : ", len(tuple1))
print ("Second tuple length : ", len(tuple2))

