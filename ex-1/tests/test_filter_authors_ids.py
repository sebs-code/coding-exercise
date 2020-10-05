
import unittest

import filter_authors_ids


class TestFilterAuthorsIds(unittest.TestCase):
    """
    test cases to consider: 
        different author values
        author/id Value that are known NOT in the ORM
    """
    
    def setUp(self) -> None:
        # set up the django ORM? 
        pass

    def tearDown(self) -> None:
        # tear down the django ORM? 
        pass

    def test_filter_authors_ids(self):
        filter_authors_ids.test_filter_authors_ids()
        self.fail()


if __name__ == '__main__':
    unittest.main()
