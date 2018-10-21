import unittest
from os.path import expanduser

from .. import laterz


class Test(unittest.TestCase):

    def test_directory_slash(self):
        assert laterz.directory_slash('foo/bar') == 'foo/bar/'
        assert laterz.directory_slash('foo/bar/') == 'foo/bar/'

    def test_directory_resolve_home(self):
        assert laterz.directory_resolve_home('foo/bar') == 'foo/bar'
        assert laterz.directory_resolve_home(
            '~/foo/bar') == expanduser("~") + '/foo/bar'

    def test_directory_exists(self):
        assert laterz.directory_exists('/tmp/')

    def test_directory_exists_2(self):
        self.assertRaises(
            RuntimeError, laterz.directory_exists, '/non/existent/')

    def test_read_page(self):
        page = laterz.read_page('https://in.mail.yahoo.com')
        self.assertIsInstance(page, bytes)
        assert b'yahoo.com' in page

    def test_get_page_title(self):
        page = laterz.read_page('https://in.mail.yahoo.com')
        self.assertIsInstance(laterz.get_page_title(page), str)

    def test_get_domain_name(self):
        assert laterz.get_domain_name(
            'https://www.gab.lc/articles/') == 'www.gab.lc'

    def test_generate_filename(self):
        assert laterz.generate_filename(
            url='https://www.gab.lc/articles/', title='Some title') == 'www.gab.lc-some-title.pdf'

    def test_download_page(self):
        assert laterz.download_page(
            url='https://www.gab.lc/articles/weighted_ntile/', destination='/tmp') == '/tmp/www.gab.lc-weighted-ntile-with-postgresql-gablc.pdf'
