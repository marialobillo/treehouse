print("A")
try:
    result = "test" + 5
    print("B")
except ValueError:
    print("C")
except TypeError:
    print("D")
else:
    print("E")
print("F")
