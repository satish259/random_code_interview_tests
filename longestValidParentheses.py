import unittest

def longestValidParentheses(s):
    l=list(s)
    count=min(l.count('('),l.count(')'))
    return (count * 2)

class TestlongestValidParentheses(unittest.TestCase):

    def test_longestValidParentheses(self):
        t1=longestValidParentheses("(()")
        self.assertEqual(t1,2)

        t2=longestValidParentheses(")()())")
        self.assertEqual(t2,4)

if __name__ == '__main__':
    unittest.main()