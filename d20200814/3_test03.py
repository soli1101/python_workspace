
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#코레일 열차표 예매
browser = webdriver.Chrome('e:/dev/python_workspace/chromedriver.exe')
browser.get("http://www.letskorail.com")

# print(browser.window_handles)

browser.switch_to.window(browser.window_handles[1])
browser.close()

print(browser.window_handles)

browser.switch_to.window(browser.window_handles[1])
browser.close()

browser.switch_to.window(browser.window_handles[0])

browser.find_element_by_css_selector("#txtGoStart")
element = browser.find_element_by_css_selector('#txtGoEnd')
element.click()
element.send_keys(Keys.BACK_SPACE)
element.send_keys(Keys.BACK_SPACE)
element.send_keys("포항")
element.send_keys(Keys.ENTER)

element = browser.find_element_by_xpath('//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img')
element.click()
browser.switch_to_window(browser.window_handles[1])
element = browser.find_element_by_id("d20200815")
element.click()

browser.switch_to_window(browser.window_handles[0]) #-->main창으로 다시 옮김

element = browser.find_element_by_css_selector("#time > option:nth-child(13)")
element.click()
element = browser.find_element_by_css_selector("#res_cont_tab01 > form > div > fieldset > p > a > img")
element.click()

time.sleep(3)
# browser.find_elements_by_xpath('//*[@id="txtGoStart"]')
