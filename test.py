import os
import yaml
import unittest

data = yaml.safe_load(open('environments/local.yml'))

for key in data:
    os.environ[key] = data[key]

from handler import get_easy_word, get_medium_word, get_hard_word


class TestHandler(unittest.TestCase):
		  
     def test_easy_word(self):
         print(get_easy_word({},None))
         medium_word = get_medium_word({},None)
         hard_word = get_hard_word({},None)

if __name__ == '__main__':
    unittest.main()