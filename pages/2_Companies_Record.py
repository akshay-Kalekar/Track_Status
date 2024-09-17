import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv('./BTechData2.csv', na_filter=False)

# Display company-wise placement counts
st.write("Company Placed and Student Counts")

# Count the number of students placed per company
companies = {}
for row in df['Companies']:
    row = row.capitalize().strip()
    if row:
        companies[row] = companies.get(row, 0) + 1

# Create a DataFrame from the company counts
company_df = pd.DataFrame(list(companies.items()), columns=['Company Name', 'Placed Counts'])

# Display the company placement data in a table
st.dataframe(company_df,width=10000,)

# Package type categorization (assuming there's a 'C_Type' column in your CSV)
if 'C_Type' in df.columns:
    st.write("Package Categorized")
    
    package_type = {}
    for row in df['C_Type']:
        row = row.capitalize().strip()
        if row:
            package_type[row] = package_type.get(row, 0) + 1

    # Create a DataFrame from the package type counts
    package_type_df = pd.DataFrame(list(package_type.items()), columns=['Package Type', 'Counts'])
    
    # Display the package type data in a table
    st.dataframe(package_type_df,width=10000,)
else:
    st.write("Column 'C_Type' not found in the dataset.")



