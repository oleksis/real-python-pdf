import os
import sys
import unittest

_path = os.path.realpath(os.path.abspath(__file__))
ROOT_PATH = os.path.dirname(os.path.dirname(_path))
sys.path.insert(0, ROOT_PATH)

from main import get_chunk, get_links


class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.content = """
# Table of Contents

<!-- toc starts -->

##	Basic
* [Python Strings](https://realpython.com/python-strings/ "Strings in Python")
##	Intermediate
* [Python Interface](https://realpython.com/python-interface/ )
##	Advanced
* [Python GIL](https://realpython.com/python-gil/  "GIL in Python")

<!-- toc ends -->

# Contributing
        """

    def test_get_chunk(self):
        expected = ("Python Strings", "Python Interface", "Python GIL")
        result = get_chunk("toc", self.content)
        self.assertTrue(all(_e in result for _e in expected))

    def test_get_links(self):
        expected = [
            {
                "text": "Python Strings",
                "url": "https://realpython.com/python-strings/",
                "title": "Strings in Python",
            },
            {
                "text": "Python Interface",
                "url": "https://realpython.com/python-interface/",
                "title": "",
            },
            {
                "text": "Python GIL",
                "url": "https://realpython.com/python-gil/",
                "title": "GIL in Python",
            },
        ]
        result = get_links(self.content)
        for idx, _e in enumerate(expected):
            self.assertDictEqual(result[idx], _e)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
