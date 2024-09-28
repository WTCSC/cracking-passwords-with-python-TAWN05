import re
from hashlib import algorithms_available
from typing import assert_never

#from pygments.console import ansiformat
#from pysss import password

import sys

from apt_pkg import sha256sum

import text_utils
import hashlib
import argparse
import time


def jill(pfilename, dfilename, cracked=False, timer=False, algorithm=False):
    # Defines passwd this will be used as all of our hashed passwords
    passwd = []
    # Defines username like passwd this will be all of our usernames
    usrname = []
    # Defines answer this will be the end resault of this program
    answer = []
    # Defines the var used for what username to use from the list.
    a = 0
    # Defines the var used to get the number of not cracked passwords
    d = 0
    start_time = 0
    f = 0

    # Opens are reads files makes password_text or password text, and puts the contents into a string
    password_file = open(pfilename, 'r')
    # Counts the number of lines in password_file for defining usrname, and passwd.
    password_nlines = text_utils.count_lines(pfilename)
    password_text = password_file.read()

    # Opens and reads dictionary file and puts the contents into a string
    dictionary_file = open(dfilename, 'r')
    dictionary_file_nlines = text_utils.count_lines(dfilename)
    dictionary_text = dictionary_file.read()

    # Makes and splits password_text into read_password_text or read password text this splits the text by new lines and colens
    read_password_text = re.split('[\n:]', password_text)
    read_dictionary_text = dictionary_text.split('\n')
    slicer_text = [password_text]

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
        start_time = time.time()
        # Adds 1 to a This is used to pick the correct username
        a += 1

        # Makes a loop that cycles through read_dictionary_text
        for y in read_dictionary_text:
                if algorithm:
                    # Compare the parsed argument value directly
                    if algorithm == 'sha256':
                        used_algorithm = hashlib.sha256(str(y).encode('utf-8'))
                    elif algorithm == 'sha512':
                        used_algorithm = hashlib.sha512(str(y).encode('utf-8'))
                    elif algorithm == 'md5':
                        used_algorithm = hashlib.md5(str(y).encode('utf-8'))
                    elif algorithm == 'sha3-512':
                        used_algorithm = hashlib.sha3_512(str(y).encode('utf-8'))
                    else:
                        print(f"Unsupported algorithm: {algorithm}")
                        return answer  # Exit if the algorithm is not supported
                else:
                    used_algorithm = hashlib.sha256(str(y).encode('utf-8'))
            # Defines the hash and sets the message = to the current value of y also encodes this string
                hashed = used_algorithm
            # Turns the raw hash into hex
                hex_digest = hashed.hexdigest()
            # Compairs the password hash with the dictionary hash
                if x == hex_digest:
                    end_time = time.time()
                     # If the hashed password and hashed dictionary text match then it adds the username and password to answer
                    times = ''

                    if timer:
                        times = ' ({0:.5f} seconds)'.format(end_time - start_time)

                    answer += ['{0:02}:{1:02}{2}'.format(usrname[(a - 1)], y, times)]
                    #answer.append(f"{usrname[a -1]}:{y} {times}")
                else:
                    d += 1

    d = ((d - (dictionary_file_nlines * password_nlines)))
    if cracked:
        print(f"Number of passwords not cracked: {d}")
    password_file.close()
    dictionary_file.close()
    return answer

# Makes a variable to display answer in the correct format.
def main():
    parser = argparse.ArgumentParser(description='cracked passwords from two readable txt files')
    
    parser.add_argument('password_filename', help='The file to read dictionarys from')
    
    parser.add_argument('dictionary_filename', help='the file to read the password list')

    parser.add_argument("-t", "--timer", help="gives time for each passed password",
                        action="store_true")
    
    parser.add_argument("-c", "--cracked", help="gives number of passwords not cracked",
                        action="store_true")
    
    parser.add_argument("-a", "--algorithm", help="sets a specific algorithm for the cracker",
                        choices=['sha256', 'sha512', 'md5', 'sha3-512'])

    args = parser.parse_args()
    # Makes a variable to display answer in the correct format.
    passwords = jill(args.password_filename, args.dictionary_filename, args.cracked, args.timer, args.algorithm)
    for x in passwords:
        print(x)

if __name__ == '__main__':
    main()

# this is for testing
"""jill("passwords.txt","wordlist.txt", "-c","-t", "sha512")
passwords = jill("passwords.txt", "wordlist.txt", "-c", "-t", "sha512")
for x in passwords:
    print(x)"""