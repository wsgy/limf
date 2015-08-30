#!/bin/env python
import argparse
from .parse_arguments import parse_arguments
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
                              ' 2 - pomf.cat, 3 - pomf.hummingbird.moe, 4 - xpo.pw,'
                              ' 5 - mixtape.moe, 6 - maxfile.ro'))
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
    clone_list = [
        ["http://1339.cf/", "http://b.1339.cf/"],
        ["http://bucket.pw/", "http://dl.bucket.pw/"],
        ["http://pomf.cat/", "http://a.pomf.cat/"],
        ["http://pomf.hummingbird.moe/", "http://a.pomf.hummingbird.moe/"],
        ["http://xpo.pw/", "http://u.xpo.pw/"],
        ["https://mixtape.moe/", "https://my.mixtape.moe/"],
        ["https://maxfile.ro/static/", "https://d.maxfile.ro/"]
    ]
    if args.host and args.host not in range(0, len(clone_list)):
        print('Please input valid host number')
        exit()
    try:
        parse_arguments(args, clone_list)
    except FileNotFoundError:
        print('Plese enter valid file.')

if __name__ == '__main__':
    main()
