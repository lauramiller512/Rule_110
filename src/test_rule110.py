import rule_110
import unittest

class TestMakeBinary(unittest.TestCase):

    #passes
    def test_compute(self):
        result = rule_110.compute([0,0,0,0,0,1,0])
        self.assertEqual(result, [0,0,0,0,1,1,0])

    #passes
    def test_binary(self):
        result = rule_110.make_binary([3])
        self.assertEqual(result, [0])

        result = rule_110.make_binary(["t"])
        self.assertEqual(result, [0])

    #passes
    def test_generate(self):
        result = rule_110.generate([0,0,0,0,1,0])
        self.assertEqual(result, ". . . O ")

    
    def test_validate(self):
        result = rule_110.validate([3])
        self.assertEqual(result, "This is not valid")

        result = rule_110.validate([0])
        self.assertEqual(result, "Valid")


if __name__ == '__main__':
    unittest.main()