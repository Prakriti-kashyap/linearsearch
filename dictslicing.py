
import itertools

# Create a new dictionary variable
myDictionary = {
    "name": "Fred",
    "animal": "cat",
    "colour": "red",
    "age": 3
} 

# Create a sliced dictionary
# dict() is used to convert the iterable result of itertools.islice() to a new dictionary
slicedDict = dict(itertools.islice(myDictionary.items(), 1 ,3))

print(slicedDict)


#REPETITION
print(myDictionary*3)
