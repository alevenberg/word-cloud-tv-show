
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image
import string 
from wordcloud import WordCloud, ImageColorGenerator
import sys 
from os import path

def generate_cloud(words, tv_show):
    wc = WordCloud(width=480, height=480, margin=0)
    wc.generate(words)
    wc.to_file("./" + tv_show + "/" + tv_show + '-word-cloud.png')

    # Plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wc) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    # To view the figure
    # plt.show() 

def generate_mask_word_cloud(words, mask, tv_show):
    char_mask = np.array(Image.open(mask, 'r').convert('RGB')) 
   
    wc = WordCloud(background_color="white", width=400, height=400, mask=char_mask)
    wc.generate(words)
    wc.to_file("./" + tv_show + "/" + tv_show + '-mask-word-cloud.png')

def main():
    if len(sys.argv) < 2:
        print("Usage: word_cloud.py tv-show-name")
        sys.exit()

    tv_show = sys.argv[1]
    file_name = tv_show + "-scripts.txt"

    file = open("./" + tv_show + "/" + file_name,"r")
    
    words = file.readline()

    generate_cloud(words,tv_show)

    mask_file = tv_show + "-mask.png"
    mask_path = "./" + tv_show + "/" + mask_file
    if (path.exists(mask_path)):
        generate_mask_word_cloud(words, mask_path, tv_show)

if __name__ == "__main__": 
    main()    
