import time
import pandas as pd
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--lang=en")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
options.add_argument("--incognito")

driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=options)
driver.implicitly_wait(100)

URL = "http://static.bacalaureat.edu.ro/2021/rapoarte/rezultate/alfabetic/page_PAGENR.html"
scraped_list = []

for page_nr in range(1, 4):
    driver.get(URL.replace("PAGENR", str(page_nr)))

    for i in range(3, 22, 2):
        student = []

        id = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[2]")
        student.append(id.text)

        county_rank = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[3]")
        student.append(county_rank.text)

        country_rank = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[4]")
        student.append(country_rank.text)

        high_school = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[5]")
        student.append(high_school.text)

        county = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[6]")
        student.append(county.text)

        prev_promotion = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[7]")
        student.append(prev_promotion.text)

        school_type = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[8]")
        student.append(school_type.text)

        specialization = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[9]")
        student.append(specialization.text)

        final_grade = driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[20]")
        student.append(final_grade.text)

        scraped_list.append(student)

driver.close()


df = pd.DataFrame(scraped_list, columns=[
    'id',
    'county_rank',
    'country_rank',
    'high_school',
    'county',
    'prev_promotion',
    'school_type',
    'specialization',
    'final_grade'
])

print(df.to_string())


