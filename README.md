# Mission-to_Mars
Module 10 - Web scraping, MongoDB, Beautiful Soup, Splinter

## Overview
In the module we created code to scrape items from a few websites to compile a new Mars website to impress NASA. In the challenge we added new images of Mars' surface to our scraping.py and our FLASK_APP website.

## Method
To scrape the full resolution images from the Mars Hemisperes website, I wrote a for loop to click on each image link to get to get to the page where I could find the address for the full size image. In the scrape_all() function of my scraping.py, I added in this new code and added the list of dictionaries to the data dictionary for our MongoDB.

## Website
I then added those images to the website and made Bootstrap styling edits to the button, images, and Mars New headline. I also ensured that the website was mobile responsive by adjusting the column settings to xs sizing.


