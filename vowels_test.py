from unittest import TestCase
from vowels import count_vowels


class Test(TestCase):
    def test_count_vowels(self):
        self.assertTupleEqual(count_vowels('hellothere'), ('eo', 4))

    def test_input_is_string(self):
        with self.assertRaises(TypeError):
            count_vowels([1, 2, 3, 4])