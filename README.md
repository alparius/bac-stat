# bac-stat

Statistics from the *Romanian Baccalaureate* results for a *Data Literacy* course project.


## Instructions
In general, the first step of reproducing any part of the scripts assumes a recent version of Python being available. The used dependencies can then be installed with `pip install -r requirements.txt` after entering the `src` directory.

## The data

The underlying dataset was acquired from the [official site of the examination](http://static.bacalaureat.edu.ro). Only the last three years (2019, 2020, 2021) were available, the results from before (2004-2018) were removed from the site since those were not anonymised.

The data was scraped using Selenium, static scraping methods didn't prove to be successful due to the included JavaScript in several of the table's cells. The scraping itself turned out to be times of magnitudes slower than expected, so the script was extended to save data to file in smaller batches and to always check for already collected batches. Even though this way it was possible to run multiple instances of the script (around 5-10), all in all obtaining the full dataset still took two full days' time.

The batches were combined into single `.csv` files for each year and they can be found in the `data` directory.

Reproducing the scraping process requires one additional dependency: the Chrome browser and a matching version of the [Chrome WebDriver](https://chromedriver.chromium.org/downloads) downloaded to a location specified in the 19th line of the `src/scrape/scrape_main.py` file. Then the aforementioned file should be executable.
