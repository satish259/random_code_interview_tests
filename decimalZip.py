'''
Problem:
Given two numbers a and b, definition of decimal zip is as explained below:
• the first (i.e. the most significant) digit of C is the first digit of a;
• the second digit of C is the first digit of b;
• the third digit of C is the second digit of a;
• the fourth digit of C is the second digit of b;
•  and so on.... and return the zipped number
If A or B runs ount of digits, an optionally defined fill digit to be used.
'''

def decimalZip(A,B,fillDigit=''):
    from itertools import zip_longest
    from itertools import chain
    return int("".join(chain.from_iterable(zip_longest(str(A),str(B), fillvalue=fillDigit))))

import unittest

class TestCase(unittest.TestCase):
    def test_decimalZip_no_fill(self):
        self.assertEquals(decimalZip(12,59),1529)

    def test_decimalZip_with_fill(self):
        self.assertEqual(decimalZip(1094,12,'0'),11029040)

if __name__ == '__main__':
    unittest.main()