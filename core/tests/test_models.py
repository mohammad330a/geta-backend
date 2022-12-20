from django.test import TestCase
from ..models import Course,Request,Offer
from accounts.models import User
from datetime import datetime


class ModelTest(TestCase):
    def testCourseModel(self):
        course = Course.objects.create(name="AdvanceProgramming")
        self.assertEquals(str(course), 'AdvanceProgramming')
        print("IsInstance : ",isinstance(course,Course))
        self.assertTrue(isinstance(course,Course))
    
    def testRequestModel(self):
        course = Course.objects.create(name="AdvanceProgramming")
        user = User.objects.create()
        request = Request.objects.create(student= user, course= course, email="saleh@gmail.com", created= datetime.now())
        self.assertEquals((str(request.course)), 'AdvanceProgramming')
        self.assertEquals(str(request.email), 'saleh@gmail.com')
        self.assertTrue(isinstance(request,Request))
        self.assertTrue(isinstance(request.created,datetime))
        
    
    def testOffrrModel(self):
        course = Course.objects.create(name="LinearAlgebra")
        user = User.objects.create()
        offer = Offer.objects.create(instructor= user, course= course, email="saleh@gmail.com", created= datetime.now())
        self.assertEquals((str(offer.course)), 'LinearAlgebra')
        self.assertEquals(str(offer.email), 'saleh@gmail.com')
        self.assertTrue(isinstance(offer,Offer))
        self.assertTrue(isinstance(offer.created,datetime))  
        