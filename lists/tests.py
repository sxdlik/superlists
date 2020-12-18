from django.test import TestCase

from lists.models import Item


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


class ItemModelTest(TestCase):
    """ 待办事项模型测试 """

    def test_saving_and_retrieving_items(self):
        """ 测试待办事项正常保存 """
        first_item = Item()
        first_item.text = 'one item'
        first_item.save()

        second_item = Item()
        second_item.text = 'two item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'one item')
        self.assertEqual(second_saved_item.text, 'two item')
