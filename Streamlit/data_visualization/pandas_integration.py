# Pandas is a tool for working with data in Python. It helps you organize and analyze data in tables called DataFrames.

# Basic Pandas Operations


# Creating a DataFrame: Think of this as making a table from scratch.
import streamlit as st
import pandas as pd

# Creating a simple DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Claire'],
    'Age': [24, 27, 22, 32],
    'Salary': [50000, 54000, 58000, 62000]
}
df = pd.DataFrame(data)
st.write(df)


# Viewing Data: You can view the first few rows of your table with head().

# print(df.head())

# Filtering Data: You can filter rows based on conditions.
filtered_df = df[df['Age'] > 25]

st.write(filtered_df)


# Adding Columns: You can create new columns.
df['Bonus'] = df['Salary'] * 0.1
st.write(df)


#line chart

# Sample DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Show the DataFrame
st.title('Sales Data')
st.dataframe(df)

# Show a line chart
st.write("Sales over time:")
st.line_chart(df.set_index('Month')['Sales'])

st.bar_chart(df.set_index('Month')['Sales'])

st.area_chart(df.set_index('Month')['Sales'])


# Uploading Files:

file = st.file_uploader("Upload your CSV file", type="csv")
if file is not None:
    df = pd.read_csv(file)

    st.write(df)
    