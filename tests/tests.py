from selene.support.shared import browser
from selene import be, have


def test_finds_selene():
    browser.open('/ncr').should(have.title('Google'))
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('#search').should(have.text('User-oriented WEB UI browser'))