import streamlit as st
from query_data import query_rag

st.title("Document Query Application")

query_text = st.text_input("Enter your query:")

if st.button("Submit"):
    if query_text:
        try:
            response = query_rag(query_text)
            st.write("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error processing query: {e}")
    else:
        st.write("Please enter a query.")
