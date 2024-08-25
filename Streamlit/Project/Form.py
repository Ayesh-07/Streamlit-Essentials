import streamlit as st

st.title("Information Form")
st.markdown("---")

# Create the form
with st.form("Form"):
    # File uploader for image
    image = st.file_uploader("Upload your image", type=["jpg", "png", "jfif", "jpeg"])

    # Two columns for first name and last name
    col1, col2 = st.columns(2)
    with col1:
        f_name = st.text_input("Enter your first name")
    with col2:
        l_name = st.text_input("Enter your last name")
    
    # Email input
    email = st.text_input("Enter your Email")

    # Three columns for date, day, and time selection
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        date = st.date_input("Select Date")
    with col_2:
        day = st.selectbox("Enter Day", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
    with col_3:
        time = st.time_input("Select Time")
    
    # Bio text area with character limit
    bio = st.text_area("Describe yourself", max_chars=100)

    # Radio button for gender selection
    gender = st.radio("Select your gender", ("Male", "Female", "Other"))

    # Slider for age selection
    age = st.slider("Select your age", min_value=0, max_value=100)

    # Submit button
    submit = st.form_submit_button("Submit")

# Check if the form was submitted
if submit:
    if not (f_name and l_name and email and bio):
        st.warning("All fields are required.")
    else:
        # Display uploaded image if available
        if image is not None:
            st.image(image, caption="Uploaded Image", use_column_width=True)

        # Display form data
        st.write(f"**First Name:** {f_name}")
        st.write(f"**Last Name:** {l_name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Bio:** {bio}")
        st.write(f"**Selected Day:** {day}")
        st.write(f"**Selected Time:** {time}")
        st.write(f"**Selected Date:** {date}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Age:** {age}")

        # Success message
        st.success("Your information was successfully submitted.")
