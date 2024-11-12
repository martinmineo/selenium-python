import json

import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def driver(config):
    # Initialize the ChromeDriver instance
    if config['browser'] == 'Firefox':
        d = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        d = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('--headless')
        d = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser {config["browser"]} not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    d.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield d

    # Quit the WebDriver instance for the cleanup
    d.quit()
