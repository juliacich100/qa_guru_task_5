import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()