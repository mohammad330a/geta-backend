from django.test import TestCase
from django.urls import reverse, resolve
from ..views import *


class UrlTest(TestCase):
    def testRequestList(self):
        url = reverse('RequestList')
        print(url)
        self.assertEquals(resolve(url).func.view_class, RequestList)
        
    def testRequestList(self):
        url = reverse('UserRequestList')
        print(url)
        self.assertEquals(resolve(url).func.view_class, UserRequestList)

