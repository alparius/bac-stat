# bac-stat

Statistics from the *Romanian Baccalaureate* results for a *Data Literacy* course project.


Repository structure:
- `data` contains zip archives of the scraped dataset
- `experiments` holds the experiments' Jupyter notebooks and the generated plots
- `paper` is for the final PDF and for the LaTeX project
- `scrape` contains the data scraping script

## Instructions

In general, the first step of reproducing any part of the scripts assumes a recent version of Python being available.
- For steps of executing the scraping script, read below.
- For the dependencies of the experiments, a default Jupyter environment is required, the rest of the unusual dependencies (`tueplots`, `geopandas`) can be handled within the notebooks.


## The data

The underlying dataset was acquired from the [official site of the examination](http://static.bacalaureat.edu.ro). Only the last three years (2019, 2020, 2021) were available, the results from before (2004-2018) were removed from the site since those were not anonymised.

The data was scraped using Selenium, which turned out to be times of magnitudes slower than expected, so the script was extended to save data to file in smaller batches and to always check for already collected batches. These batches were combined into single `.csv` files for each year and they can be found in the `data` directory.

The used dependencies can then be installed with `pip install -r requirements.txt` after entering the `scrape` directory.

Reproducing the scraping process requires one additional dependency: the Chrome browser and a matching version of the [Chrome WebDriver](https://chromedriver.chromium.org/downloads) downloaded to a location specified in the 19th line of the `scrape/scrape_main.py` file. Then the aforementioned file should be executable.
