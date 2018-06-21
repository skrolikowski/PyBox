import unittest
from pybox.math import util


class MathUtilTest(unittest.TestCase):
    def test_dot(self):
        l1 = [1, 2, 3]
        l2 = [3, 4, 6]

        self.assertEqual(util.dot(l1, l2), 29)


if __name__ == '__main__':
    unittest.main()
