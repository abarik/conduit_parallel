import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url, waiting_time=20):
        self.driver = driver
        self.url = url
        self.waiting_time = waiting_time

    def go(self):
        try:
            self.driver.get(self.url)
        except BaseException:
            self.log_error('Page cannot be reached: ' + self.url)
            assert False
        else:
            assert True
        return None

    def close_test(self):
        self.driver.quit()
        return None

    def log_error(self, text):
        sys.stdout.write(text)
        # print(text)
        return None

    def get_element(self, by_locator, wtime=None):
        element = WebDriverWait(
            self.driver, self.waiting_time if wtime is None else wtime).until(
            EC.visibility_of_element_located(by_locator))
        return element

    def get_elements(self, by_locator, wtime=None):
        elements = WebDriverWait(
            self.driver, self.waiting_time if wtime is None else wtime).until(
            EC.visibility_of_all_elements_located(by_locator))
        return elements

    def get_element_attribute(self, by_locator, value):
        element = self.get_element(by_locator)
        return element.get_attribute(value)

    def get_element_text(self, by_locator):
        return self.get_element().text

    @staticmethod
    def get_attribute_on_webelement(webelement, value):
        return webelement.get_attribute(value)

    @staticmethod
    def do_click_on_webelement(webelement):
        return webelement.click()

    @staticmethod
    def get_element_text_on_webelement(webelement):
        return webelement.text

    def set_checkbox(self, by_locator, setting):
        """
        Setting a checkbox
        :param by_locator: locator tuple
        :param setting: a string, 'checked' or not
        :return: None
        """
        inp_checkbox = self.get_element(by_locator)
        if setting == 'checked':
            if inp_checkbox.get_attribute('checked') == 'true':
                pass
            else:
                inp_checkbox.click()
        else:
            if inp_checkbox.get_attribute('checked') == 'true':
                inp_checkbox.click()
            else:
                pass
        return None

    def set_select_option(self, by_locator, value):
        """
        Setting a select field to a value
        :param options: locate the select
        :param value: A value for a option
        :return: None
        """
        element = self.get_element(by_locator)
        options = element.find_elements_by_xpath('./option')
        for opt in options:
            if opt.get_attribute('value') == value:
                opt.click()
        return None

    def do_send_keys(self, by_locator, value):
        element = self.get_element(by_locator)
        element.clear()
        element.send_keys(value)
        return None

    def do_click(self, by_locator):
        element = WebDriverWait(
            self.driver, self.waiting_time).until(EC.element_to_be_clickable(by_locator))
        element.click()
        return None

    def get_url(self, url):
        WebDriverWait(self.driver, self.waiting_time).until(EC.url_contains(url))
        return self.driver.current_url
