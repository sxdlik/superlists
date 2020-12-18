from django.test import TestCase


class HomePageTest(TestCase):
    """ 首页测试 """

    def test_uses_home_template(self):
        """ 测试使用 home 模板 """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """ 测试 POST 请求能够保存数据 """
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
