# Track Status

## Overview
**Track Status** is a Streamlit-based web application designed to facilitate student record analysis and placement data overview. The app helps extract student names from a large list of registration numbers, filter them by campus, and display placement statistics, including company-wise placement counts and package categorization.

## Features
- **Campus-wise Record Filtering**: Extract and filter student records based on their campus (Bhopal, Vellore, Chennai, Amravati).
- **Company-wise Placement Data**: Display the number of students placed in each company.
- **Package Type Categorization**: Categorize students by the type of package they received, if available in the dataset.
- **Real-time Data Display**: Interact with data tables for student records, company placement, and package categorization.

## Branch-Wise Assumptions
The application assumes the following branch-wise structure for student registration numbers:
- `0000-1000` & `2001-4000`: Vellore
- `1001-2000` & `4001-7000`: Chennai
- `7001-10000`: Amravati
- `10001 onwards`: Bhopal

## Installation
To install and run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/track-status.git
   cd track-status

2. **Install the required Python packages**
    ```bash
    pip install streamlit pandas

3. **Run the application**
    ```bash
    streamlit run app.py

4. **View the app**
    Open a browser and navigate to http://localhost:8501 to interact with the app