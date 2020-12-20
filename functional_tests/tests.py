import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    """ 新用户测试 """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        """ 测试可以输入一个待办事项以及显示待办事项列表 """

        # 东东听说有一个很酷的在线待办事项应用
        # 他去看了这个应用的首页
        self.browser.get(self.live_server_url)

        # 他注意到网页的标题和头部都包含有 "待办事项" 这个词
        self.assertIn('待办事项', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('待办事项', header_text)

        # 应该邀请他输入一个待办事项
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), '请输入你的待办事项')

        # 他在一个文本框中输入了 "东东学习Django"
        input_box.send_keys('东东学习Django')

        # 他按下回车键后，页面更新了
        # 待办事项中显示了 "1：东东学习Django"
        input_box.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: 东东学习Django')

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 他输入了 "学习Python"
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('东东学习Python')
        input_box.send_keys(Keys.ENTER)

        # 页面再次更新，他的清单中显示了这两个待办事项
        self.wait_for_row_in_list_table('2: 东东学习Python')
        self.wait_for_row_in_list_table('1: 东东学习Django')

        # 他很满意，去睡觉了

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """ 测试多用户分别开始一个新的待办事项列表 """
        # 东东新建一个待办事项清单
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys('东东在学习英语')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: 东东在学习英语')

        # 他注意到清单有个唯一的URL
        dd_list_url = self.browser.current_url
        self.assertRegex(dd_list_url, '/lists/.+')

        # 现在，另外一个叫果果的用户访问了网站
        # # 使用一个新浏览器会话
        # # 确保东东的信息不会从cookie中泄露出去
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 果果访问首页
        # 页面中看不到东东的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('东东在学习英语', page_text)
        self.assertNotIn('东东学习Python', page_text)

        # 东东新输入一个待办事项，新建了一个清单
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('果果喜欢喝牛奶')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: 果果喜欢喝牛奶')

        # 果果也获得了他唯一的URL
        gg_list_url = self.browser.current_url
        self.assertRegex(gg_list_url, '/lists/.+')
        self.assertNotEqual(gg_list_url, dd_list_url)

        # 这个页面还是没有东东的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('东东学习Django', page_text)
        self.assertIn('果果喜欢喝牛奶', page_text)

        # 两人都很满意，然后去睡觉了
