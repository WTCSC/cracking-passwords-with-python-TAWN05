import re
import text_utils
def jill(dfilename, pfilename):
    passwd = []
    usrname = []

    # Opens are reads files makes ptext or password text
    pfile = open(f'{pfilename}', 'r')
    pnlines = text_utils.count_lines(pfilename)
    ptext = pfile.read()

    dfile = open(f'{dfilename}', 'r')
    dtext = dfile.read()

    # Makes and splits ptext into rptext or read password text this splits the text by new lines and colens 
    rptext = re.split('[\n:]', ptext)

    rdtext = dtext.split('\n')

    # Defines b the var used to determen wheather it is a username or a password
    for b in range(0, (pnlines * 2)):

        # if b is not divisable by 2 it is a password text and if it is, it is a username text 
        # this method is used becuase i can use .format to give the same format as the passwords.txt and allow the user to see an easy match
        if b % 2 != 0:
            passwd += [rptext[b]]
        else:
            usrname += [rptext[b]]
    print(rdtext[3])
    i = 3
    
    return "{0:02}:{1:02}".format(usrname[i], passwd[i])
"""try:
    filename = input("Enter the line number: ")
    result = (filename)
    print(f"The number on line {line_number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")"""
print(jill("wordlist.txt", "passwords.txt"))