import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title("Student Record Analysis")

# App description
st.write("Note: The data may contain inaccuracies.")

# App functionality details
st.write("""
This app is designed to ease the extraction of Bhopal students' names from a long list of registration numbers. 
Simply copy and paste the entire column of registration numbers, and the app will filter out the relevant Bhopal student records.
""")

# Branch-wise assumptions for registration numbers
st.write("""
We assume student IDs follow this branch-wise structure:
- 0000-1000 & 2001-4000: Vellore
- 1001-2000 & 4001-7000: Chennai
- 7001-10000: Amravati
- 10001 onwards: Bhopal
""")
