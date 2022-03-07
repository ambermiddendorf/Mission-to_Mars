
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
import time

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)
    hemispheres = full_images(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_paragraph = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None

    return news_title, news_paragraph

# ### Featured Images

# Visit URL
def featured_image(browser):
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

def mars_facts():
    try:
    # use 'read_html' to scrape the facts table into a dataframe    
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None    

    # Assign columns and set index of dataframe     
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def full_images(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

# 2. Create a list to hold the images and titles.
    hemispheres=[]

# 3. Write code to retrieve the image urls and titles for each hemisphere.
    for n in range(4):
        image_link = browser.find_by_tag('h3')[n]
        image_link.click()
        time.sleep(2)
        html = browser.html
        img_soup = soup(html, "html.parser")
        d_img = img_soup.find(class_='container')
        full_img=d_img.find_all('li')[0]
        full_img_url=full_img.find(href=True).get('href')
        title = img_soup.find(class_='title').getText()
        hemispheres.append({'title': title, 'img_url':url+full_img_url})
        browser.back()   

# 4. Print the list that holds the dictionary of each image url and title.   
    return hemispheres

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

