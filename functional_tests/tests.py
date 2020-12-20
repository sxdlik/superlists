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
        self.wait_for_row_in_list_table('1: 东东学习Django')
        self.wait_for_row_in_list_table('2: 东东学习Python')

        # 东东想知道这个网站是否会记住他的清单
        # 他看到网站为他生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 他访问这个URL，发现他的待办事列表还在

        # 他很满意，去睡觉了
        self.fail('本次测试完成')

