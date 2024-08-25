
# ### 1. Simple Form Submission App


#    - **Widgets to Practice**: `st.text_input()`, `st.number_input()`, `st.radio()`,
#      `st.checkbox()`, `st.button()`

#    - **Task**: 
#      - Create a simple registration form with fields like Name, Age, Gender, Email, and a checkbox for 
#        agreeing to terms and conditions.
#      - Once the form is submitted by clicking a button, display the user's information below the form.
#    - **Bonus**: Add basic validation (e.g., mandatory fields).


import streamlit as st

#App Title
st.title("Simple Form Submission App")

# User Enter his name  
name = st.text_input("Enter Your Name" )

# User Enter his age  
age = st.number_input("Enter Your Age" , max_value=100 , min_value=18)

# User Choose his Gender  
gender = st.radio("Choose Your Gender" , ("Male" , "Female" , "Other"))

# User Enter his Email  
email = st.text_input("Enter Your Email")

# Checkbox for agreeing to terms and conditions
agree = st.checkbox("I agree to the terms and conditions")

#Submit Button

button = st.button("Submit Information")

if button:
    st.write("Name : "  ,name)
    st.write("Age : " ,age)
    st.write("Gender: " ,gender)
    st.write("Email : " ,email)
else:
        st.warning("Please fill all fields and agree to the terms and conditions.")    




# ------------------------------------------------------------------------------------------------------



# ### Practice Questions
# 1. Create a form to collect user feedback on a product. 
# Include fields for text input (feedback), rating (slider), and a submit button.


feedback = st.text_input("Kindly give your feeddback")
rating = st.slider("Give rating" , max_value=5 , min_value=0)
button =st.button("Submit")

if button:
    st.write("Thankyou For Your Feedback" , feedback)
    st.write("Thankyou For Your Rating" , rating)



# 2. Design a widget where users can choose a date and time for an event and display it on submission.


date = st.date_input("Select Date")
time = st.time_input("Select Time")
if date:
    st.write("Date:", date)
    st.write("time:", time)



# 3. Build a form for uploading a CSV file and display its contents in a table format after the upload.

import pandas as pd

st.title("CSV File Uploader")

# File uploader widget for uploading CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the contents of the CSV file
    st.write("Here are the contents of the file:")
    st.dataframe(df)
else:
    st.write("Please upload a CSV file to display its contents.")



# Create an app where users can choose their favorite fruit from a multiselect and
# display the selected fruits in a sentence.



# App title
st.title("Favorite Fruit Selector")

# List of fruits to choose from
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grapes', 'Mango', 'Pineapple']

# Multiselect widget for users to choose their favorite fruits
selected_fruits = st.multiselect("Select your favorite fruits", fruits)

# Display the selected fruits in a sentence
if selected_fruits:
    st.write(f"You selected: {', '.join(selected_fruits)}.")
else:
    st.write("Please select at least one fruit.")
