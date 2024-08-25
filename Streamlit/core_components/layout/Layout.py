import streamlit as st
st.set_page_config(layout="wide")

# 1. Using Columns
# You can arrange your widgets horizontally using columns.

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Animals")
    st.write("Cow")
    st.write("Goat")
    st.write("Lion")
    st.write("Tiger")
    st.write("Horse")

with col2:
    st.header("Birds")
    st.write("Owl")
    st.write("Crow")
    st.write("Parrot")
    st.write("Separow")
    st.write("Bats")

with col3:
    st.header("Colors")
    st.write("Orange")
    st.write("Pink")
    st.write("Purple")
    st.write("Yellow")
    st.write("Red")


# ----------------------------------------------------------------------------------------------------------


# 2. Containers
# Containers allow you to create sections where you can add multiple elements.


with st.container():
    st.write("This is inside a container")

st.write("This is outside the container")


# ------------------------------------------------------------------------------------------------------------

# Expander
# Use expanders to collapse and expand sections of the layout.

with st.expander("See explanation"):
    st.write("This is an expander that can be toggled open or closed.")
    
    
# ---------------------------------------------------------------------------------------------------------------

# 4. Sidebar
# Streamlit allows placing widgets or text on the sidebar for better organization.


st.sidebar.title("Sidebar Title")
st.sidebar.write("This is on the sidebar")
st.sidebar.button("Sidebar Button")


# -------------------------------------------------------------------------------------------------

# 5. Page Layout (Wide or Centered)
# By default, Streamlit uses a centered layout, but you can switch to a wide layout.

# Add this line at the beginning of your app
# st.set_page_config(layout="wide")