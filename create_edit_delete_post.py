# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
import time
import wplogin

class WordPressTestCase(unittest.TestCase):
    dr = None
    post_list_url = 'http://localhost/wordpress/wp-admin/edit.php'
	
    def setUp(self):
        self.dr = webdriver.Firefox()

    def test_create_post(self):
        wplogin.login(self)
        title = self.create_post()
        self.dr.get(self.post_list_url)
        post_list_table = self.dr.find_element_by_class_name('wp-list-table')
        self.assertTrue(title in post_list_table.text)

    def test_edit_post(self):
        wplogin.login(self)
        post_title = self.create_post()
        print "We will edit the post titled '%s' and rename the ttile as AAA" % post_title
        self.dr.get(self.post_list_url)
        edit_list_table = self.dr.find_element_by_link_text(post_title)
        edit_list_table.click()
        edit_list_table.click()
        sleep(1)
        edit_title = self.dr.find_element_by_id("title")
        edit_title.clear()
        edit_title.send_keys("AAA")
        self.dr.find_element_by_id("publish").click()

    def test_delete_post(self):
        wplogin.login(self)
        title = self.create_post()
        print "We will delete the post titled '%s'" % title
        self.dr.get(self.post_list_url)
        title_xpath = "//label[contains(text()," + title + ")]/following-sibling::input[@type='checkbox']"
        post_list_table = self.dr.find_element_by_xpath(title_xpath).click()
        Select(self.dr.find_element_by_name("action")).select_by_visible_text(u"移至回收站")
        self.dr.find_element_by_id("doaction").click()

    def create_post(self):
        create_post_url = 'http://localhost/wordpress/wp-admin/post-new.php'
        self.dr.get(create_post_url)
        title_or_content = 'new_post' + str(time.time())
        self.dr.find_element_by_name('post_title').send_keys(title_or_content)
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
        print js
        self.dr.execute_script(js)
        self.dr.find_element_by_name('publish').click()
        return title_or_content

    def tearDown(self):
        sleep(3)
        self.dr.quit()
		
if __name__ == '__main__':
    unittest.main()
