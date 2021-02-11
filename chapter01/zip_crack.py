# A brute-force zip-file password cracker
import zipfile
import argparse
from threading import Thread


def extract_file(zfile, password):
    '''
    The extractall() function throws an exception when the password
    is incorrect. Using this, catch the exception and consider it
    an incorrect password.
    '''
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        print(f'[+] Found password: {password}\n')
    except RuntimeError:
        pass


def main(zname, dname):
    '''
    This function utilizes threads of execution to improve performance, 
    which allows simultaneous testing of multiple passwords. For each 
    word in the dictionary, a new thread is spawned.
    '''
    z_file = zipfile.ZipFile(zname)
    with open(dname) as pass_file:
        for line in pass_file.readlines():
            password = line.strip('\n')
            t = Thread(target=extract_file, args=(z_file, password))
            t.start()


if __name__ == '__main__':
    '''
    This function allows the user to specify the name of the zip file to 
    crack and the name of the dictionary file from the command line.
    '''
    parser = argparse.ArgumentParser(usage='zip_crack.py ZIPFILE DICTFILE')
    parser.add_argument('zipfile', type=str, metavar='ZIPFILE',
                        help='specify zip file')
    parser.add_argument('dictfile', type=str, metavar='DICTFILE',
                        help='specify dictionary file')
    args = parser.parse_args()
    main(args.zipfile, args.dictfile)
