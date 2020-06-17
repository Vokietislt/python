from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException

search=["game of thrones","poe","xxx tentacion","one piece","avengers endgame","wikipedia","lucifer"]


def btnClick(what):
# locate submit button by_xpath
    button = driver.find_element_by_xpath('//*[@'+what+']')
    button.click()

def findElement (where,what):
    whereTo = driver.find_element_by_xpath('//*[@'+where+']')
    if what ==".":
        whereTo.clear()
    else:
     whereTo.send_keys(what)

def getElement (element):
    elementClass = driver.find_element_by_class_name(element)
    to = elementClass.text
    print(to)
    return to

def start(whereTo):
    # driver.get method() will navigate to a page given by the URL address
    driver.get(whereTo)
    findElement('type="search"',search[4])
    btnClick('type="submit"')
    getElement('infobox')

# =====================================================================
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('chromedriver.exe')
start('https://www.wikipedia.org/')
l=""
while(l!="stop"):
    l = input ("\ntype stop to stop:\nwhere to go next:")
    findElement('type="search"',l)
    if l ==".":
        start('https://www.wikipedia.org/')
    else:
        btnClick('type="submit"')
        try:
            getElement('infobox')
        except NoSuchElementException:
            print("No information table")
            findElement('type="search"',".")

