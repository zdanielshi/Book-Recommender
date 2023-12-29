# Importing libraries
import streamlit as st
from openai import OpenAI

# Access the API key from Streamlit secrets
api_key = st.secrets["api_key"]

# Initialize OpenAI client with the API key
client = OpenAI(api_key = api_key)

# Create the Streamlit interface
st.title("Book Recommender")

user_input = st.text_area("Enter a list of your favorite books")

# Function to get book recommendations
def get_recommendations(user_books):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {
        "role": "system",
        "content": "You are an excellent assistant who helps with book recommendations"
      },
      {
        "role": "user",
        "content": "Below are a list of books that I really like. Give me recommendations for more books."
      },
      {
        "role": "user",
        "content": user_input
      },
      {
        "role": "user",
        "content": """
              When responding, give me a list of responses exactly as the following. 
              Give me exactly 5 book recommendations. None should repeat the recommendations 
              Example:
              - "Book Title 1" by Author
              - "Book Title 2" by Author
              - "Book Title 3" by Author
              - "Book Title 4" by Author
              - "Book Title 5" by Author
              """
      },
    ],
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0
  )
  return response.choices[0].message.content

# Button to trigger the recommendation query
if st.button ("Get recommendations"):
  with st.spinner ("Fetching recommendations..."):
    recommendations = get_recommendations(user_input)
    st.success('Recommendations:')
    st.write(recommendations)