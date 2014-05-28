import unittest, roman3

class KnownValues(unittest.TestCase):
    known_values = (    (1, 'I'),
                        (2, 'II'),
                        (3, 'III'),
                        (4, 'IV'),
                        (5, 'V'),
                        (6, 'VI'),
                        (7, 'VII'),
                        (8, 'VIII'),
                        (9, 'IX'),
                        (10, 'X'),
                        (50, 'L'),
                        (100, 'C'),
                        (500, 'D'),
                        (1000, 'M'),
                        (31, 'XXXI'),
                        (148, 'CXLVIII'),
                        (294, 'CCXCIV'),
                        (312, 'CCCXII'),
                        (421, 'CDXXI'),
                        (528, 'DXXVIII'),
                        (621, 'DCXXI'),
                        (782, 'DCCLXXXII'),
                        (3888, 'MMMDCCCLXXXVIII'),
                        (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman3.to_roman(integer)
            self.assertEqual(numeral, result)

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, 4000)
    
    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, 0)
    
    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman3.OutOfRangeError, roman3.to_roman, -1)

if __name__ == '__main__':
    unittest.main()
