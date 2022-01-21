import pandas as pd


def scrape_page_range(driver, year, page_start, page_end):
    """
    Scrape the BAC results of a year from the official website.
    :param driver: initialized ChromeDriver object
    :param year: string of the year to scrape (currently: 2019, 2020, 2021)
    :param page_start: first page to scrape in this run
    :param page_end: last page to scrape in this run
    :return: a pandas dataframe of the scraped data
    """
    url = 'http://static.bacalaureat.edu.ro/YEAR/rapoarte/rezultate/alfabetic/page_PAGENR.html'
    url = url.replace('YEAR', year)

    scraped_list = []
    for page_nr in range(page_start, page_end + 1):
        driver.get(url.replace('PAGENR', str(page_nr)))

        # progress tracker
        if page_nr % 10 == 0:
            print(year + ", page: " + str(page_nr))

        for i in range(3, 22, 2):
            student = []

            # student id
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[2]").text)
            # rank in county
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[3]").text)
            # rank in country
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[4]").text)
            # high school and city
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[5]").text)
            # county abbr.
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[6]").text)
            # is the student from a previous promotion
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[7]").text)
            # school type
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[8]").text)
            # student's specialization
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[9]").text)

            # romanian - competency level
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[10]").text)
            # romanian - grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[11]").text)
            # romanian - appeal on the written exam grade
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[12]").text)
            # romanian - final grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[13]").text)

            # mother tongue
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[14]").text)
            # mother tongue - competency level
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[1]").text)
            # mother tongue - grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[2]").text)
            # mother tongue - appeal on the written exam grade
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[3]").text)
            # mother tongue - final grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[4]").text)

            # studied modern language
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[15]").text)
            # studied modern language - qualifications
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[16]").text)

            # mandatory subject of the specialization
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[17]").text)
            # spec - grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[5]").text)
            # spec - appeal on the written exam grade
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[6]").text)
            # spec - final grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[7]").text)

            # elective subject of the specialization
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[18]").text)
            # elective - grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[8]").text)
            # elective - appeal on the written exam grade
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[9]").text)
            # elective - final grade on the written exam
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i + 1) + "]/td[10]").text)

            # digital competencies
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[19]").text)

            # overall final grade
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[20]").text)
            # successful or not
            student.append(driver.find_element_by_xpath("//*[@id='mainTable']/tbody/tr[" + str(i) + "]/td[21]").text)

            scraped_list.append(student)

    df = pd.DataFrame(scraped_list, columns=[
        'id',
        'county_rank',
        'country_rank',
        'high_school',
        'county',
        'prev_promotion',
        'school_type',
        'specialization',
        'romanian_competency',
        'romanian_written',
        'romana_written_appeal',
        'romana_written_final',
        'mother_tongue',
        'mother_tongue_competency',
        'mother_tongue_written',
        'mother_tongue_written_appeal',
        'mother_tongue_written_final',
        'modern_language',
        'modern_language_results',
        'mandatory_subject',
        'mandatory_subject_written',
        'mandatory_subject_written_appeal',
        'mandatory_subject_written_final',
        'elective_subject',
        'elective_subject_written',
        'elective_subject_written_appeal',
        'elective_subject_written_final',
        'digital_competencies',
        'final_grade',
        'successful'
    ])

    return df
