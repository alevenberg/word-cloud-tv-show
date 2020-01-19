# word-cloud-tv-show

## Outline 
- [Scrape data](./scraper.py)
- [Clean the data](./clean_data.py)
- [Generate the word cloud](./word_cloud.py)

## How to use

1. Set up and activate your environment and install the requirements according to the environment.yml
    - If using anaconda, can use the command `conda env create -f environment.yml`
2. Run the script 
    * `run.sh tv-show-name`
      - Make sure there exists a link to the given tv show on https://www.springfieldspringfield.co.uk/ 
      - Optionally, put an image named tv-show-name-mask.png into the directory ./tv-show-name to create a masked word cloud
    * Make sure to give execute permissions: `chmod 755` 
  
## Example

When you run, `./run.sh phineas-and-ferb`, the following is generated 

A masked word cloud image:

![mask image](https://github.com/alevenberg/word-cloud-tv-show/blob/master/phineas-and-ferb/mask_word_cloud.png)

Word cloud:

![word cloud image](https://github.com/alevenberg/word-cloud-tv-show/blob/master/phineas-and-ferb/word_cloud.png)
