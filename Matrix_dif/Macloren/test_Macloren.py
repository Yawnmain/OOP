import Macloren as mac
import unittest


class tester(unittest.TestCase):
    def test_exp(self):
        n = 5
        x = 2
        ans = 7.266666666666667
        self.assertEqual(mac.exp(x, n), ans)

    def test_sin(self):
        n = 5
        x = 1.5
        ans = 0.9974949556821353
        self.assertEqual(mac.sin(x, n), ans)

    def test_cos(self):
        n = 5
        x = 5
        ans = -0.16274663800705724
        self.assertEqual(mac.cos(x, n), ans)

    def test_arcsin(self):
        n = 3
        x = 1
        ans = 1.286309523809524
        self.assertEqual(mac.arcsin(x, n), ans)

    def test_arccos(self):
        n = 2
        x = 1
        ans = 0.32912966012822986
        self.assertEqual(mac.arccos(x, n), ans)


if __name__ == '__main__':
    unittest.main()
