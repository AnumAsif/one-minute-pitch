import unittest
from app.models import Category,User,Pitch
from app import db

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.user_anum = User(username = 'anum',password='potato',email='anum@yahoo.com')
        self.category_tech = Category(name="Technology")
        self.new_pitch=Pitch(message="ad adad adadad",category_id=self.category_tech.id,user_id=self.user_anum.id)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Category.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.message,'ad adad adadad')
        self.assertEquals(self.new_pitch.user_id,self.user_anum.id)
        self.assertEquals(self.new_pitch.category_id,self.category_tech.id)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_category(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches(self.category_tech.id)
        self.assertTrue(len(got_pitches)==1)
