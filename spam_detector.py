
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = {
    'text': [
        'Win money now!!!',
        'Congratulations, you have won a prize',
        'Call me later',
        'Hello, how are you?',
        'Free entry in a contest',
        'Let’s meet tomorrow',
        'You have been selected for a reward',
        'Are you available today?',
        'Earn cash quickly',
        'See you at class'
    ],
    'label': [1,1,0,0,1,0,1,0,1,0]   
}

df = pd.DataFrame(data)

X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))

def predict_spam(text):
    text_vec = vectorizer.transform([text])
    result = model.predict(text_vec)

    if result[0] == 1:
        return "Spam"
    else:
        return "Not Spam"


while True:
    ui = input("\nEnter message (or type 'exit'): ")

    if user_input.lower() == 'exit':
        break

    print("Prediction:", predict_spam(ui))
