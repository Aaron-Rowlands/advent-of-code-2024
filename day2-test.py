import unittest
import day2 as subject

class testDay2(unittest.TestCase):
    def test_unsafe_report(self):
        report = [9, 10, 18]
        self.assertFalse(subject.isSafe(report))

    def test_safe_report(self):
        report = [10, 7, 4, 2, 1]
        self.assertTrue(subject.isSafe(report))
