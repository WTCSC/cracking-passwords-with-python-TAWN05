import re
from typing import assert_never

from pygments.console import ansiformat
from pysss import password

import text_utils
import hashlib
import argparse
def jill(dfilename, pfilename):
    # Defines passwd this will be used as all of our hashed passwords
    passwd = []
    # Defines username like passwd this will be all of our usernames
    usrname = []
    # Defines answer this will be the end resault of this program
    answer = ""
    # Defines the var used for what username to use from the list.
    a = 0
    fanswer = []

    # Opens are reads files makes password_text or password text, and puts the contents into a string
    password_file = open(f'{pfilename}', 'r')
    # Counts the number of lines in password_file for defining usrname, and passwd.
    password_nlines = text_utils.count_lines(pfilename)
    password_text = password_file.read()

    # Opens and reads dictionary file and puts the contents into a string
    dictionary_file = open(f'{dfilename}', 'r')
    dictionary_text = dictionary_file.read()

    # Makes and splits password_text into read_password_text or read password text this splits the text by new lines and colens
    read_password_text = re.split('[\n:]', password_text)
    read_dictionary_text = dictionary_text.split('\n')

    # Defines b the var used to determen wheather it is a username or a password
    for b in range(0, (password_nlines * 2)):

        # If b is NOT divisable by 2 it is a password text and if it is, it's a username text
        # this method is used because I can use .format to give the same format as the passwords.txt and allow the user to see an easy match
        if b % 2 != 0:
            passwd += [read_password_text[b]]
        else:
            usrname += [read_password_text[b]]

    # Makes a loop that goes through all strings in passwd
    for x in passwd:
        # Adds 1 to a This is used to pick the correct username
        a += 1
        # Makes a loop that cycles through read_dictionary_text
        for y in read_dictionary_text:
            # Defines the hash and sets the message = to the current value of y also encodes this string
            sha256_hash = hashlib.sha256(str(y).encode('utf-8'))
            # Turns the raw hash into hex
            hex_digest = sha256_hash.hexdigest()
            # Compaiers the password hash with the dictonary hash
            if x == hex_digest:
                # If the hashed password and hashed dictionary text match then it adds the username and password to answer
                #answer += (f'{usrname[(a - 1)]}:{y}\n')
                answer = ('{0:02}:{1:02}'.format(usrname, password))
    password_file.close()
    dictionary_file.close()
    return answer
#print(jill("wordlist.txt","passwords.txt"))
# Makes a variable to display answer in the correct format.
"""def main():
    parser = argparse.ArgumentParser(description='cracked passwords from two readable txt files')
    parser.add_argument('dictionary_filename', help='The file to read passwords from')
    parser.add_argument('password_filename', help='the file to read the dictionary list')
    args = parser.parse_args()
    passwords = jill(args.dictionary_filename, args.password_filename)
    for x in passwords:
        print(x)
if __name__ == '__main__':
    main()"""