import random

l1 = []
for _ in range(10):
    l1.append(random.randint(1, 100))
print(l1)
l1 = tuple(l1)
print(l1)


l1 = [(10, 20, 40,), (40, 50, 60,), (70, 80, 90,)]
for i in range(len(l1)):
    l1[i] = list(l1[i])
for t in range(len(l1)):
    l1[t][-1] = (100)
for n in range(len(l1)):
    l1[n] = tuple(l1[n])
print(l1)
print(type(l1))
for r in range(len(l1)):
    print(type(l1[r]))
