"""
These tests cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear', 'panda', 'python', 'polar bear', 'panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(driver, phrase):
    search_page = DuckDuckGoSearchPage(driver)
    result_page = DuckDuckGoResultPage(driver)

    # Given the DuckDuckGo page is displayed
    search_page.load()

    # When the user searches for the phrase
    search_page.search(phrase)

    # Then the search result query is the phrase
    assert phrase in result_page.search_input_value()

    # And the search result title contains the phrase
    assert phrase in result_page.title()
