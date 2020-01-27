opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://pinshape.com/search/designs?')


#Scroll down
SCROLL_PAUSE_TIME = 10
# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#get list
try:
    html_list = browser.find_element_by_id("search-results")
    items = html_list.find_elements_by_tag_name("li")

    file = open("output.txt", "w+", encoding='utf8')
except:
  print("Something went wrong")

for item in items:
    try:
        #pin_image_wrapper = item.find_element_by_class_name('pin-image-wrapper')
        pin_image = item.find_element_by_class_name('pin-image')
        image_source = pin_image.get_attribute('data-pin-image-blurred')
        username = item.find_element_by_class_name('username')
        pin_title = item.find_element_by_class_name('pin-title')
        like = item.find_element_by_class_name('like')
        download = item.find_element_by_class_name('repin-count')
        price = item.find_elements_by_tag_name("a")

        #print(pin_image.get_attribute('outerHTML'))

        text = like.text + '\t' + download.text + '\t' + price[-1].text + '\t' + username.text + '\t' + pin_title.text + '\t' + image_source + '\r\n'
        file.write(text)
    except:
        print("Something went wrong 2")


#file = open("output.html", "w+")
#
try:
    file.close()
    browser.close()
except:
    print("Something went wrong 3")