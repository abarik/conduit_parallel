import random
import string
import pandas as pd
import os


class TestData:
    """Base URL - Conduit homepage from docker image"""
    # BASE_URL = 'http://localhost:1667/'
    BASE_URL = 'https://psycho.unideb.hu/'


    """Data file for test data"""
    FILE_ARTICLE_DATA = 'article_test_data.txt'  # by https://www.mockaroo.com/

    """Data file names for output"""
    OUT_FILE_POPULAR_TAGS = 'out_popular_tags.csv'
    OUT_FILE_ARTICLE_LINKS = 'out_article_links.csv'

    """Test data variables from data files"""
    ARTICLE_TEST_DATA = None

    """Number of new Articles to insert"""
    ARTICLE_TEST_DATA_MAX_NUM = 20

    """Test data for user settings"""
    SETTINGS_SHORT_BIO = "Árvíztűrő ütvefúrógép. A Microsoft cég alapítójaként és tulajdonosaként Bill Gates fontos szerepet játszott a 20. század végén felvirágzó mikroszámítógép-ipar történetében, olyan széles körben elterjedt szoftverek fűződnek a nevéhez, mint az MS-DOS vagy a Microsoft Windows."

    class User:
        def __init__(self, user_name, user_email, password):
            self.user_name = user_name
            self.user_email = user_email
            self.password = password

    def __init__(self):
        TestData.ARTICLE_TEST_DATA = pd.read_csv(os.path.realpath('test_conduit/config/' + TestData.FILE_ARTICLE_DATA),
                                                 delimiter='\t')

        """General User for all tests (except registrations testcase)"""
        name = TestData.random_username(8)
        self.GEN_USER = self.User(name, name + '@' + TestData.random_domain(), 'Userpass1')

        """User for registration testcase"""
        name = TestData.random_username(8)
        self.REG_USER = self.User(name, name + '@' + TestData.random_domain(), 'Userpass1')

        """Unique articles for a testcase"""
        self.UNIQUE_ARTICLE = {
            'title': TestData.random_username(12),
            'about': TestData.random_username(15),
            'body': TestData.random_username(30),
            'tag': TestData.random_username(15)
        }

        self.UNIQUE_ARTICLE_WITH_COMMENTS = {
            'title': TestData.random_username(12),
            'about': TestData.random_username(15),
            'body': TestData.random_username(30),
            'tag': TestData.random_username(15),
            'comments': ['Good post.', 'Thanks.', 'Átvíztűrő ütvefúrógép.']
        }


    @staticmethod
    def random_username(y):
        if y > 4:
            return ''.join(random.choice(string.ascii_letters) for x in range(y - 3)) + ''.join(
                random.choice(string.digits) for x in range(3))
        else:
            return ''.join(random.choice(string.ascii_letters) for x in range(y))

    @staticmethod
    def random_domain():
        domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
        return domains[random.randint(0, len(domains) - 1)]
