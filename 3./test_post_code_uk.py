
import unittest
from post_code_uk import PostCodeUk

class TestPostCodeUK(unittest.TestCase):

    def test_valid_postcode(self):
        try:
            PostCodeUk("PO16 7GZ")
        except ValueError:
            self.fail("PostCodeUk() raised ValueError unexpectedly!")

    def test_invalid_postcode(self):
        with self.assertRaises(ValueError):
            PostCodeUk("INVALID")

    def test_normalization(self):
        self.assertEqual(PostCodeUk("po16 7gz").code, "PO167GZ")

    def test_formatted(self):
        self.assertEqual(PostCodeUk("L18JQ").formatted(), "L1 8JQ")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            PostCodeUk("A1")
            
    def test_some_cases(self):
        post_coedes = ['SW1W 0NY', 'W1N 4DJ', 'L1 8JQ', 'TW89GS', 'EC1A1BB'
                , 'W1A0AX', 'm11ae', 'b338th', 'cr26xh', 'DN551PT']
        
        for code in post_coedes:
            try:
                PostCodeUk(code)
            except ValueError:
                self.fail("PostCodeUk() raised ValueError unexpectedly!")


if __name__ == '__main__':
    unittest.main()
