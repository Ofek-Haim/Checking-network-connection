# -*- coding: utf-8 -*-
import urllib2


def checking_network_connection():
    """
    This function check if the user
    connect to the internet.
    using urllib2
    If the user connect to the internet this function
    return True, else return False.
    """
    try:
        urllib2.urlopen('http://213.57.23.50', timeout=1)
        return True
    except urllib2.URLError as err:
        return False


if __name__ == '__main__':
    print checking_network_connection()