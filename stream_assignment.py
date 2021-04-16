import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
st.title('Mood Detector')
import emoji
import pyjokes

def print_sentiment_scores(sentence):
    mood = ''
    analyser = SentimentIntensityAnalyzer()
    snt = analyser.polarity_scores(sentence)

    for key in snt:
        if snt[key] >= 0.5:
            mood = key
    if mood == "neg":
        st.write(emoji.emojize(":pensive_face:"))

        st.write("Don't wory next day will be fine to cheer you up I have something for you")
        st.write(pyjokes.get_joke())

    elif mood == "neu":
        st.write(emoji.emojize(":smiling_face_with_smiling_eyes:"))
        st.write("Okay Best of luck for tommorow")
        st.write(pyjokes.get_joke())
    elif mood == "pos" or mood == "compound":
        st.write(emoji.emojize(":smiling_face_with_heart-eyes:"))
        st.write("Good to hear that")
    st.write(snt)
sentence=st.text_input('How Was your day?...')
print_sentiment_scores(sentence)