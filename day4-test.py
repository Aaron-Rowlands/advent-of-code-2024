import unittest
import day4 as subject

class testDay4(unittest.TestCase):
    def test_count_XMAS_forward(self):
        self.assertEqual(3, subject.count_XMAS_line("XMASXMASXMASSSS"))

    def test_count_XMAS_backward(self):
        self.assertEqual(2, subject.count_XMAS_line("SSSAMX SAMXXX"))

    def test_block(self):
        strings = [
            "MMMSXXMASM",
            "MSAMXMMMSA",
            "AMXSXMAAMM",
            "MSAMASMSSX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
        self.assertEqual(18, subject.count_XMAS_block(strings))

    def test_X_MAS_detection(self):
        simpleBlock = [
            "M.S",
            ".A.",
            "M.S",
        ]
        self.assertEqual(1, subject.X_MAS_detection(simpleBlock))

        complexBlock = [
            ".M.S......",
            "..A..MSMS.",
            ".M.S.MAA..",
            "..A.ASMSM.",
            ".M.S.M....",
            "..........",
            "S.S.S.S.S.",
            ".A.A.A.A..",
            "M.M.M.M.M.",
            "..........",
        ]
        self.assertEqual(9, subject.X_MAS_detection(complexBlock))
