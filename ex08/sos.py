import sys

if len(sys.argv) <= 1:
	exit()

args = [string.upper() for string in sys.argv[1:]]

morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
			'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
			'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
			'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--','X':'-..-',
			'Y':'-.--', 'Z':'--..', ' ' : '/','1':'.----', '2':'..---',
            '3':'...--', '4':'....-', '5':'.....','6':'-....', '7':'--...',
            '8':'---..', '9':'----.', '0':'-----'}

morse_words_list = []

try:
	for string in args:
		morse_words_list.append(" ".join([morse_dict[letter] for letter in string]))
except:
	print("ERROR")
	exit()

result = " / ".join(morse_words_list)

print(result)