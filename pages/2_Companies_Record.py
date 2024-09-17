import streamlit as st
import pandas as pd

# Set up the page configuration with a title, icon, and wide layout
st.set_page_config(page_title="Companies Records", page_icon="🐱", layout="wide")

# Load the CSV file
df = pd.read_csv('./BTechData2.csv', na_filter=False)

# Add a main header for the app
st.title("📊 Company-wise Placement Records")

# Section to display company placement counts
st.subheader("Company-wise Placement Counts")

# Count the number of students placed per company
companies = {}
for row in df['Companies']:
    row = row.capitalize().strip()
    if row:
        companies[row] = companies.get(row, 0) + 1

# Create a DataFrame from the company counts
company_df = pd.DataFrame(list(companies.items()), columns=['Company Name', 'Placed Counts'])

# Add a description to the table
st.write("The table below shows the number of students placed in each company:")

# Display the company placement data in a table
st.dataframe(company_df, use_container_width=True)

# Check if the 'C_Type' column exists and display package type counts
if 'C_Type' in df.columns:
    st.subheader("🎁 Package Type Distribution")
    
    package_type = {}
    for row in df['C_Type']:
        row = row.capitalize().strip()
        if row:
            package_type[row] = package_type.get(row, 0) + 1

    # Create a DataFrame from the package type counts
    package_type_df = pd.DataFrame(list(package_type.items()), columns=['Package Type', 'Counts'])
    
    # Add a description to the package type table
    st.write("Here is the distribution of package types offered to students:")
    
    # Display the package type data in a table
    st.dataframe(package_type_df, use_container_width=True)
else:
    st.warning("Column 'C_Type' not found in the dataset.")


