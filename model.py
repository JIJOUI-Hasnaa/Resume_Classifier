from sklearn.feature_extraction.text import TfidfVectorizer
import re
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
df=pd.read_csv(r"C:\Users\Pc\Downloads\dataset_cv1\Resume\Resume.csv")

#cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text) #delete numbers
    text = re.sub(r'[^\w\s]', '', text) #delete punctuation
    return text
df["Resume_str"] = df["Resume_str"].apply(clean_text)

#separate data
X = df["Resume_str"]     
y=df["Category"]
#vectorisation
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

#model
model=LogisticRegression(max_iter=6000)
model.fit(X_train,y_train)
#prediction
y_pred = model.predict(X_test)

#model evaluation 
print("Accuracy:", accuracy_score(y_test, y_pred))

#save work
import joblib
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(model, "model.pkl")
