import unittest
from pybox.math.matrix import Matrix


class Vector2Test(unittest.TestCase):
    def test_new(self):
        mat = Matrix()

        self.assertListEqual(mat.matrix[0], [1, 0, 0])
        self.assertListEqual(mat.matrix[1], [0, 1, 0])
        self.assertListEqual(mat.matrix[2], [0, 0, 1])

    def test_identity(self):
        mat = Matrix.identity()

        self.assertListEqual(mat[0], [1, 0, 0])
        self.assertListEqual(mat[1], [0, 1, 0])
        self.assertListEqual(mat[2], [0, 0, 1])

if __name__ == '__main__':
    unittest.main()