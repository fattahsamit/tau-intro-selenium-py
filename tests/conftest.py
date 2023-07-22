"""
This module contains shared fixtures.
"""
import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Edge', 'Chrome', 'Firefox',
                                 "Headless Edge", "Headless Chrome", "Headless Firefox"]
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Setup Phase
    if config['browser'] == 'Edge':
        b = selenium.webdriver.Edge()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Headless Edge':
        opts = selenium.webdriver.EdgeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Edge(options=opts)
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    elif config['browser'] == 'Headless Firefox':
        opts = selenium.webdriver.FirefoxOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Firefox(options=opts)
    else:
        raise Exception(f"Browser '{config['Browser']}' is not supported!")

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Cleanup Phase
    # Quit the WebDriver instance for the cleanup
    b.quit()
