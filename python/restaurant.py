import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load dataset
df = pd.read_csv(r"data.csv")

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# Function to detect sentiment
def get_sentiment(text):

    text = str(text)

    score = analyzer.polarity_scores(text)['compound']

    if score >= 0.05:
        return "Positive"

    elif score <= -0.05:
        return "Negative"

    else:
        return "Neutral"


# Create sentiment column
df['sentiment'] = df['clean_review'].apply(get_sentiment)


# Function to categorize reviews
def categorize_review(text):

    text = str(text).lower()

    # Food Quality Issues
    if any(word in text for word in [
        'watery',
        'cold',
        'stale',
        'raw',
        'bad taste',
        'tasteless',
        'burnt'
    ]):
        return 'Food Quality'

    # Staff Behaviour Problems
    elif any(word in text for word in [
        'rude',
        'staff',
        'behaviour',
        'manager'
    ]):
        return 'Staff Behaviour'

    # Delivery Related Issues
    elif any(word in text for word in [
        'late',
        'delay',
        'slow',
        'waiting'
    ]):
        return 'Delivery Delay'

    # Hygiene Issues
    elif any(word in text for word in [
        'dirty',
        'hair',
        'smell',
        'unclean'
    ]):
        return 'Hygiene'

    # Price Complaints
    elif any(word in text for word in [
        'expensive',
        'costly',
        'overpriced'
    ]):
        return 'Pricing'

    # Positive Experience
    elif any(word in text for word in [
        'delicious',
        'amazing',
        'tasty',
        'good',
        'best'
    ]):
        return 'Positive Experience'

    else:
        return 'Other'


# Create category column
df['category'] = df['clean_review'].apply(categorize_review)


# Check missing ratings
print("Missing Ratings Before Filling:")
print(df['Overall_Rating'].isnull().sum())


# Function to predict missing ratings
def predict_rating(sentiment, review):

    review = str(review).lower()

    positive_words = [
        'amazing',
        'excellent',
        'best',
        'awesome',
        'delicious',
        'love'
    ]

    negative_words = [
        'worst',
        'bad',
        'rude',
        'dirty',
        'waste',
        'terrible'
    ]

    # Count positive and negative words
    pos_count = sum(word in review for word in positive_words)
    neg_count = sum(word in review for word in negative_words)

    # Positive Reviews
    if sentiment == 'Positive':

        if pos_count >= 2:
            return 5
        else:
            return 4

    # Negative Reviews
    elif sentiment == 'Negative':

        if neg_count >= 2:
            return 1
        else:
            return 2

    # Neutral Reviews
    else:
        return 3


# Fill ONLY missing ratings
df.loc[df['Overall_Rating'].isnull(), 'Overall_Rating'] = df.apply(
    lambda row: predict_rating(
        row['sentiment'],
        row['clean_review']
    ),
    axis=1
)


# Check updated results
print("\nSample Output:")
print(df[['clean_review', 'sentiment', 'Overall_Rating']].head(50))


# Save final cleaned dataset
df.to_csv(
    "restaurant_reviews_final.csv",
    index=False,
    encoding='utf-8-sig'
)

print("\nFinal Dataset Saved Successfully")