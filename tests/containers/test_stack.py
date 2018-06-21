import unittest
from pybox.containers.stack import Stack

class StackTest(unittest.TestCase):
    def setUp(self):
        self.s1 = Stack()
        self.s2 = Stack([1, 2, 3, 4, 5])

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(len(self.s1), 0)
        self.assertEqual(len(self.s2), 5)

    def test_clear(self):
        self.s2.clear()

        self.assertEqual(len(self.s2), 0)

    def test_push(self):
        self.s1.push(1)
        self.s1.push(2)
        self.s1.push(3)

        self.assertEqual(len(self.s1), 3)
        self.assertEqual(self.s1.peek(), 3)

    def test_pop(self):
        s1Value = self.s1.pop()

        self.assertEqual(s1Value, None)

        s2Value = self.s2.pop()

        self.assertEqual(s2Value, 5)
        self.assertEqual(len(self.s2), 4)
        self.assertEqual(self.s2.peek(), 4)

    def test_push_pop(self):
        self.s1.push(1)
        self.s1.push(2)
        self.s1.push(3)

        s1Value = self.s1.pop()

        self.assertEqual(s1Value, 3)
        self.assertEqual(len(self.s1), 2)

    def test_peek(self):
        self.assertEqual(self.s1.peek(), None)
        self.assertEqual(self.s2.peek(), 5)

    def test_isEmpty(self):
        self.assertTrue(self.s1.isEmpty())
        self.assertFalse(self.s2.isEmpty())


if __name__ == '__main__':
    unittest.main()