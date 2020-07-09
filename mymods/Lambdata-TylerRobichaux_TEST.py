#!/usr/bin/env python


import unittest
from my_mod import nospaces
from my_mod_two import capitalizationstandardized

# def nospaces(x):
#     # Removes trailing and leading spaces
#     return x.srt.strip()



class my_modTEST(unittest.TestCase):
    """A Test that checks if the my_mod method is working correctly"""
    def test_nospaces(self):
        x1 = '   P Sherman 42 Wallaby Way Sydney '
        y1 = nospaces(x1)
        self.assertEqual(y1, 'P Sherman 42 Wallaby Way Sydney')


class my_mod_twoTEST(unittest.TestCase):
  """
  A Test that checks if the my_mod_two method is working correctly
  """
  def test_capitalizationstandardized(self):
    x1 = 'cCecassacAEg ssAWSEFGc a3r4 as##f$'
    y1 = capitalizationstandardized(x1)
    self.assertEqual(y1, 'ccecassacaeg ssawsefgc a3r4 as##f$')

if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()