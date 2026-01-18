import unittest
import tempfile
import src.day5 as subject

class testOrderingRule(unittest.TestCase):
    def test_check(self):
        rule = subject.OrderingRule(1, 2)

        self.assertTrue(rule.check([1, 2, 3]))
        self.assertTrue(rule.check([]))
        self.assertTrue(rule.check([3]))

        self.assertFalse(rule.check([2, 1, 3]))

    def test_fix(self):
        rule = subject.OrderingRule(1, 2)
        sequences = [
            [2, 1, 3],
            [3],
            [1, 1, 2],
        ]
        for sequence in sequences:
            rule.fix(sequence)

        self.assertEqual(sequences[0], [1, 2, 3])
        self.assertEqual(sequences[1], [3])
        self.assertEqual(sequences[2], [1, 1, 2])

class testMainUtilities(unittest.TestCase):
    def setUp(self):
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp_input_file:
            tmp_input_file.write("1|2\n")
            tmp_input_file.write("3|4\n")
            tmp_input_file.write("5|6\n")
            tmp_input_file.write("1,3,5\n")
            tmp_input_file.write("2,4,6\n")
            tmp_input_file.flush()
        self.tmp_input_file = tmp_input_file

        return super().setUp()

    def test_read_rules(self):
        rules = subject.read_rules(self.tmp_input_file.name)

        self.assertEqual(len(rules), 3)

    def test_read_sequences(self):
        sequences = subject.read_sequences(self.tmp_input_file.name)

        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0], [1, 3, 5])
        self.assertEqual(sequences[1], [2, 4, 6])
