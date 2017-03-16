# coding: utf-8
# Import test libraries
import unittest
import palindrome


# Build test class
class TestPalindrome(unittest.TestCase):
    """Example unittest test methods for is_palindrome."""

    def test_palindrome_example_1(self):
        """Test is_palindrome for empty case."""

        actual = palindrome.is_palindrome('')
        expected = True
        self.assertEqual(expected, actual)

    def test_palindrome_example_2(self):
        """Test is_palindrome for single case."""

        actual = palindrome.is_palindrome('a')
        expected = True
        self.assertEqual(expected, actual)
    
    def test_palindrome_example_3(self):
        """Test is_palindrome for small even true."""

        actual = palindrome.is_palindrome('aa')
        expected = True
        self.assertEqual(expected, actual)
        
    def test_palindrome_example_4(self):
        """Test is_palindrome for small even false."""

        actual = palindrome.is_palindrome('ab')
        expected = False
        self.assertEqual(expected, actual)
        
    def test_palindrome_example_5(self):
        """Test is_palindrome for small odd true."""

        actual = palindrome.is_palindrome('aba')
        expected = True
        self.assertEqual(expected, actual)
        
    def test_palindrome_example_6(self):
        """Test is_palindrome for small odd false."""

        actual = palindrome.is_palindrome('abc')
        expected = False
        self.assertEqual(expected, actual)
        
    def test_palindrome_example_7(self):
        """Test is_palindrome for long even true."""

        actual = palindrome.is_palindrome('abccba')
        expected = True
        self.assertEqual(expected, actual)
        
    def test_palindrome_example_8(self):
        """Test is_palindrome for long even false."""

        actual = palindrome.is_palindrome('abcdef')
        expected = False
        self.assertEqual(expected, actual)
        
    def test_palindrome_example_9(self):
        """Test is_palindrome for long odd true."""

        actual = palindrome.is_palindrome('abcdcba')
        expected = True
        self.assertEqual(expected, actual)
        
    def test_palindrome_example_10(self):
        """Test is_palindrome for long odd false."""

        actual = palindrome.is_palindrome('abcdefg')
        expected = False
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
