from django.test import TestCase
from ..models import Course,Request,Offer

class ModelTest(TestCase):
    def testCourseModel(self):
        course = Course.objects.create(name="AdvanceProgramming")
        self.assertEquals(str(course), 'AdvanceProgramming')
        print("IsInstance : ",isinstance(course,Course))
        self.assertTrue(isinstance(course,Course))