from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from re import sub
from decimal import Decimal
import secrets


class Scrapper:

    def __init__(self):
        pass

    @staticmethod
    def get_balance_data():

        dcap = dict(DesiredCapabilities.PHANTOMJS)

        dcap["phantomjs.page.settings.userAgent"] = secrets.USER_AGENT

        driver = webdriver.PhantomJS(desired_capabilities=dcap)

        driver.set_window_size(800, 600)

        driver.get(secrets.SITE_URL)

        # Username input
        user_input_form = driver.find_element_by_id('login-form')
        user_input = user_input_form.find_element_by_name('IDToken1')
        user_input.send_keys(secrets.USER_NAME)

        user_input_form.submit()

        # Security Question
        try:
            secret_question_form = driver.find_element_by_id('challengequestion')

            if secret_question_form:
                secret_question_input = secret_question_form.find_element_by_name('IDToken1')
                secret_question_input.send_keys('tom')
                secret_question_form.submit()
        except:
            pass

        # Password
        password_form = driver.find_element_by_id('loginForm')
        password_input = password_form.find_element_by_name('IDToken2')
        password_input.send_keys(secrets.PASSWORD)
        password_form.submit()

        # crawl for balance
        current_balance_element = driver.find_elements_by_xpath("//*[contains(text(), 'Current Balance')]")
        balance = current_balance_element[0].find_elements_by_xpath('following-sibling::span[1]')[0].text

        # driver.save_screenshot('screenshot.png')

        driver.quit()

        return balance, '1/2/15'

    @staticmethod
    def to_decimal(money_str):
        return Decimal(sub(r'[^\d.]', '', money_str))
