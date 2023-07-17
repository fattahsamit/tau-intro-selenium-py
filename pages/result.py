"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, "a.result__a")
    SEARCH_INPUT = (By.ID, "searchbox_input")

    def __init__(self, browser):
        self.browser = browser

    def search_input_value(self):
        # TODO
        return ""

    def title(self):
        # TODO
        return ""

    def result_link_titles(self):
        # TODO
        return []
