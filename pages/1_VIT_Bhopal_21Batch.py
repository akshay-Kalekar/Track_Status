import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
# Title of the Streamlit app
st.title("List of Enrolled Students")

# Read the CSV file
df = pd.read_csv('./BTechData2.csv', na_filter=False)
st.dataframe(df,width=10000,hide_index=True)

# Get user input
getRecords = st.text_input(label="Enter the records to find (space-separated) eg. 21BCEXXXXX 21BAIYYYYYY ...")
search_terms = getRecords.split(' ')  # Split by space

# Trim whitespace from search terms
search_terms_vel = [term.strip() for term in search_terms if term.strip() and len(term)==9 and term[5] in '023' ]
search_terms_che = [term.strip() for term in search_terms if term.strip() and len(term)==9 and term[5] in '1456' ]
search_terms_ap = [term.strip() for term in search_terms if term.strip() and len(term)==9 and term[5] in '987' ]
search_terms_bp = [term.strip() for term in search_terms if term.strip() and len(term)==10]
st.dataframe(search_terms,use_container_width=True,hide_index=True)

# Specify the columns to search
columns_to_search = ['Reg No']  # Replace with your specific column names

# Check if search_terms is not empty

if search_terms_bp :

    # Filter the DataFrame for matching records in specified columns
    filtered_df = df[df[columns_to_search].apply(lambda row: any(term in row.astype(str).values for term in search_terms_bp), axis=1)]

    # Display the filtered DataFrame
    st.dataframe(filtered_df,use_container_width=True)
    st.write("No of Shortlisted from Bhopal : ", len(filtered_df))

if search_terms_ap :
    st.write("No of shortlisted from Amravati : ",len(search_terms_ap))
    
if search_terms_vel :
    st.write("No of shortlisted from Vellore : ",len(search_terms_vel))
    
if search_terms_che :
    st.write("No of shortlisted from Chennai : ",len(search_terms_che))
elif not search_terms_bp and not search_terms_ap  :
    st.write("Please enter records to find.")
