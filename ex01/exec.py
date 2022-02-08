import sys

input_strings_reversed = ' '.join(sys.argv[1:])[::-1].swapcase()
print(input_strings_reversed)