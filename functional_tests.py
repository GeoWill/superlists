#functional testing module
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser = webdriver.Firefox()

        #Edith has heard about a cool new online to-do app.
        #She goes to check out it's home page
        self.browser.get('http://localhost:8000')

        #She opens the homepage
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #She is immeadiatly invited to enter a todo item

        # She types "buy peakcock feathers" into a text box

        #when she hits enter the page updates and the page lists:
        #"1: buy peacocl feathers" as an item in a to-do list

        #There is still a texbox inviting her to add anther item.

        #She enters "Use peacock feathers to make a fly"

        #the page updates again showing both items in the list

        #How will she save her list?
        #the site generates a unique url for her
        #there is some text explaining this

        #she visits that url - her todo list is still there.

        #satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
