import unittest
from pybox.containers.queue import Queue


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.q1 = Queue()
        self.q2 = Queue([1, 2, 3, 4, 5])

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(len(self.q1), 0)
        self.assertEqual(len(self.q2), 5)

    def test_clear(self):
        self.q1.clear()
        self.q2.clear()

        self.assertEqual(len(self.q1), 0)
        self.assertEqual(len(self.q2), 0)

    def test_enqueue(self):
        self.q1.enqueue(10)
        self.q2.enqueue(10)

        self.assertEqual(len(self.q1), 1)
        self.assertEqual(len(self.q2), 6)

    def test_dequeue(self):
        q1Value = self.q1.dequeue()
        q2Value = self.q2.dequeue()

        self.assertEqual(q1Value, None)
        self.assertEqual(q2Value, 1)

    def test_enqueue_dequeue(self):
        self.q1.enqueue(1)
        self.q1.enqueue(2)
        self.q1.enqueue(3)

        q1Value = self.q1.dequeue()

        self.assertEqual(q1Value, 1)
        self.assertEqual(len(self.q1), 2)

    def test_peek(self):
        self.assertEqual(self.q1.peek(), None)
        self.assertEqual(self.q2.peek(), 1)

    def test_isEmpty(self):
        self.assertTrue(self.q1.isEmpty())
        self.assertFalse(self.q2.isEmpty())


if __name__ == '__main__':
    unittest.main()
