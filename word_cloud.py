
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import string 

def read_file_and_clean_data(file_name):
    df = pd.read_csv(file_name) 

    # Clean data
    words = []
    # Iterate through the csv file 
    for row in df.iterrows(): 
        line = (row[1]).to_string()

        # Remove carriage return
        line = line.replace('\\r', '') 

        # Split the words for each row 
        tokens = line.split(" ") 
        
        # Converts each token into lowercase 
        tokens = list(map(lambda x: x.lower(), tokens))

        # Remove punctuation
        tokens = list(map(lambda x: x.rstrip(string.punctuation).lstrip(string.punctuation), tokens))

        # Remove empty strings
        tokens = list(filter(None, tokens)) 

        tokens = list(map(lambda x: x.rstrip(string.punctuation).lstrip(string.punctuation), tokens))

        words.extend(tokens)

    return words

def generate_cloud(words):
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(" ".join(words))

    # Plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.show() 

def main():
    # Replace with correct file name 
    file_name = "phineas-and-ferb-scripts.csv"

    words = read_file_and_clean_data(file_name)
  
    # Generate word cloud
    generate_cloud(words)

if __name__ == "__main__": 
    main()    
