#!/bin/env python
"""
Copyright 2015 Mikołaj 'lich' Halber <lich@cock.li>
Distributed under the terms of WTF Public License v2.
See http://www.wtfpl.net/txt/copying for the full license text.
"""
import re
import random
try:
    import requests
    import argparse
except ImportError:
    print("Install argparse and request libraries.")
    exit()

def upload_files(selected_file, selected_host, only_link):
    """
    Uploads selected file to the host, thanks to the fact that
    every pomf.se based site has pretty much the same architecture.
    """
    try:
        answer = requests.post(
            url=selected_host[0]+"upload.php",
            files={'files[]':open(selected_file, 'rb')})
        if only_link:
            return selected_host[1]+(
                re.findall('"url":"(.+)",', answer.text)[0])
        else:
            return selected_file+" : "+selected_host[1]+(
                re.findall('"url":"(.+)",', answer.text)[0])
    except requests.exceptions.ConnectionError:
        print(selected_file + " couldn't be uploaded to " + selected_host[0])

def main():
    """
    Creates arguments, and list of working clones
    """
    parser = argparse.ArgumentParser(
        description='Uploads selected file to working pomf.se clone')
    parser.add_argument('files', metavar='file', nargs='+', type=str,
                        help='Files to upload')
    parser.add_argument('-c', metavar='host number', type=int,
                        dest='host', default=random.randrange(0, 4),
                        help=("Select hosting: 0 - 1339.cf, 1 - bucket.pw,"
                              " 2 - xpo.pw,3 - pomf.cat."))
    parser.add_argument('-l', dest='only_link', action='store_const',
                        const=True, default=False,
                        help='Changes output to just link to the file')
    args = parser.parse_args()
    #fixme check if clone is active or not.
    clone_list = [
        ["http://1339.cf/", "http://a.1339.cf/"],
        ["https://bucket.pw/", "https://dl.bucket.pw/"],
        ["http://xpo.pw/", "http://u.xpo.pw/"],
        ["http://pomf.cat/", "http://a.pomf.cat/"]
    ]
    #upload every file selected to random or chosen host
    try:
        for i in args.files:
            print(upload_files(i, clone_list[int(args.host)], args.only_link))
    except IndexError as i:
        print('Please enter valid server number.')

if __name__ == '__main__':
    main()
