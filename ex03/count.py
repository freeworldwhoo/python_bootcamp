from string import punctuation

def text_analyzer(*args):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    l = len(args)
    if l == 0:
        text = input("What is the text to analyse?\n")
    elif l > 1:
        print("ERROR")
        return
    else:
        text = args[0]
    upper = 0
    lower = 0
    punc = 0
    space = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        elif c in punctuation:
            punc += 1
    print("The text contains",len(text),"characters:")
    print("-",upper,"upper letters")
    print("-",lower,"lower letters")
    print("-",punc,"punctuation marks")
    print("-",space,"spaces")
