import streamlit as st
import joblib
import string


# ---------------------------------------------------
# Load trained files
# ---------------------------------------------------

model = joblib.load("emotion_model.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")
emotion_mapping = joblib.load("emotion_mapping.pkl")


# ---------------------------------------------------
# Text preprocessing
# ---------------------------------------------------

def remove_punc(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))


def remove_num(txt):
    new = ""

    for i in txt:
        if not i.isdigit():
            new += i

    return new


def remove_emojis(txt):
    new = ""

    for i in txt:
        if i.isascii():
            new += i

    return new


# ---------------------------------------------------
# Preprocess function
# ---------------------------------------------------

def preprocess_text(txt):

    # lowercase
    txt = txt.lower()

    # remove punctuation
    txt = remove_punc(txt)

    # remove numbers
    txt = remove_num(txt)

    # remove emojis
    txt = remove_emojis(txt)

    # remove stopwords
    words = txt.split()

    cleaned = []

    for word in words:
        if word not in stop_words:
            cleaned.append(word)

    return " ".join(cleaned)


# ---------------------------------------------------
# Stopwords
# ---------------------------------------------------

stop_words = joblib.load("stop_words.pkl")


# ---------------------------------------------------
# Streamlit UI
# ---------------------------------------------------

st.set_page_config(
    page_title="Emotion Prediction",
    page_icon="😊",
    layout="centered"
)


st.title("😊 Emotion Prediction")
st.write("Enter a sentence and the ML model will predict the emotion.")


# ---------------------------------------------------
# Text input
# ---------------------------------------------------

user_text = st.text_area(
    "Enter your text:",
    placeholder="Example: I am feeling very happy today!",
    height=150
)


# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if st.button("Predict Emotion"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")

    else:

        # preprocess text
        cleaned_text = preprocess_text(user_text)

        # convert text into TF-IDF
        text_tfidf = tfidf_vectorizer.transform([cleaned_text])

        # prediction
        prediction = model.predict(text_tfidf)[0]

        # convert number to emotion
        emotion = emotion_mapping[prediction]

        st.success(f"Predicted Emotion: **{emotion.upper()}**")