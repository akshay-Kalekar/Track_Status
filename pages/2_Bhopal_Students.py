import streamlit as st
import pandas as pd

# Set up the page configuration with title, icon, and wide layout
st.set_page_config(page_title="Filter Records", page_icon="🎓", layout="wide")

# Title of the app
st.title("🎓 List of Enrolled Students")


# Read the CSV file with brnach
# df = pd.read_csv('./data/22.csv', na_filter=False)
# Read the CSV file
df = pd.read_csv('./BTechData2.csv', na_filter=False)

# Display the full dataframe with hidden index
st.dataframe(df, use_container_width=True, hide_index=True)

