from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver")

df = pd.DataFrame(columns=["Title", "Location", "Company", "Salary", "Sponsored", "Description"])

for i in range(0, 500, 10):
    driver.get('https://www.indeed.co.in/jobs?q=artificial%20intelligence&l=India&start=' + str(i))
    jobs = []
    driver.implicitly_wait(4)

    for job in driver.find_elements_by_class_name('result'):

        soup = BeautifulSoup(job.get_attribute('innerHTML'), 'html.parser')

        try:
            title = soup.find("a", class_="jobtitle").text.replace("\n", "").strip()
            print(title)

        except:
            title = 'None'
            print(title)


        try:
            location = soup.find(class_="location").text
            print(location)
        except:
            location = 'None'
            print(location)

        try:
            company = soup.find(class_="company").text.replace("\n", "").strip()
            print(company)
        except:
            company = 'None'
            print(company)

        try:
            salary = soup.find(class_="salary").text.replace("\n", "").strip()
            print(salary)
        except:
            salary = 'None'
            print(salary)

        try:
            sponsored = soup.find(class_="sponsoredGray").text
            sponsored = "Sponsored"
            print(sponsored)
        except:
            sponsored = "Organic"
            print(sponsored)
    '''
      sum_div = job.find_element_by_xpath('./div[3]')
        try:
            sum_div.click()
        except:
            close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]
            close_button.click()
            sum_div.click()
        job_desc = driver.find_element_by_id('vjs-desc').text

        df = df.append({'Title': title, 'Location': location, "Company": company, "Salary": salary,
                        "Sponsored": sponsored, "Description": job_desc}, ignore_index=True)

        print("Got these many results:", df.shape)

df.to_csv("ai.csv", index=False)
    
    '''
