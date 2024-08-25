# Import the required libraries
import streamlit as st
import requests
from urllib.parse import quote

# Define the endpoint of the FastAPI application
endpoint = "https://miguel5458-creator--example-fastapi-app-fastapi-app-dev.modal.run/process_url/"

# Set the title of the Streamlit application
st.title("URL Processor")

# Create a text input for the user to input their URL
data_url = st.text_input("Enter the URL you want to process:")

# Prepare the input data for the API request
if st.button("Process"):
    if data_url:
        # Encode the URL
        encoded_url = quote(data_url, safe='')

        # Construct the full endpoint URL with the encoded URL parameter
        full_url = f"{endpoint}?data_url={encoded_url}"

        # Send a request to the FastAPI application
        try:
            response = requests.get(full_url)
            response.raise_for_status()  # Ensure the request was successful
            res_json = response.json()
            
            # Display the results
            if res_json["status"] == "success":
                st.subheader("Processed Data")
                st.json(res_json["result"])
            else:
                st.error(f"Error: {res_json['message']}")
        except requests.RequestException as e:
            st.error(f"Error making request: {e}")
    else:
        st.warning("Please enter a URL.")