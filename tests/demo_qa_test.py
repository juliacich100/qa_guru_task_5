from selene.support.shared import browser
from selene import have, be, command
import os
import tests

def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Julia')
    browser.element('#lastName').should(be.blank).type('Ekkart')
    browser.element('#userEmail').should(be.blank).type('test@mail.com')
    browser.element('[name=gender][value=Female] + label').click()
    browser.element('#userNumber').type('0123456789')

    browser.element('[class = "react-datepicker__input-container"]').click()
    browser.element('[class = "react-datepicker__month-select"]').click()
    browser.element('[value= "10"]').click()
    browser.element('[class = "react-datepicker__year-select"]').click()
    browser.element('[value="1985"]').click()
    browser.element('[class = "react-datepicker__day react-datepicker__day--014"]').click()

    ads = browser.all('[id^=google_ads_][id$=container__]')
    ads.should(have.size_less_than_or_equal(3))
    ads.perform(command.js.remove)

    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#subjectsInput').type('Accounting').press_enter()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), 'more.jpg')
        )
    )

    browser.element('#currentAddress').should(be.blank).type('Sitsevaya st')
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaipur').press_enter()

    browser.element('#submit').press_enter()

    browser.element('.table').all('td').even.should(have.texts(
        'Julia Ekkart',
        'test@mail.com',
        'Female',
        '0123456789',
        '14 November,1985',
        'Accounting',
        'Music',
        'more.jpg',
        'Sitsevaya st',
        'Rajasthan Jaipur'
    ))
