
from wordcloud import WordCloud, STOPWORDS 
import string 
import matplotlib.pyplot as plt 

def generate_cloud(words):
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(words)

    # Plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.savefig('word_cloud.png')

    # To view the figure
    plt.show() 

def main():
    # Replace with correct file name 
    file_name = "phineas-and-ferb-scripts.txt"

    file = open(file_name,"r")
    
    words = file.readline()

    generate_cloud(words)

if __name__ == "__main__": 
    main()    
