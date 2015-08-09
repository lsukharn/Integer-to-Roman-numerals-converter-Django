import unittest
from django.test import TestCase
from django.http import HttpRequest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from views import roman_form

class FT(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/form')
        assert 'Roman numerals' in self.browser.title

    def tearDown(self):
        self.browser.quit()

    def test_post_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['integer'] = 777

        response = roman_form(request)

        #check whether 777 is correctly converted into DCCLXXVII
        self.assertIn('DCCLXXVII', response.content.decode())

    def test_input_form(self):
        input =  self.browser.find_element_by_id('id_integer')
        input.send_keys('111')
        input.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_form_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Roman numerals: CXI', [row.text for row in rows])


class ViewTest(TestCase):

    def test_html_render(self):
        response = self.client.get('/form/')
        self.assertTemplateUsed(response, 'roman_form.html')
