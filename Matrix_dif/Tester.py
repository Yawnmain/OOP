import MYmatrix as m
import unittest


class tester(unittest.TestCase):

    def test_add(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scalar = 3
        ans = [[4, 5], [6, 7], [8, 9]]
        self.assertEqual(m.add(a, scalar), ans)

    def test_add_mat(self):
        a = [[1, 2], [3, 4], [5, 6]]
        b = [[6, 5], [4, 3], [2, 1]]
        ans = [[7, 7], [7, 7], [7, 7]]
        self.assertEqual(m.add(a, b), ans)

    def test_mul(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scalar = 3
        ans = [[3, 6], [9, 12], [15, 18]]
        self.assertEqual(m.mul(a, scalar), ans)

    def test_mul_mat(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scalar = [[4, 2, 12], [5, 8, 1]]
        ans = [[14, 18], [32, 38], [50, 58]]
        self.assertEqual(m.mul(a, scalar), ans)

    def test_div(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scalar = 1/2
        ans = [[0.5, 1.0], [1.5, 2.0], [2.5, 3.0]]
        self.assertEqual(m.mul(a, scalar), ans)

    def test_sub(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scalar = 2
        ans = [[-1, 0], [1, 2], [3, 4]]
        self.assertEqual(m.sub(a, scalar), ans)

    def test_sub_mat(self):
        a = [[1, 2], [3, 4], [5, 6]]
        b = [[2, 3], [4, 5], [6, 7]]
        ans = [[-1, -1], [-1, -1], [-1, -1]]
        self.assertEqual(m.sub(a, b), ans)

    def test_add_rows(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scalar = 2
        row1 = 0
        row2 = 1
        ans = [[7, 10], [3, 4], [5, 6]]
        self.assertEqual(m.add_rows(a, row1, row2, scalar), ans)

    def test_add_rows(self):
        a = [[1, 2], [3, 4], [5, 6]]
        default = [[1, 2], [3, 4], [5, 6]]
        scalar = 2
        row1 = 0
        row2 = 1
        ans = [[7, 10], [3, 4], [5, 6]]
        self.assertEqual(m.add_rows(a, row1, row2, scalar), ans)
        self.assertEqual(a, default)

    def test_mul_rows(self):
        a = [[1, 2], [3, 4], [5, 6]]
        default = [[1, 2], [3, 4], [5, 6]]
        scalar = 2
        id = 0
        ans = [[2, 4], [3, 4], [5, 6]]
        self.assertEqual(m.mul_row(a, id, scalar), ans)
        self.assertEqual(a, default)

    def test_change_rows(self):
        a = [[1, 2], [3, 4], [5, 6]]
        default = [[1, 2], [3, 4], [5, 6]]
        row1 = 0
        row2 = 1
        ans = [[3, 4], [1, 2], [5, 6]]
        self.assertEqual(m.change_rows(a, row1, row2, True), ans)
        self.assertEqual(a, default)
        m.change_rows(a, row1, row2)
        self.assertEqual(a, ans)


if __name__ == '__main__':
    unittest.main()
