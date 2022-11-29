import slau as sl
import unittest


class tester(unittest.TestCase):

    def test_reverse_slau_1(self):
        m = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
        keys = [15, -9, 5]
        ans = [-7.0, -2.0, 2.0]
        self.assertEqual(sl.reverse_slau(m, keys), ans)

    def test_reverse_slau_2(self):
        m = [[4, -2], [6, 1]]
        keys = [22, 45]
        ans = [7.0, 3.0]
        self.assertEqual(sl.reverse_slau(m, keys), ans)

    def test_reverse_slau_3(self):
        m = [[1, 2], [3, 4]]
        keys = [6, 8]
        ans = [-4.0, 5.0]
        self.assertEqual(sl.reverse_slau(m, keys), ans)


if __name__ == '__main__':
    unittest.main()
