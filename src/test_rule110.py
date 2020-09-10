import rule_110
import unittest

class TestMakeBinary(unittest.TestCase):

    #passes
    def test_binary(self):
        result = rule_110.make_binary([3])
        self.assertEqual(result, [0])

        result = rule_110.make_binary(["t"])
        self.assertEqual(result, [0])

    def test_generate(self):
        result = rule_110.generate([0,0,0,0,1,0])
        self.assertEqual(result, ". . . O ")

    #passes
    def test_compute(self):
        result = rule_110.compute([0,0,0,0,0,1,0])
        self.assertEqual(result, [0,0,0,0,1,1,0])


if __name__ == '__main__':
    unittest.main()