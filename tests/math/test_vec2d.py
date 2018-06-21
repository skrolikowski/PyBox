import unittest
from pybox.math.vec2d import Vec2d


class Vector2Test(unittest.TestCase):
    def setUp(self):
        self.v1 = Vec2d(1, 2)
        self.v2 = Vec2d(3, 4)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertTrue(self.v1.x == 1 and self.v1.y == 2)
        self.assertTrue(self.v2.x == 3 and self.v2.y == 4)

    def test_copy(self):
        v3 = self.v1.copy()
        v4 = self.v2

        self.assertTrue(self.v1 == v3)
        self.assertTrue(self.v2 == v4)

    def test_scale(self):
        self.v1.scale(2)
        self.v2.scale(0.5)

        self.assertTrue(self.v1.x == 2 and self.v1.y == 4)
        self.assertTrue(self.v2.x == 1.5 and self.v2.y == 2)

    def test_length(self):
        self.assertAlmostEqual(self.v1.length(), 2.236, places=3)
        self.assertAlmostEqual(self.v2.length(), 5)

    def test_lengthSq(self):
        self.assertEqual(self.v1.lengthSq(), 5)
        self.assertEqual(self.v2.lengthSq(), 25)

    def test_distance(self):
        self.assertAlmostEqual(self.v1.distance(self.v2), 2.828, places=3)

    def test_lerp(self):
        self.assertEqual(self.v1.lerp(self.v2, 0.25), Vec2d(1.5, 2.5))
        self.assertEqual(self.v1.lerp(self.v2, 0.5), Vec2d(2, 3))
        self.assertEqual(self.v1.lerp(self.v2, 0.75), Vec2d(2.5, 3.5))

    def test_lerpException(self):
        with self.assertRaises(Exception) as context:
            self.v1.lerp(self.v2, 2)

            self.assertTrue('Second argument must be a float value between 0 and 1.0.' in context.exception)

    def test_normalize(self):
        v3 = Vec2d(0, 0)

        self.assertAlmostEqual(self.v1.normalize(), Vec2d(0.447, 0.894), places=3)
        self.assertAlmostEqual(self.v2.normalize(), Vec2d(0.6, 0.8))
        self.assertEqual(v3.normalize(), Vec2d(0, 0))

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2), 11)

    def test_cross(self):
        self.assertEqual(self.v1.cross(self.v2), -2)

    def test_add(self):
        v3 = self.v1 + self.v2

        self.assertTrue(self.v1.x == 1 and self.v1.y == 2)
        self.assertTrue(self.v2.x == 3 and self.v2.y == 4)
        self.assertTrue(v3.x == 4 and v3.y == 6)

    def test_sub(self):
        v3 = self.v2 - self.v1

        self.assertTrue(self.v1.x == 1 and self.v1.y == 2)
        self.assertTrue(self.v2.x == 3 and self.v2.y == 4)
        self.assertTrue(v3.x == 2 and v3.y == 2)

    def test_mul(self):
        v3 = self.v1 * self.v2

        self.assertTrue(self.v1.x == 1 and self.v1.y == 2)
        self.assertTrue(self.v2.x == 3 and self.v2.y == 4)
        self.assertTrue(v3.x == 3 and v3.y == 8)

    def test_div(self):
        v3 = self.v2 / self.v1

        self.assertTrue(self.v1.x == 1 and self.v1.y == 2)
        self.assertTrue(self.v2.x == 3 and self.v2.y == 4)
        self.assertTrue(v3.x == 3 and v3.y == 2)

    def test_divException(self):
        v1 = Vec2d(2, 4)
        v2 = Vec2d(0, 0)

        with self.assertRaises(ZeroDivisionError) as context:
            v3 = v1 / v2

            self.assertTrue('Right-hand side Vec2d contains a 0. Cannot divide by 0.' in context.exception)

    def test_lt(self):
        self.assertTrue(self.v1 < self.v2)

    def test_gt(self):
        self.assertFalse(self.v1 > self.v2)

    def test_eq(self):
        self.assertFalse(self.v1 == self.v2)
        self.assertTrue(self.v1 == Vec2d(1, 2))

    def test_ne(self):
        self.assertTrue(self.v1 != self.v2)
        self.assertFalse(self.v1 != Vec2d(1, 2))


if __name__ == '__main__':
    unittest.main()
