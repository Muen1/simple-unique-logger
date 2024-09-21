import unittest
from unique_int import UniqueInt

class TestUniqueInt(unittest.TestCase):
    def test_process_file(self):
        unique_int = UniqueInt()
        unique_int.process_file('sample_input_01.txt', 'sample_output_01.txt')
        with open('sample_output_01.txt', 'r') as file:
            result = file.read().strip().split('\n')
        expected = ['-9', '-1', '5', '14', '62']
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

