#THIS IS test
with open("hello2.py") as fh:
    count = sum(1 for line in fh for character in line if character.isupper())

print(count)

list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
#print(A0, ":", A1,":",A2,":",A3,":",A4,":",A5,":",A6)
print("---")
print(A3)
print(A4)
print(A5)
print(A6)
