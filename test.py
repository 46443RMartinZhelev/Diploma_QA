#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebsite:
  # 1. Check browser configuration in browser_setup_and_teardown
  # 2. Run 'Selenium Tests' configuration
  # 3. Test report will be created in reports/ directory

  @pytest.fixture(autouse=True)
  def browser_setup_and_teardown(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    self.browser = webdriver.Chrome(chrome_options)

    self.browser.maximize_window()
    self.browser.implicitly_wait(10)
    self.browser.get("https://www.automationexercise.com")

    yield

    self.browser.close()
    self.browser.quit()

  @pytest.mark.skip(reason="E2E Test Case - Run Only In Formal & Sanity Runs")
  def test_register_user(self):
    """Test Case 1: Register User"""
    expected_tab_title = 'Automation Exercise'
    expected_signup_title = 'New User Signup!'
    username = 'MartinZhelev123'
    user_email = "martin.zhelev@unibit.bg"
    title = 'Mr.'
    user_full_name = ['Martin', 'Zhelev']
    password = 'test123'
    date_of_birth = [8, 4, 2001] # list object allows easier recovery later on

    # 3. Verify that home page is visible successfully
    actual_tab_title = self.browser.title

    assert actual_tab_title == expected_tab_title

    # 4. Click on 'Signup / Login' button
    login_button = self.browser.find_element(By.XPATH, "//a[@href='/login']")
    login_button.click()

    # 5. Verify 'New User Signup!' is visible
    actual_signup_text = self.browser.find_element(By.CSS_SELECTOR, "div[class='signup-form'] h2").text

    assert actual_signup_text == expected_signup_title

    # 6. Enter name and email address
    user_name_field = self.browser.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")
    email_field = self.browser.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")

    user_name_field.click()
    user_name_field.send_keys(username)
    email_field.click()
    email_field.send_keys(user_email)

    # 7. Click 'Signup' button
    signup_button = self.browser.find_element(By.CSS_SELECTOR,"button[data-qa='signup-button']")
    signup_button.click()

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expected_account_information_text = 'ENTER ACCOUNT INFORMATION'
    actual_account_information_text = self.browser.find_element(By.CSS_SELECTOR,"html > body > section > div > "
                                                                                "div > div > div:nth-of-type(1) > h2 > b")

    assert actual_account_information_text.text == expected_account_information_text

    # 9. Fill details: Title, Name, Email, Password, Date of birth
    if title == 'Mr.':
      title_locator = "label[for='id_gender1']"
    else:
      title_locator = "label[for='id_gender2']"
    title_button = self.browser.find_element(By.CSS_SELECTOR, title_locator)
    title_button.click()

    password_input = self.browser.find_element(By.CSS_SELECTOR, "input[id='password']")
    password_input.click()
    password_input.send_keys(password)

    birthdate_selector = self.browser.find_element(By.CSS_SELECTOR, "select[data-qa='days']")
    birthdate_selector.click()
    birthdate_selector = self.browser.find_element(By.CSS_SELECTOR, "select[data-qa='days'] option[value='" +
                                                   str(date_of_birth[0]) + "']")
    birthdate_selector.click()
    birthdate_selector = self.browser.find_element(By.CSS_SELECTOR, "select[data-qa='months']")
    birthdate_selector.click()
    birthdate_selector = self.browser.find_element(By.CSS_SELECTOR, "select[data-qa='months'] option[value='" +
                                                   str(date_of_birth[1]) + "']")
    birthdate_selector.click()
    birthdate_selector = self.browser.find_element(By.CSS_SELECTOR, "select[data-qa='years']")
    birthdate_selector.click()
    birthdate_selector = self.browser.find_element(By.CSS_SELECTOR, "select[data-qa='years'] option[value='" +
                                                   str(date_of_birth[2]) + "']")
    birthdate_selector.click()

    # 10. Select checkbox 'Sign up for our newsletter!'
    newsletter_selector = self.browser.find_element(By.CSS_SELECTOR, "input[id='newsletter']")
    newsletter_selector.click()

    # 11. Select checkbox 'Receive special offers from our partners!'
    optin_selector = self.browser.find_element(By.CSS_SELECTOR, "input[id='optin']")
    optin_selector.click()

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    first_name_input = self.browser.find_element(By.CSS_SELECTOR, "input[data-qa='first_name']")
    first_name_input.click()
    first_name_input.send_keys(user_full_name[0])

    last_name_input = self.browser.find_element(By.CSS_SELECTOR, "input[data-qa='last_name']")
    last_name_input.click()
    last_name_input.send_keys(user_full_name[1])

    company_input = self.browser.find_element(By.CSS_SELECTOR, "input[id='company']")
    company_input.click()
    company_input.send_keys("Martin Zhelev Test OOD")

    address_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='address1']")
    address_input.click()
    address_input.send_keys("Test Street, 1000, MZT OOD")

    address_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='address2']")
    address_input.click()
    address_input.send_keys("Test Street, 2000, MZT OOD")

    country_select = self.browser.find_element(By.CSS_SELECTOR, "select[id='country']")
    country_select.click()
    country_select = self.browser.find_element(By.CSS_SELECTOR, "option[value='United States']")
    country_select.click()

    state_select = self.browser.find_element(By.CSS_SELECTOR, "input[id='state']")
    state_select.click()
    state_select.send_keys("Oregon")

    state_select = self.browser.find_element(By.CSS_SELECTOR, "input[id='city']")
    state_select.click()
    state_select.send_keys("Oregon City")

    zipcode_select = self.browser.find_element(By.CSS_SELECTOR, "input[id='zipcode']")
    zipcode_select.click()
    zipcode_select.send_keys("97045")

    phone_number_select = self.browser.find_element(By.CSS_SELECTOR, "#mobile_number")
    phone_number_select.click()
    phone_number_select.send_keys("971-204-4603")

    # 13. Click 'Create Account button'
    create_account_button = self.browser.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    create_account_button.click()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    account_created_text = self.browser.find_element(By.CSS_SELECTOR, "html > body > section > div "
                                                                      "> div > div > h2 > b").text
    assert account_created_text == "ACCOUNT CREATED!"

    # 15. Click 'Continue' button
    continue_button = self.browser.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    continue_button.click()

    # 16. Verify that 'Logged in as username' is visible
    logged_in_info_text = self.browser.find_element(By.CSS_SELECTOR, "html > body > header > div > div > div >"
                                                            " div:nth-of-type(2) > div > ul > li:nth-of-type(10) > a").text
    logged_in_info_username = self.browser.find_element(By.CSS_SELECTOR, "html > body > header > div > div > div "
                                                                         "> div:nth-of-type(2) > div > ul "
                                                                         "> li:nth-of-type(10) > a > b").text
    assert "Logged in as" in logged_in_info_text
    assert logged_in_info_username == username

    # 17. Click 'Delete Account' button
    delete_account_button = self.browser.find_element(By.CSS_SELECTOR, "html > body > header > div > div > div > "
                                                                       "div:nth-of-type(2) > div > ul > "
                                                                       "li:nth-of-type(5) > a")
    delete_account_button.click()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

    account_deleted_text = self.browser.find_element(By.CSS_SELECTOR, "html > body > section > div >"
                                                                      " div > div > h2 > b").text
    assert account_deleted_text == "ACCOUNT DELETED!"
