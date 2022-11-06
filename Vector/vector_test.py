import class_vector as v
import unittest


class tester(unittest.TestCase):

    def test_add(self):
        a = [1, 2, 3, 4]
        answer = [2, 3, 4, 5]
        self.assertEqual(v.add(a, 1), answer)

    def test_sub(self):
        a = [1, 2, 3, 4]
        answer = [0, 1, 2, 3]
        self.assertEqual(v.sub(a, 1), answer)

    def test_mul(self):
        a = [1, 2, 3, 4]
        answer = [2, 4, 6, 8]
        self.assertEqual(v.mul(a, 2), answer)

    def test_div(self):
        a = [1, 2, 3, 4]
        answer = [0.5, 1, 1.5, 2]
        self.assertEqual(v.div(a, 2), answer)

    def test_cos(self):
        a = [1, 0, 0]
        b = [0, 1, 1]
        self.assertEqual(v.Cos(a, b), 0)

    def test_scalar(self):
        a = [5, -4]
        b = [2, 1]
        self.assertEqual(v.scalar_mlt(a, b), 6)


if __name__ == '__main__':
    unittest.main()
