import unittest
import roman10 as roman

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
                        (3999, 'MMMCMXCIX'),
                        (4000, 'MMMM'),
                        (4500, 'MMMMD'),
                        (4888, 'MMMMDCCCLXXXVIII'),
                        (4999, 'MMMMCMXCIX'))

    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman.to_roman(integer)
            self.assertEqual(numeral, result)
            
    def test_from_roman_known_values(self):
        '''from_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 5000)
    
    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)
    
    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, -1)
    
    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(roman.NotIntegerError, roman.to_roman, 0.5)

class RoundTripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''from_roman(to_roman(n)) == n for all n'''
        for integer in range(1, 5000):
            numeral = roman.to_roman(integer)
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

class FromRomanBadInput(unittest.TestCase):
    def test_too_many_repeated_numerals(self):
        '''from_roman should fail with too many repeated numerals'''
        for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)
    
    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numerals'''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)
    
    def test_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)
    
    def test_blank(self):
        '''from_roman should fail with blank string'''
        self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, '')
    
    def test_non_string(self):
        '''from_roman should fail with non-string input'''
        self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, 1)

if __name__ == '__main__':
    unittest.main()
