import unittest

def mathsPuzzle(lenDigit):
    rList=[]
    if lenDigit <=10:
        maxDigit=10**lenDigit
        for x in range(maxDigit):
            for y in list(str(x)):
                if list(str(x)).count(str(y))!=y:
                    break
                elif y==lenDigit-1:
                    rList.append(x)
    else:
        print('mathsPuzzle is unable to deal with anothing greater than base 10')
    return rList

class TestmathsPuzzle(unittest.TestCase):

    def test_mathsPuzzle(self):
        t1=longestValidParentheses(2)
        self.assertEqual(t1,[])

        t2=mathsPuzzle(10)
        self.assertEqual(t2,[].append[6210001000])

if __name__ == '__main__':
    unittest.main()
