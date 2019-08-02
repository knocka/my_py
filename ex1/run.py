import _example as example
x = example.fact(5)
print(x)
y = example.my_mod(7,3)
print(y)
z = example.get_time()
print(z)
w = example.new_Word("meat")
print(example.Word_getWord(w))
example.Word_updateWord(w, "beef")
print(example.Word_getWord(w))
example.delete_Word(w)


