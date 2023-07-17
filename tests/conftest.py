"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    # Setup Phase
    # Initialize the EdgeDriver instance
    b = selenium.webdriver.Edge()

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Cleanup Phase
    # Quit the WebDriver instance for the cleanup
    b.quit()
