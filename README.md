# Web-Scraping-Indeed-Job-Postings-with-Selenium-1



http://chromedriver.chromium.org/downloads

https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/

https://notebooks.azure.com/hello-codeheroku/projects/data-science-jobs-analysis

Implicit Waits and Explicit Waits
Implicit Waits
As we have learnt before, implicit waits are a method to make the test wait for the webpage’s components to load, so that they can be available during our tests. Selenium originally borrowed this idea from Watir. Now what does implicit wait does actually. Suppose we wrote a script like this

 

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
from selenium import webdriver
import unittest
 
class AlertHandle(unittest.TestCase):
 
   def setUp(self):
      self.driver=webdriver.Firefox()
      self.driver.implicitly_wait(30)
      self.driver.maximize_window()
 
      self.driver.get('http://www.questionselenium.com/2013/09/sample-confirmation-box.html')
 
  def test_Alterbox(self):
      print("This is a test to show implicit wait")
  def tearDown(self):
      self.driver.quit()
 
if __name__=="__main__"
unittest.main(versbosity=2)
Now the implicitly_wait( ) method tells the script , more precisely, it tells the Webdriver to poll the DOM for a certain amount of time , here for 30 seconds, when trying to find an element or elements if they are not immediately available. Here by poll, we mean to check the DOM again and again.

Once defined, implicit wait will be defined for the whole life time of a Webdriver object instance, until it is changed. So once defined in a script, it will be active for the lifetime of a script, until modified. By default, the implicit wait time set is 0.

Also, implicit wait won’t allow you to set any predefined conditions to wait for any webelement to be present or as such. If you want such kinda flexibility, you need to take the help of explicit wait, which is why we are going to discuss this in next section.

 

Explicit Wait
Not in every situation you want a predefined wait to be available in tests and wait for that long duration, for the element to be present or be visible in the DOM. We want to define a  wait condition, so that we can be able to wait for only that specific web element to be present and then carry on with the script functioning. To achieve this Selenium webdriver API provides us with explicit waits.

Explicit waits are a good way to organize a test script and provide more flexibility, by allowing us to design out tests in a way, where we can wait for some predefined or custom conditions and then carry on with what we want.

Explicit waits are implemented using the WebDriverWait and expected_conditions class of the python/Java API.

Let see an suppose we have a JS alert on a webpage, and we want to see if that clicking on that button, which fires the alert , actually fires the alert on not. Now, we would want this test to wait to click on the button and then only wait for that amount of time when the alert is not present. Once the alert appears, we would just want to accept it and then go on and accept the alert.

 

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
 
class Explicit_waiting(unittest.TestCase):
 
   def setUp(self):
       self.driver=webdriver.Firefox()
       self.driver.maximize_window()
 
       #getting the browser navigation
       self.driver.get('')
 
   def test_BrowserNav(self):
       driver=self.driver
 
       tt1=driver.find_element_by_id('timingAlert')
       tt1.click()
 
       WebDriverWait(self.driver,10).until(expected_conditions.alert_is_present())
 
       alert1=driver.switch_to.alert
 
       alert1.accept()
 
   def tearDown(self):
       self.driver.quit()
 
if __name__="__main__":
unittest.main(verbosity=2)
 

Now, focus specifically on this line of code

1
WebDriverWait(self.driver,10).until(expected_conditions.alert_is_present())
Here, we are using the WebDriverWait to make the driver wait a maximum of 10 seconds, until, the alert shows up. If the alert doesn’t appear in that stipulated time, the Webdriver will throw an NoAlertPresentException

During the course of test execution, Webdriver calls the ExpectedCondition every 500 milliseconds, untill it returns successfully.

 

Expected Conditions :

These are some common conditions which are frequently encountered when automating web applications.

Selenium Python binding provides some convenience methods so you don’t have to code an expected_condition class yourself or create your own utility package for them.

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
You can read about the whole list of the expected conditions in the official Selenium python documentation here.



How to wait for elements in Python Selenium WebDriver
 admin    Python Selenium    April 5, 2018  |  5
We all know and experimented that Selenium WebDriver can interact with web browser and simulate user actions. User actions could be click, select, type etc.. or combinations of these actions. However most of the user action requires some kind of wait before performing it.

Reasons could be many, including but not limited to below.

Page is not loaded yet
Element to interact with is not available in DOM yet
AJAX is still loading and element will be created after AJAX
Delay in page response etc…
In modern applications, elements within the page may load at different time intervals even after page is loaded. This makes locating elements difficult; if the element Selenium looking for is not present in the DOM, it will raise NoSuchElementException exception. There should be some kind of delay to wait for these elements. At the same time, this delay should not make test script execution longer.

Using waits, we can wait for an element to be available in DOM. Wait provides some time interval between actions performed like locating element or any other operation with the element.

Implicit Wait:

An implicit wait instructs Selenium WebDriver to poll DOM for a certain amount of time, this time can be specified, when trying to find an element or elements that are not available immediately. The default setting is 0 seconds which means WebDriver will not wait before any operations on element.

Once set, the implicit wait is set for the life of the WebDriver object i.e. all actions will be delayed by given time.

Syntax:
driver.implicitly_wait(10)

Pass number of seconds to wait as an argument

Python
1
from selenium import webdriver
2
​
3
driver = webdriver.Firefox()
4
driver.implicitly_wait(15)
5
driver.get("http://url")
6
driver.find_element_by_id("id_of_element").click()
Explicit Wait:

Explicit wait is used to specify wait condition for a particular element. Here we define to wait for a certain condition to occur before proceeding further in the code.

There can be instance when a particular element takes more than usual time to load. In that case no need to set a huge time to Implicit wait, as this will make browser to wait for the same time for every element. To avoid that situation explicit wait is used by defining a separate wait time only on the required element.


 
There are some predefined methods provided that will help your script to wait only as long as required. WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.

Following two packages are required to set explicit wait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

Python
1
from selenium import webdriver
2
from selenium.webdriver.common.action_chains import ActionChains
3
from selenium.webdriver.common.by import By
4
from selenium.webdriver.support.ui import WebDriverWait
5
from selenium.webdriver.support import expected_conditions as ec
6
​
7
driver = webdriver.Chrome()
8
​
9
driver.get("http://url")
10
driver.maximize_window()
11
​
12
# wait for element to appear, then hover it
13
wait = WebDriverWait(driver, 10)
14
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@data-tracking-id='men']")))
15
ActionChains(driver).move_to_element(men_menu).perform()
16
​
17
# wait for Fastrack menu item to appear, then click it
18
fastrack = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//a[@data-tracking-id='0_Fastrack']")))
19
fastrack.click()
This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds. WebDriverWait by default calls the ExpectedCondition every 500 milliseconds, which is called poll frequency, until it returns successfully. A successful return is for ExpectedCondition type is Boolean return true or not null return value for all other ExpectedCondition types.

We have the option to change the poll frequency by passing keyword argument ‘poll_frequency’ which accepts values in seconds. Default value is 0.5 second. For instance, lets change poll frequency to 1 second.

Python
1
wait = WebDriverWait(driver, 10, poll_frequency=1)
The expected_conditions module contains a set of predefined conditions to use with WebDriverWait.

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
