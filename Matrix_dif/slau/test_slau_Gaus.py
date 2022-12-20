import slau as s
import unittest


class tester(unittest.TestCase):

    def test_gaus_1(self):
        m = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
        keys = [15, -9, 5]
        ans = [-7.0, -2.0, 2.0]
        self.assertEqual(s.gaus_slau(m, keys), ans)

    def test_gaus_2(self):
        m = [[4, -2], [6, 1]]
        keys = [22, 45]
        ans = [7.0, 3.0]
        self.assertEqual(s.gaus_slau(m, keys), ans)

    def test_gaus_3(self):
        m = [[3, -2], [5, 4]]
        keys = [6, 32]
        ans = [4.0, 3.0]
        self.assertEqual(s.gaus_slau(m, keys), ans)


if __name__ == '__main__':
    unittest.main()
