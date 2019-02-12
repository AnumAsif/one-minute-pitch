import unittest
from app.models import Category

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_category = Category(name = 'tech')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))
