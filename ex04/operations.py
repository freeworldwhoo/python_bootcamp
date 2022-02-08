import sys
l = len(sys.argv)

if l < 3:
    print("Usage: python operations.py <number1> <number2>")
elif l > 3:
    print("InputError: too many arguments")
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("Sum        ",a+b)
        print("Difference:",a-b)
        print("Product    ",a*b)
        print("Quotient:  ",a/b if b!=0 else "ERROR (div by zero)")
        print("Remainder: ",a%b if b!=0 else "ERROR (modulo by zero)")
    except:
        print("InputError: only numbers")