"""Testing"""
import unittest
import translator

class Testing(unittest.TestCase):
    """Tests for the translator Module"""
    def test_e2f(self):
        """Test english2french translation"""
        word = "Bonjour"
        self.assertEqual(word, translator.englishToFrench("Hello"))

    def test_e2fnull(self):
        """test None"""
        word = "Bonjour"
        self.assertIsNotNone(word)

    def test_f2e(self):
        """Test french2english translation"""
        word = "Hello"
        self.assertEqual(word, translator.frenchToEnglish("Bonjour"))

    def test_f2enull(self):
        """test None"""
        word = "Hello"
        self.assertIsNotNone(word)

if __name__ == '__main__':
    unittest.main()
