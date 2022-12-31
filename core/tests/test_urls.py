from django.test import TestCase
from django.urls import reverse, resolve
from ..views import *


class UrlTest(TestCase):
    def testRequestList(self):
        url = reverse('RequestList')
        self.assertEquals(resolve(url).func.view_class, RequestList)
        
    def testUserRequestList(self):
        url = reverse('UserRequestList')
        self.assertEquals(resolve(url).func.view_class, UserRequestList)

    def testRequestCreate(self):
        url = reverse('RequestCreate')
        self.assertEquals(resolve(url).func.view_class, RequestCreate)

    def testRequestRetrieve(self):
        url = reverse('RequestRetrieve', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, RequestRetrieve)
    
    def testRequestUpdate(self):
        url = reverse('RequestUpdate')
        self.assertEqual(resolve(url).func.view_class, RequestUpdate)

