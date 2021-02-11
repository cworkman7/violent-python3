# UNIX Password Cracker
# crypt() algorithm hashes UNIX passwords
from crypt import crypt


def test_pass(crypt_pass):
    '''
    This function takes the encrypted password as a parameter and
    returns either finding the password or exhausting the words in
    the dictionary.
    '''
    # strips out the salt from the first two characters of the 
    # encrypted password hash
    salt = crypt_pass[:2]
    dict_file = open('dictionary.txt', 'r')

    for word in dict_file.readlines():
        crypt_word = crypt(word.strip('\n'), salt)
        # opens the dictionary and iterates through each word in
        # the dictionary, creating an encrypted password hash from the
        # dictionary word and the salt.
        if crypt_word == crypt_pass:
            # if the result matches our encrypted password hash
            print(f'[+] Found Password: {word}\n')
            return
    # if none of the dictionary match, after iterating through
    print('[-] Password Not Found.\n')
    return


if __name__ == '__main__':
    '''
    This function opens the encrypted password file "passwords.txt"
    and reads the content of each line in the password file. For 
    each line, it splits out the username and the hashed password.
    For each individual hashed password, the test_pass() function is 
    called that tests passwords against a dictionary file.
    '''
    pass_file = open('passwords.txt')
    for line in pass_file.readlines():
        if ':' in line:
            user = line.split(':')[0]
            _crypt_pass = line.split(':')[1].strip()
            print(f'[*] Cracking Password For: {user}')
            test_pass(_crypt_pass)
