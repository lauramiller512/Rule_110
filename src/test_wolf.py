import wolf
import unittest

class TestMakeBinary(unittest.TestCase):

    def setUp(self):
        self.states = [
            (1, 1, 1), 
            (1, 1, 0), 
            (1, 0, 1), 
            (1, 0, 0), 
            (0, 1, 1), 
            (0, 1, 0), 
            (0, 0, 1), 
            (0, 0, 0)
        ]
        self.cells = [0, 0, 0, 0, 0, 0, 1]
        self.rule = wolf.parse_rule(110)
        self.rule_map = dict(zip(self.states, self.rule))


    def test_parse_rule(self):
        self.assertEqual([0, 1, 1, 0, 1, 1, 1, 0], self.rule)

    def test_parse_rule_error(self):
        self.assertRaises(ValueError, wolf.parse_rule, "10101a")

    def test_make_states(self):
        self.assertEqual(wolf.make_states(), self.states)

    def test_make_map(self):
        rule = [0, 1, 1, 0, 1, 1, 1, 0]
        new_map = wolf.make_map(self.states, rule)
        self.assertEqual(new_map, self.rule_map)

    def test_compute(self):
        new_list = wolf.compute(self.cells, self.rule_map)
        self.assertEqual(new_list, [0, 0, 0, 0, 0, 1, 1])
