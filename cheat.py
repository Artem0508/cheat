from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://flipgrid.com/de42a1f0")

while (True):
    browser.find_element_by_class_name("likeButton").click()
    browser.refresh()
