import streamlit as st

def predict_genre(plot):
    plot = plot.lower()

    if "love" in plot or "romance" in plot:
        return ["Romance"]
    elif "fight" in plot or "war" in plot:
        return ["Action"]
    elif "ghost" in plot or "haunted" in plot:
        return ["Horror"]
    elif "funny" in plot or "laugh" in plot:
        return ["Comedy"]
    elif "detective" in plot or "murder" in plot:
        return ["Thriller"]
    else:
        return ["Drama"]

st.title("🎬 Movie Genre Predictor")

plot = st.text_area("Enter a movie plot:")

if st.button("Predict Genre"):
    if plot.strip():
        genres = predict_genre(plot)
        st.success("Predicted Genre: " + ", ".join(genres))
    else:
        st.warning("Please enter a movie plot.")