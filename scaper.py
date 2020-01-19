# Scrapes springfieldspringfield for all the tv scripts for a given show

from bs4 import BeautifulSoup
import requests
import csv

BASE_URL = "https://www.springfieldspringfield.co.uk/"
TV_SHOW = "phineas-and-ferb"

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
    # Replace with the tv show you want to generate the word cloud for
    url = "https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=phineas-and-ferb"

    soup = get_beautiful_soup(url)
    if soup is None:
        sys.exit()

    # Get episodes
    links = get_links(soup)

    # Open file
    with open(TV_SHOW + '-scripts.csv', mode='w') as script_file:
        script_writer = csv.writer(script_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for link in links:
            print("Scraping url: '{}'".format(link))
            script = scrape_page(link)
            script_writer.writerow([script])

if __name__ == "__main__": 
    main()    
