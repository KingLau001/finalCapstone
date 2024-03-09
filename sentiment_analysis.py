#import the files
import pandas as pd
import spacy
from textblob import TextBlob
nlp =spacy.load('en_core_web_sm')

#path to the CSV file and read it 
filePath = 'amazon_product_reviews.csv'
df = pd.read_csv(filePath)
# Select the 'review.text' column
reviews_data = df['reviews.text']
#clense the missing values or reviews
clean_data = reviews_data.dropna()
#create a list for the cleans data to go into
review_list= []

#remove stopwords
for review in clean_data[0:20]: #change "clean_data" to "clean_data[XX:XX]" for min max values
    nlp_review = nlp(review)
    filteredText = " ".join(token.text for token in nlp_review if not token.is_stop)
    review_list.append(filteredText)

#create the function to find sentiment
def analyze_sentiment(review):
    # create a TextBlob object
    blob = TextBlob(review)
    # get the polarity score (where -1 is very negative, 0 is neutral, and 1 is very positive)
    polarity = blob.sentiment.polarity
    # determine sentiment label based on the polarity score
    if polarity > 0:
        sentiment_label = "Positive"
    elif polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    # return both the sentiment label and the polarity score
    return sentiment_label, polarity

# loop the list into the function to find the sentiment score
for list in review_list:
    sentiment_label, sentiment_score = analyze_sentiment(list)
    print("Review Sentiment:", sentiment_label, sentiment_score)
