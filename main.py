import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

# Streamlit web application
# Streamlit web application
def main():
    st.title("N-gram Generator")

    # Input text
    text_input = st.text_area("Enter your text here:")

    # Select n for n-grams
    n_value = st.slider("Select the value of n for n-grams", 2, 5, 2)

    if st.button("Generate N-grams"):
        if text_input:
            n_grams = generate_ngrams(text_input, n_value)
            total_ngrams = len(n_grams)
            st.write(f"Total {n_value}-grams: {total_ngrams}")
            st.write(f"{n_value}-grams:")
            st.write(n_grams)

            
        else:
            st.warning("Please enter a text passage.")

if __name__ == "__main__":
    main()

