import os.path

from selene import browser, have, command


def test_complete_todo():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Stanislav')
    browser.element('#lastName').type('Cyberslav')
    browser.element('#userEmail').type('horns.n.hooves@scam.net')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('8005553535')

    # browser.element('#dateOfBirthInput').send_keys(u'\ue009' + u'a')  # второй метод установки даты "одним махом"
    # browser.element('#dateOfBirthInput').type('01 01 01')
    # browser.element('#dateOfBirthInput').press_enter()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2001"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="0"]').click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('#subjectsInput').type('c').press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('pic.png'))
    browser.element('#currentAddress').type('Улица Есенина, дом каруселина')
    browser.element("#state").perform(command.js.scroll_into_view)
    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()

    browser.element('#submit').click()

    browser.element(".modal-content").element("tbody").all("tr").all("td").even.should(have.exact_texts((
        'Stanislav Cyberslav',
        'horns.n.hooves@scam.net',
        'Other',
        '8005553535',
        '01 January,2001',
        'Physics',
        'Sports, Reading, Music',
        'pic.png',
        'Улица Есенина, дом каруселина',
        'Uttar Pradesh Lucknow'
    )))
