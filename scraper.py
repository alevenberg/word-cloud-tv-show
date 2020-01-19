# Scrapes springfieldspringfield for all the tv scripts for a given show

from bs4 import BeautifulSoup
import requests
import csv
import sys
import progressbar

BASE_URL = "https://www.springfieldspringfield.co.uk/"

def get_beautiful_soup(url):
    """ Gets a beautiful soup object for the given url """
    # Connect to page
    try: 
        page = requests.get(url)
    except requests.exceptions.ConnectionError: 
        print("Unable to connect to url '{}'".format(url))
        return None

    if (page is None):
        print("Unable to connect to url '{}'".format(url))
        return None
    
    soup = BeautifulSoup(page.text, "lxml")
    return soup

def get_links(soup):
    """ Returns a list of the links for each episode for a given tv show """
    links = []
    episodes = soup.findAll('a',attrs={'class':'season-episode-title'})
    for episode in episodes:
        links.append(BASE_URL + episode['href'])
    return links

def scrape_page(url):
    """ Scrapes a single page and return the text as a str"""
    soup = get_beautiful_soup(url)
    if soup is None:
        sys.exit()

    script = soup.find('div', {'class':'scrolling-script-container'})
    script_text = script.text.strip()

    return script_text

def main():
    if len(sys.argv) < 2:
        print("Usage: scraper.py tv-show-name")
        sys.exit()

    tv_show = sys.argv[1]
    url = BASE_URL + "episode_scripts.php?tv-show=" + tv_show
    print("Scraping url: {}".format(url))

    soup = get_beautiful_soup(url)
    if soup is None:
        sys.exit()

    # Get episodes
    links = get_links(soup)

    # Open file
    with open("./" + tv_show + "/" + tv_show + '-scripts.csv', mode='w') as script_file:
        script_writer = csv.writer(script_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        bar = progressbar.ProgressBar(maxval=len(links)).start()

        for i, link in enumerate(links):
            script = scrape_page(link)
            script_writer.writerow([script])
            bar.update(i)

if __name__ == "__main__": 
    main()    
