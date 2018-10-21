import os
import re
from os.path import expanduser
import urllib.request
from urllib.parse import urlparse


import argparse
import pdfkit
import urllib.request
from bs4 import BeautifulSoup


def directory_slash(destination):
    """ Ensure that the destination directory contains a final `/` """

    if destination[-1] != '/':
        return destination + '/'

    return destination


def directory_resolve_home(destination):
    """ Resolve home directory `~` """

    if destination[:1] == '~':
        home = expanduser("~")
        return home + destination.strip('~')

    return destination


def directory_exists(destination):
    """ Check if a directory exists """

    if not os.path.isdir(destination):
        raise RuntimeError('Directory %s does not exists' % (destination))

    return True


def read_page(url):
    """ Read page content and return the source code """

    return urllib.request.urlopen(url).read()


def get_page_title(page):
    """ Return an HTML title from a source code """

    html = BeautifulSoup(page, "html.parser")
    return html.title.string


def get_domain_name(url):
    """ Returns the domain name from a URL """

    parsed_uri = urlparse(url)
    return parsed_uri.netloc


def generate_filename(url, title):
    """ Generate a filename """

    # Replace all special characters with `-
    title = re.sub('[^a-z0-9 ]+', '', title.lower())
    title = '-'.join(title.split())

    return get_domain_name(url) + '-' + title + '.pdf'


def download_page(url, destination):
    """ Download a page with pdfkit """

    # Set and verify destination path
    destination = directory_resolve_home(directory_slash(destination))
    directory_exists(destination)

    # Set output name
    filename = generate_filename(url=url, title=get_page_title(read_page(url)))

    pdfkit.from_url(url, destination + filename)

    return destination + filename


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str,
                        help="URL to download", required=True)
    parser.add_argument("-o", "--out", type=str,
                        help="Destination directory", default='~/Downloads/')
    args = parser.parse_args()

    download_page(args.url, args.out)


if __name__ == '__main__':
    main()
