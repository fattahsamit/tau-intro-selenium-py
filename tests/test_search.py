"""
These tests cover DuckDuckGo searches.
"""
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(PHRASE)

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
        EC.title_contains(PHRASE+' at DuckDuckGo'))
    '''

    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    # titles = result_page.result_link_titles()
    # matches = [t for t in titles if PHRASE.lower() in t.lower()]
    # assert len(matches) > 0

    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    # Then the search result title contains "panda"
    assert PHRASE+' at DuckDuckGo' in result_page.title()
