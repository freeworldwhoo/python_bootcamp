t = tuple((19, 42, 21))

l = len(t)
if (l == 0):
    exit(print("no number"))
numbers = ", ".join(map(str, t))
print(f"The {l} numbers are: {numbers}")