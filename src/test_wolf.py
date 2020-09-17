from wolf import parse_rule
from wolf import make_states
from wolf import make_map
from wolf import compute
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
        self.rule = parse_rule(110)
        self.rule_map = dict(zip(self.states, self.rule))


    def test_parse_rule(self):
        self.assertEqual([0, 1, 1, 0, 1, 1, 1, 0], self.rule)

    def test_parse_rule_error(self):
        self.assertRaises(ValueError, parse_rule, "10101a")

    def test_make_states(self):
        self.assertEqual(make_states(), self.states)

    def test_make_map(self):
        rule = [0, 1, 1, 0, 1, 1, 1, 0]
        new_map = make_map(self.states, rule)
        self.assertEqual(new_map, self.rule_map)

    def test_compute(self):
        new_list = compute(self.cells, self.rule_map)
        self.assertEqual(new_list, [0, 0, 0, 0, 0, 1, 1])
