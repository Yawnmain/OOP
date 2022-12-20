import unittest
import approx as app


class tester(unittest.TestCase):
    def test_MNK(self):
        xy = [[2, 4], [3, 9]]
        ans = 2.69
        self.assertEqual(round(app.MNK(xy)[0], 2), ans)

    def test_line_approx(self):
        xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [4]
        ans = [[4, 4.62]]
        self.assertEqual([[round(el[0], 2), round(el[1], 2)]
                         for el in app.line_approx(xy, x)], ans)

    def test_line_approx_2(self):
        xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [2, 3]
        ans = [[2, 2.65], [3, 3.63]]
        self.assertEqual([[round(el[0], 2), round(el[1], 2)]
                         for el in app.line_approx(xy, x)], ans)

    def test_approx_by_polynomial(self):
        koffs = [0.48, -4.8, 13.96, -7.64]
        x = [1, 3, 5]
        ans = [[1, 2.0], [3, 4.0], [5, 2.16]]
        self.assertEqual([[round(el[0], 2), round(el[1], 2)]
                         for el in app.approx_by_polynomial(koffs, x)], ans)


if __name__ == '__main__':
    unittest.main()
