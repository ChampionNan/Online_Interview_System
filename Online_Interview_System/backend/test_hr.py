from .models import *
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class HrViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    Hr.objects.create(name='cbn', mobile='11111111111', email='940107412@qq.com', password='123456')
    Hr.objects.create(name='lsq', mobile='11111111111', email='940107410@qq.com', password='123456')
    Hr.objects.create(name='lcy', mobile='11111111111', email='940107411@qq.com', password='123456')

  def test_hr_set(self):
    """
    Test hr set
    """
    url = 'hr/'
    data = {'name': 'cbn', 'mobile': '11111111111', 'email': '940107412@qq.com'}
    response = self.client.post(url, data, format='json')
    json_data = eval(response.content)
    self.assertEqual(json_data[0]['success'], True)


  def test_hr_all(self):
    url = 'hr/getall/'
    data = {''}
    response = self.client.get(url, data, format='json')
    json_data = eval(response.content) 
    length = len(json_data[0])
    self.assertEqual(length, 3)

