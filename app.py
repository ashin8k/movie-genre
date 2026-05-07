import streamlit as st
from transformers import pipeline

# Load model (runs once)
classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

labels = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance"]

def predict_genre(text):
    result = classifier(text, candidate_labels=labels)
    return result

# ---------------- UI ----------------

st.title("🎬 Movie Genre Predictor")
st.write("Enter a movie story and get predicted genres")

text = st.text_area("Movie Story")

if st.button("Predict Genre"):
    if text.strip() == "":
        st.warning("Please enter a movie story")
    else:
        result = predict_genre(text)

        st.subheader("Predicted Genres:")

        for label, score in zip(result["labels"][:3], result["scores"][:3]):
            st.write(f"{label}: {score:.2f}%")