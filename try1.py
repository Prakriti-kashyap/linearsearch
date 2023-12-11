a,b=1,0
try:
          print(a/b)
          print("This won't be printed")
          print('10'+10)
except TypeError:
          print("You added values of incompatible types")
except ZeroDivisionError:
          print("You divided by 0")
