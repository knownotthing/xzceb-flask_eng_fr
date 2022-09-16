import unittest
from translator import english_to_french
from translator import french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("Dog"),"Chat")
        self.assertEqual(english_to_french("Hello"),"Bonjour")

class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("Chat"),"Dog")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()