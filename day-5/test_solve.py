import unittest
import solve

class TestSolve(unittest.TestCase):

    # @unittest.skip("Not implemented")
    def test_decode_seat_70_7(self):
        input = "BFFFBBFRRR"
        expected = (70, 7)
        actual = solve.decode_seat(input)
        self.assertEqual(expected, actual)

    # @unittest.skip("Not implemented")
    def test_decode_seat_14_7(self):
        input = "FFFBBBFRRR"
        expected = (14, 7)
        actual = solve.decode_seat(input)
        self.assertEqual(expected, actual)

    # @unittest.skip("Not implemented")
    def test_decode_seat_102_4(self):
        input = "BBFFBBFRLL"
        expected = (102, 4)
        actual = solve.decode_seat(input)
        self.assertEqual(expected, actual)

    def test_decode_row_f(self):
        input = "F"
        expected = 0
        actual = solve.decode_row(input, (0, 127))
        self.assertEqual(expected, actual)

    def test_decode_row_b(self):
        input = "B"
        expected = 63
        actual = solve.decode_row(input, (0, 63))
        self.assertEqual(expected, actual)

    def test_decode_row_bb(self):
        input = "BB"
        expected = 47
        actual = solve.decode_row(input, (32, 47))
        self.assertEqual(expected, actual)

    def test_decode_row_ff(self):
        input = "FF"
        expected = 32
        actual = solve.decode_row(input, (32, 47))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()