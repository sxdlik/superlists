from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):
    """ 首页测试 """

    def test_root_url_resolves_to_home_page_view(self):
        """ 测试根路由返回首页的视图函数 """
        found = resolve('/')
        self.assertEqual(found.func, home_page)
