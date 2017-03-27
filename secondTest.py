#Question 1
import math
print(math.pi)

#Question 2
x = 5
for i in range(x):
    x = x + i
    print(x, end=" ")

#Question 5
text = "Enjoy the test"
result = text.strip().split()[0]
print("\n" + result)

#Question 6
def fn(x, y):
    z = x + y

print(fn(1, 2))

#Question 10
try:
    x = int("zero")
    print(10 / x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")