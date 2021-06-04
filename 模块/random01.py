import random

# ran = random.random()
# print(ran)
#
# ran = random.randrange(1, 10, 2)
# print(ran)
#
# ran = random.randint(1, 10)
# print(ran)
list = ['a', 'b', 'c', 'd']
ran = random.choice(list)
print(ran)

random.shuffle(list)
print(list)
