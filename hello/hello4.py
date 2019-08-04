

def forever():
    yield 999
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b

x = all(name ==  name.title() for name in ["A1", "Bb1", "C1"])
print(x)
pass

for x in forever():
    print(x)




