from selenium import webdriver

login_url = 'http://localhost/wordpress/wp-login.php'

def login(self):
    self.dr.get(login_url)
    self.dr.find_element_by_name('log').send_keys('admin')
    self.dr.find_element_by_name('pwd').send_keys('admin')
    self.dr.find_element_by_name('wp-submit').click()
