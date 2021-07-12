from django.test import TestCase
from django import urls
from django.test import TestCase , SimpleTestCase
from django.urls import reverse
# Create your tests here.


class SnackTest(TestCase): 

    def test_home_view (self): 
        url = reverse ('view')
        actual = self.client.get(url).status_code
        excepted= 200
        self.assertEqual (actual , excepted) 

    def test_template_view(self):  
        url = reverse ('view')
        actual = self.client.get(url)
        excepted= 'snack_list.html'
        self.assertTemplateUsed (actual , excepted) 



