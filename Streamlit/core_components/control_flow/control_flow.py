# 1. Conditional Statements (if-else)
# You can use if-else blocks to control what gets rendered on the Streamlit app based on certain conditions.

import streamlit as st

st.title("Conditional Rendering Example")

user_input = st.text_input("Enter something:")

if user_input:
    st.write(f"You entered: {user_input}")
else:
    st.write("Please enter something.")


#-------------------------------------------------------------------------------

# 2. Loops (for, while)

st.title("Loop Example")

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    st.write(f"Number: {number}")
    
# ------------------------------------------------------------------------

# Event-Based Control (Buttons)



st.title("Button Control Example")

if st.button('Click Me'):
    st.write("Button clicked!")
else:
    st.write("Click the button to see a message.")
