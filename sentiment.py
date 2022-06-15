from textblob import TextBlob


def perform_analysis(text):
    result = TextBlob(text=text)
    return result
