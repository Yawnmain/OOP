import interpolar as i
import unittest


class tester(unittest.TestCase):
    def test_for_single(self):
        mA = [[2, 5], [6, 9]]
        x = 4
        ans = [x, 7]
        self.assertEqual(i.single_inter(mA, x), ans)

    def test_for_part_inter(self):
        mA = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [-1.5, 3, 2, 5, 9]
        ans = [[-1.5, -0.5], [3, 4.0], [3, 4.0], [2, 3.0],
               [5, 5.399999999999999], [9, 11.799999999999999]]
        self.assertEqual(i.part_inter(mA, x), ans)

    def test_Lagrange(self):
        xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = 4
        ans = [x, 2.12]
        self.assertEqual(i.Lagrange(xy, x), ans)


if __name__ == '__main__':
    unittest.main()
