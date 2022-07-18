import unittest
from translator import frenchToEnglish, englishToFrench


class TestTranslator(unittest.TestCase):

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish("None"), '')

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench("None"), '')

if __name__ == '__main__':
    unittest.main()
