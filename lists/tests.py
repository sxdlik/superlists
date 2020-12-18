from django.test import TestCase
from django.urls import resolve
from django.http import HttpResponse

from lists.views import home_page


class HomePageTest(TestCase):
    """ 首页测试 """

    def test_uses_home_template(self):
        """ 测试使用 home 模板 """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
