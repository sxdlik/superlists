import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """ 新用户测试 """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """ 测试可以输入一个待办事项以及显示待办事项列表 """

        # 东东听说有一个很酷的在线待办事项应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页的标题和头部都包含有 "待办事项" 这个词
        self.assertIn('待办事项', self.browser.title)
        self.fail('本次测试完成')

        # 应该邀请他输入一个待办事项

        # 他在一个文本框中输入了 "学习Django"

        # 他按下回车键后，页面更新了
        # 待办事项中显示了 "1：学习Django"

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 他输入了 "学习Python"

        # 页面再次更新，他的清单中显示了这两个待办事项

        # 东东想知道这个网站是否会记住他的清单
        # 他看到网站为他生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 他访问这个URL，发现他的待办事列表还在

        # 他很满意，去睡觉了


if __name__ == '__main__':
    unittest.main()