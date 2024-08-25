

# ### 1. **Text Input Widgets**

# - st.text_input(): Single-line text input.
# - st.text_area(): Multi-line text input.


import streamlit as st

text= st.text_input("Enter Your Name ")
st.write("You entered:", text)

textArea =st.text_area(''' Tell Me About Yourself''')
st.write("You entered:", textArea)


# -----------------------------------------------------------------------------------------------------------


# ### 2. **Number Input Widgets**


# - st.number_input(): Allows integer/float input with optional range.

number = st.number_input("Enter a number:", min_value=0, max_value=100)
st.write("You entered:", number)


# - st.slider(): A slider to select a number within a specified range.

age = st.slider("Select your age:", 0, 100, 25)
st.write("Your age is:", age)


# - st.select_slider(): Slider with custom options (e.g., colors or labels).

color = st.select_slider("Choose a color:", options=['Red', 'Green', 'Blue'])
st.write("You selected:", color)





#----------------------------------------------------------------------------------------------------------





# ### 3. **Date and Time Input Widgets**


# - st.date_input(): Date picker widget.Takes a date input from a calendar widget

selected_date = st.date_input("Select a date")
st.write("You selected:", selected_date)



# - st.time_input(): Time picker widget. Accepts a time input.

selected_time = st.time_input("Select a time")
st.write("You selected:", selected_time)



#---------------------------------------------------------------------------------------------------------

# ### 4. **Selection Widgets**
# - st.selectbox(): Dropdown with single option selection.

option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)



# - st.multiselect(): Allows multiple options to be selected.

options = st.multiselect("Select multiple options:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", options)


# - st.radio(): Radio buttons for single-choice selection.

gender = st.radio("Choose your gender:", ("Male", "Female", "Other"))
st.write("You selected:", gender)





#----------------------------------------------------------------------------------------------------------

# ### 5. **File Input Widget**
# - st.file_uploader(): Upload a file (supports multiple file types and multiple uploads).

uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "jpg"])
if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)


# image = st.file_uploader("Enter Your Image" , type = ["jpg" , "png", "jfif"] )

# audio = st.file_uploader("Enter Your Audio" , type = ["mp3", "wav"])

# video = st.file_uploader("Enter Your Video" , type = ["mp4" , "wmv"])



#--------------------------------------------------------------------------------------------------------



# ### 6. **Checkbox and Button Widgets**


# - st.checkbox(): Checkbox for boolean input (True/False).

agree = st.checkbox("I agree to the terms")
if agree:
    st.write("Thank you for agreeing!")



# - st.button(): Button that triggers an action when clicked.

if st.button("Click me"):
    st.write("Button clicked!")


#---------------------------------------------------------------------------------------------------


# ### 7. **Password Input**
# - st.text_input(type="password"): Hides the input text (for passwords).



password = st.text_input("Enter your password", type="password")
st.write("Password entered:", password)



# ### 8. **Color Picker**
# - st.color_picker(): Allows users to pick a color from a palette.

color = st.color_picker("Pick a color")
st.write("Selected color:", color)

