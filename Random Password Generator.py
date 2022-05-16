import random

#A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#....
lowercaseletter1 = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
#enerate password using all the characters, in random order
punctuation = chr(random.randint(128,152))
punctuation2 = chr(random.randint(128,152))
digit = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseletter1+lowercaseletter2+punctuation+punctuation2+digit+digit2
password = shuffle(password)

#Ouput
print(password)