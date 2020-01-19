
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image
import string 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def generate_cloud(words):
    wc = WordCloud(width=480, height=480, margin=0)
    wc.generate(words)
    wc.to_file('word_cloud.png')

    # Plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    # To view the figure
    plt.show() 

def generate_mask_word_cloud(words, mask):
    char_mask = np.array(Image.open(mask, 'r').convert('RGB')) 
   
    wc = WordCloud(background_color="white", width=400, height=400, mask=char_mask)
    wc.generate(words)
    wc.to_file('mask_word_cloud.png')

    # plt.imshow(wc.recolor(color_func=image_colors))
    # plt.show() 

def main():
    # Replace with correct file name 
    file_name = "phineas-and-ferb-scripts.txt"

    file = open(file_name,"r")
    
    words = file.readline()

    # generate_cloud(words)

    mask_file = "phineas-mask.jpg"
    generate_mask_word_cloud(words, mask_file)

if __name__ == "__main__": 
    main()    
