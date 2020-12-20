from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):
    """ 首页测试 """

    def test_uses_home_template(self):
        """ 测试使用 home 模板 """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ListViewTest(TestCase):
    """ 列表视图测试 """

    def test_uses_list_template(self):
        """ 测试使用列表模板 """
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_list_items(self):
        """ 测试显示待办事项列表中的所有待办事项 """
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')


class NewListTest(TestCase):
    """ 新增列表测试 """

    def test_can_save_a_POST_request(self):
        """ 测试 POST 请求能够保存数据 """
        self.client.post('/lists/new/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """ 测试 post 请求后重定向 """
        response = self.client.post('/lists/new/', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')


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
