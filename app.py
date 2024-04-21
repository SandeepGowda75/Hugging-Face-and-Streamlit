pip install streamlit requests
import streamlit as st
import requests

# Set your API key here
API_KEY = "your_huggingface_api_key_here"

# Streamlit app title
st.title('Sentiment Analysis with Hugging Face API')

# Text area for user input
user_input = st.text_area("Enter text to analyze sentiment", "Type here...")

if st.button('Analyze'):
    # Prepare the request payload
    api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": user_input}

    # Make the request
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        # Get the result
        result = response.json()[0]
        st.write("Label:", result['label'])
        st.write("Confidence:", result['score'])
    else:
        st.write("Failed to get response")