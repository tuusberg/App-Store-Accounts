__author__ = "Matthew Tuusberg"

import os
import json
import glob
import biplist
from pprint import pprint

class Account(object):
    def __init__(self, **kwargs):
        if 'AppleID' not in kwargs:
            raise ValueError('AppleID key is missing')

        self.__dict__.update(kwargs)

    def __repr__(self):
        attibutes = [k for k in self.__dict__ if not k.startswith('_')]
        return os.linesep.join('{}: {}'.format(attr, self.__dict__[attr]) for attr in attibutes)

    def __hash__(self):
        return hash(self.AppleID)

    def __eq__(lh, rh):
        return isinstance(rh, lh.__class__) and lh.AppleID == rh.AppleID


def grab_plists():
    """
    Looks for iTunesMetadata files inside /var/mobile/Containers/Bundle/Application/ directory.
    :returns: list of filenames
    """
    return glob.glob('/var/mobile/Containers/Bundle/Application/*/iTunesMetadata.plist')


def read_plists(plists):
    """
    Reads plist files and looks for App Store credentials.
    :param plists: list of filenames
    :returns: list of credentials found
    """
    accounts = set()
    for f in plists:
        try:
            data = biplist.readPlist(f)
        except Exception as e:
            print '{} is not readable.\nReason: {}'.format(f, e)
            continue

        account_info = data.get('com.apple.iTunesStore.downloadInfo', {}).get('accountInfo')

        if not account_info:
            continue

        try:
            account = Account(**account_info)
        except ValueError as e:
            print e
            continue

        accounts.add(account)

    return list(accounts)


def main():
    plists = grab_plists()
    accounts = read_plists(plists)

    if not any(accounts):
        print 'Credentials were not found. Try to install an application from the App Store and relaunch this script.'
        return

    for account in accounts:
        print account
        print


if __name__ == '__main__':
    main()
