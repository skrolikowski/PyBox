import unittest
from pybox.containers.pqueue import PQueue


class PQueueTest(unittest.TestCase):
    def setUp(self):
        self.q1 = PQueue()
        self.q2 = PQueue([('baz', 3), ('foo', 1)])

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(len(self.q1), 0)
        self.assertEqual(len(self.q2), 2)

    def test_clear(self):
        self.q1.clear()
        self.q2.clear()

        self.assertEqual(len(self.q1), 0)
        self.assertEqual(len(self.q2), 0)

    def test_enqueue(self):
        self.q1.enqueue(('bar', 2))
        self.q2.enqueue(('bar', 2))

        self.assertEqual(len(self.q1), 1)
        self.assertEqual(len(self.q2), 3)

    def test_enqueueException(self):
        with self.assertRaises(Exception) as context:
            q3 = PQueue([('bar', 2), 'foo'])

            self.assertTrue('Element must be tuple, you entered: foo' in context.exception)

    def test_dequeue(self):
        q1Value = self.q1.dequeue()
        q2Value = self.q2.dequeue()

        self.assertEqual(q1Value, None)
        self.assertEqual(q2Value, ('foo', 1))

    def test_enqueue_dequeue(self):
        q3 = PQueue()
        q3.enqueue(('bar', 2))
        q3.enqueue(('baz', 3))
        q3.enqueue(('foo', 1))

        q3Value = q3.dequeue()

        self.assertEqual(q3Value, ('foo', 1))
        self.assertEqual(len(q3), 2)

    def test_peek(self):
        self.assertEqual(self.q1.peek(), None)
        self.assertEqual(self.q2.peek(), ('foo', 1))

    def test_isEmpty(self):
        self.assertTrue(self.q1.isEmpty())
        self.assertFalse(self.q2.isEmpty())


if __name__ == '__main__':
    unittest.main()
