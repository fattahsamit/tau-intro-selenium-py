"""
These tests cover DuckDuckGo searches.
"""
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    '''
    # Explicit Waits
    import time
    time.sleep(5)
    '''
    '''
    # Implicit Waits
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(browser, 10).until(
        EC.title_contains(phrase+' at DuckDuckGo'))
    '''

    # And the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    # titles = result_page.result_link_titles()
    # matches = [t for t in titles if phrase.lower() in t.lower()]
    # assert len(matches) > 0

    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    # Then the search result title contains "panda"
    assert phrase+' at DuckDuckGo' in result_page.title()
