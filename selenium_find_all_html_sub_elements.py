for item in items:
    #text = item.text
    #print(text)
    # start from your target element, here for example, "header"
    all_children_by_css = item.find_elements_by_css_selector("*")
    #all_children_by_xpath = item.find_elements_by_xpath(".//*")
    for subitem in all_children_by_css:
        print(subitem.text + ',', end = '')
    #print('len(all_children_by_css): ' + str(len(all_children_by_css)))
    #print('len(all_children_by_xpath): ' + str(len(all_children_by_xpath)))