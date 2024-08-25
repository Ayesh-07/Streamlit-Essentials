
# ### 2. **Portfolio Website**
#    - Build a personal portfolio website using Streamlit.
#      - Use the **sidebar** for navigation between different sections (e.g., About, Projects, Contact).
#      - Use **columns** to display project details with images and descriptions.
#      - Use a **container** to organize content for each section.


import streamlit as st
st.set_page_config(page_title="Portfolio", layout="wide")

st.title("Portfolio Website")

navigation =  ["About", "Projects", "Contact"]


page = st.sidebar.selectbox("Menu" , navigation)

# About Section
if page == "About":
    with st.container():
        st.header("About Me")
        st.write("""
            Hi, I'm [Your Name], a developer passionate about creating user-friendly applications.
            I have experience in web development, data analysis, and more.
        """)
elif page == "Projects":
    st.header("My Projects")
    
    
elif page == "Contact":
    with st.container():
        st.header("Contact Me")
        st.write("""
            Feel free to reach out to me for collaboration or questions:
            - Email: your.email@example.com
            - LinkedIn: [Your LinkedIn](https://www.linkedin.com)
        """)


with st.container():
        col1, col2 = st.columns(2)

        with col1:
            # Displaying images for the projects
            st.image("images/mountain.jfif", caption="Mountain Project 1")
            st.image("images/mountain.jfif", caption="Mountain Project 2")
        
        with col2:
            # Displaying description for the projects
            st.subheader("Project 1: Mountain Explorer")
            st.write("This project is about exploring beautiful mountains around the world.")
            st.subheader("Project 2: Mountain Trekking")
            st.write("This project involves creating a trekking plan for various mountain ranges.")
            