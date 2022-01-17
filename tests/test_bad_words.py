import unittest
from bad_words_plus import BadWordsPlus


class TestBadWords(unittest.TestCase):
    def test_add_words_fuck(self):
        self.assertEqual(BadWordsPlus().add_bad_word(
            "fuck"), ["fuck"], "Should be F*ck")

        self.assertEqual(BadWordsPlus().add_bad_word(
            "amk"), ["fuck", "amk"], "Should be F*ck and Amk")

    def test_check_from_list(self):
        self.assertEqual(BadWordsPlus().check_from_list(
            ["hello", "hello world", "fuck you", "fucking", "testing"]), ['hello', 'hello world', 'testing'], "Should be hello, hello world, testing")


if __name__ == '__main__':
    unittest.main()
