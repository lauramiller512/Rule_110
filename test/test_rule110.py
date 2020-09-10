import rule_110

class TestMakeBinary(TestCase):

    def test_add(self):
        result = rule_110.make_binary(3)
        self.assertEqual(result, 0)
