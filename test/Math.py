import random

"""

from typing import Union

for i in range(3):
  print("hello")


a = "hej"
print(a+a)
print(4*a)

b = 5
print(b==5)
print(type(b))

c= [7,9,11,18]
c.append(5)
c.append("hej")
print(c)
c.remove(11)
print(c)

d = [12,"apple",True,0.25]
for ting in d:
       print(ting)
    #   print(ting, end=',')

myList = [1,2,3,4,5,6,7]
print(myList[1:4])



sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
for number in numbers:
    if number > 0:
        newlist.append(number)
print(newlist)

"""
double = lambda x: x * 2

# Output: 10
print(double(6))


def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % (random_number))

# Display multiplication table of 3
num = 3
find_tal = 99 // 3 + 1
min_list = []
print(find_tal)
for i in range(1, find_tal):
    print(num, 'x', i, '=', num * i)
    min_list = num * i


terms = 10

# Uncomment to take number of terms from user
#terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print(result)
# display the result

print("The total terms is:", terms)
for i in range(terms):
    print("2 raised to power", i, "is", result[i])
