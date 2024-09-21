import streamlit as st
import pandas as pd

# Set up the page configuration with title, icon, and wide layout
st.set_page_config(page_title="Filter Records", page_icon="🙀", layout="wide")

# Title of the app
st.title("🎓 List of Enrolled Students")

# Read the CSV file
df = pd.read_csv('./data/22.csv', na_filter=False)

# Display the full dataframe with hidden index
st.dataframe(df, use_container_width=True, hide_index=True)


# Get user input for search terms
st.subheader("Bhopal Student List & Other Branches College Count")
getRecords = st.text_input(label="Enter the records to find (space-separated) e.g., 21BCEXXXXX 21BAIYYYYYY ...")

# A button to trigger an action 
search = st.button('Search', type="primary")
# Process the search terms
if getRecords or search:
    search_terms = getRecords.split(' ')  # Split by space
    search_terms = [term.strip() for term in search_terms if term.strip()]  # Remove extra spaces

    # Classify search terms based on specific patterns
    search_terms_vel = [term for term in search_terms if len(term) == 9 and term[5] in '023']  # Vellore
    search_terms_che = [term for term in search_terms if len(term) == 9 and term[5] in '1456']  # Chennai
    search_terms_ap = [term for term in search_terms if len(term) == 9 and term[5] in '987']  # Amravati
    search_terms_bp = [term for term in search_terms if len(term) == 10]  # Bhopal

    # Display the search terms entered for verification
    st.subheader("Entered Search Terms")
    st.write("Search Terms: ", search_terms)

    # Specify the column to search in the DataFrame
    columns_to_search = ['Reg No']  # Ensure the column matches your CSV data

    # Filter the DataFrame based on Bhopal (10-character terms)
    if search_terms_bp:
        filtered_df_bp = df[df[columns_to_search].apply(lambda row: any(term in row.astype(str).values for term in search_terms_bp), axis=1)]
        st.subheader("Bhopal Shortlisted Records")
        st.dataframe(filtered_df_bp, use_container_width=True, hide_index=True)
        st.write(f"Total shortlisted from Bhopal: **{len(filtered_df_bp)}**")

    # Display counts for Vellore, Chennai, and Amravati
    if search_terms_ap:
        st.write(f"Total shortlisted from Amravati: **{len(search_terms_ap)}**")

    if search_terms_vel:
        st.write(f"Total shortlisted from Vellore: **{len(search_terms_vel)}**")

    if search_terms_che:
        st.write(f"Total shortlisted from Chennai: **{len(search_terms_che)}**")

    # Prompt if no search terms were found
    if not search_terms_bp and not search_terms_ap and not search_terms_vel and not search_terms_che:
        st.warning("⚠️ Please enter valid records to find.")
