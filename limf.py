#!/bin/env python
"""
Copyright 2015 Mikołaj 'lich' Halber <lich@cock.li>
Distributed under the terms of WTF Public License v2.
See http://www.wtfpl.net/txt/copying for the full license text.
"""
import re
import random
import urllib
import shlex
from subprocess import Popen,PIPE,check_output
try:
    check_output(["gpg", "-h"])
    encryption_disabled = False
except FileNotFoundError:
    encryption_disabled = True
try:
    import requests
    import argparse
except ImportError:
    print('Install argparse and request libraries.')
    exit()

def upload_files(selected_file, selected_host, only_link, file_name):
    """
    Uploads selected file to the host, thanks to the fact that
    every pomf.se based site has pretty much the same architecture.
    """
    try:
        answer = requests.post(
            url=selected_host[0]+"upload.php",
            files={'files[]':selected_file})
        if only_link:
            return selected_host[1]+(
                re.findall('"url":"(.+)",', answer.text)[0])
        else:
            return file_name+" : "+selected_host[1]+(
                re.findall('"url":"(.+)",', answer.text)[0])
    except requests.exceptions.ConnectionError:
        print(file_name + ' couldn\'t be uploaded to ' + selected_host[0])
def encrypt_files(selected_file, selected_host, only_link, file_name):
    """
    Encrypts file with gpg and random generated password
    """
    if encryption_disabled:
        print('For encryption please install gpg')
        exit()
    passphrase = '%030x' % random.randrange(16**30)
    source_filename = file_name
    cmd = 'gpg --batch --symmetric --cipher-algo AES256 --passphrase-fd 0 ' \
          '--output - {}'.format(source_filename)
    # error handling omitted
    p = Popen(shlex.split(cmd), stdout=PIPE, stdin=PIPE, stderr=PIPE)
    encrypted_data = p.communicate(passphrase.encode())[0]
    return upload_files(encrypted_data, selected_host,only_link,file_name)+'!'+passphrase

def main():
    """
    Creates arguments, and list of working clones
    """
    parser = argparse.ArgumentParser(
        description='Uploads selected file to working pomf.se clone')
    parser.add_argument('files', metavar='file', nargs='+', type=str,
                        help='Files to upload')
    parser.add_argument('-c', metavar='host number', type=int,
                        dest='host', default=None,
                        help=('Select hosting: 0 - 1339.cf, 1 - bucket.pw,'
                              ' 2 - xpo.pw, 3 - pomf.cat, 4 - pomf.hummingbird.moe.'))
    parser.add_argument('-l', dest='only_link', action='store_const',
                        const=True, default=False,
                        help='Changes output to just link to the file')
    parser.add_argument('-e', dest='encrypt', action='store_const',
                        const=True, default=False,
                        help='Encrypts uploaded files')
    parser.add_argument('-d', dest='decrypt', action='store_const',
                        const=True, default=False,
                        help='Decrypts uploaded files')
    args = parser.parse_args()
    #fixme check if clone is active or not.
    clone_list = [
        ["http://1339.cf/", "http://a.1339.cf/"],
        ["https://bucket.pw/", "https://dl.bucket.pw/"],
        ["http://xpo.pw/", "http://u.xpo.pw/"],
        ["http://pomf.cat/", "http://a.pomf.cat/"],
        ["http://pomf.hummingbird.moe/","http://a.pomf.hummingbird.moe/"]
    ]
    #upload every file selected to random or chosen host
    try:
        for i in args.files:
            if args.host:
                print(upload_files(open(i,'rb'), 
                      clone_list[args.host],args.only_link, i))
            elif args.encrypt and args.host:
                print(encrypt_files(open(i, 'rb'),
                      clone_list[args.host],args.only_link, i))
            elif args.encrypt:
                print(encrypt_files(open(i,'rb'),clone_list[random.randrange(
                      0,len(clone_list))], args.only_link, i))
            else:
                print(upload_files(open(i,'rb'), clone_list[random.randrange(
                      0,len(clone_list))], args.only_link, i))
        exit()
    except IndexError as i:
        print('Please enter valid server number.')
        exit()

if __name__ == '__main__':
    main()
