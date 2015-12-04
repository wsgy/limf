#!/bin/env python
"""A command line tool for uploding stuff to pomf.se clones"""
import argparse
import urllib
import json
from .parse_arguments import parse_arguments
def main():
    """Creates arguments and parses user input"""
    try:
        url = "https://raw.githubusercontent.com/lich/limf/master/host_list.json"
        clone_list = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    except urllib.error.URLError:
        print("Check your internet connection.")
        exit()
    #Dynamically generate host list from json hosted on github
    host_string = 'Select hosting: '
    for i in range(0, len(clone_list)):
        if i == len(clone_list)-1:
            host_string += '{} - {}'.format(str(i), clone_list[i][2])
        else:
            host_string += '{} - {}, '.format(str(i), clone_list[i][2])
    parser = argparse.ArgumentParser(
        description='Uploads selected file to working pomf.se clone')
    parser.add_argument('files', metavar='file', nargs='+', type=str,
                        help='Files to upload')
    parser.add_argument('-c', metavar='host number', type=int,
                        dest='host', default=None,
                        help=host_string)
    parser.add_argument('-l', dest='only_link', action='store_const',
                        const=True, default=False,
                        help='Changes output to just link to the file')
    parser.add_argument('-e', dest='encrypt', action='store_const',
                        const=True, default=False,
                        help='Encrypts then uploads the files.')
    parser.add_argument('-d', dest='decrypt', action='store_const',
                        const=True, default=False,
                        help='Decrypts files from links with encrypted files')
    args = parser.parse_args()
    if args.host and args.host not in range(0, len(clone_list)):
        print('Please input valid host number')
        exit()
    try:
        parse_arguments(args, clone_list)
    except FileNotFoundError:
        print('Plese enter valid file.')

if __name__ == '__main__':
    main()
