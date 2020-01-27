ids = browser.find_elements_by_xpath('//*[@id]')
        for ii in ids:
            # print ii.tag_name
            print(ii.get_attribute('id'))