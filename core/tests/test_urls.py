from django.test import TestCase
from django.urls import reverse, resolve
from ..views import *


class UrlTest(TestCase):
    def testRequestList(self):
        url = reverse('RequestList')
        self.assertEquals(resolve(url).func.view_class, RequestList)
        
    def testRequestList(self):
        url = reverse('UserRequestList')
        self.assertEquals(resolve(url).func.view_class, UserRequestList)

    def testRequestList(self):
        url = reverse('RequestCreate')
        self.assertEquals(resolve(url).func.view_class, RequestCreate)
