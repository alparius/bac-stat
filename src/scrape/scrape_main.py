from selenium import webdriver
import os.path

from src.scrape.scrape_page_range import scrape_page_range


###
# ChromeDriver setup for Selenium

options = webdriver.ChromeOptions()
options.add_argument('--lang=en')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument('--incognito')

CHROME_DRIVER_PATH = 'C:\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)


###
# scraping

nr_pages = {
    '2019': 13610,
    '2020': 15565,
    '2021': 13367
}
batch_size = 200
folder = '..//..//data//'

for year in nr_pages.keys():
    for i in range(1, nr_pages[year], batch_size):
        last_page = min(nr_pages[year], i + batch_size - 1)
        filepath = folder + 'bac-results-' + year + '-pages-' + str(i) + '-' + str(last_page) + '.csv'
        if os.path.isfile(filepath):
            continue
        else:
            bac_results = scrape_page_range(driver, year, i, last_page)
            bac_results.to_csv(filepath)

driver.close()
