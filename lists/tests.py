from django.test import TestCase
from django.urls import resolve
from django.http import HttpResponse

from lists.views import home_page


class HomePageTest(TestCase):
    """ 首页测试 """

    def test_root_url_resolves_to_home_page_view(self):
        """ 测试根路由返回首页的视图函数 """
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """ 测试首页使用正确的html """
        request = HttpResponse()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>待办事项列表</title>', html)
        self.assertTrue(html.endswith('</html>'))
