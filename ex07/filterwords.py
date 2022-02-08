import sys
from string import punctuation

l = len(sys.argv)

if l != 3:
    print("ERROR")
else:
    try:
        n = int(sys.argv[2])
        check_punc = lambda c: c if c not in punctuation else ' '
        no_punc_string = ''.join([check_punc(c) for c in sys.argv[1]])
        no_punc_string.replace('\t',' ')
        filtred_list = [word for word in no_punc_string.split(' ') if len(word) > n]
        print(filtred_list)

    except:
        print("ERROR")