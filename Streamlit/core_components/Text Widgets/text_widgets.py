
"""  
In Streamlit, st.text and other similar functions can be used to create text widgets. 
These widgets display text in the Streamlit app and allow you to control the appearance
of text, such as size, color, and formatting. 

"""





#------------------------------------------------------------------------------------------------------



import streamlit as st

# st.text              //   Displays fixed-width text (monospaced) font

st.text("1234567890")
st.text("abcdefgHIJ")
st.text("Hi ! I am Ayesha.")








# st.markdown

# Displays text in markdown format, which allows for rich text formatting.
# Supports headers, bold, italics, lists, and more.





# Bold Text: **Bold Text**
# Italic Text: _Italic Text_
# Bold and Italic Text: **_Bold and Italic Text_**
# Headers: # Header 1, ## Header 2, ### Header 3, #### Header 4
# Numbered List: 1. First item, 2. Second item, 1. Subitem, 2. Another subitem
# Bulleted List: - First item, - Second item, - Subitem, - Another subitem
# Inline Code: `Inline code`


st.markdown("# Hi I'm header 😎")

st.markdown("**I'm Bold 🥳**")






# st.write

# A versatile function that can display various types of data, including text, markdown, DataFrames, and more.
#  Automatically detects the type of data and formats it accordingly.


st.write("you should pay intension in your studies it's really 📌 Important")
st.write("12346798")
st.write("**Are you 😴 Tired ?**")






# st.title    // Displays a large title.

st.title("Let's Do Practice 😊 ")






# st.header   //  Displays a header, which is slightly smaller than a title

st.header("I’m looking forward to our meeting.🙂")





# st.subheader    //  Displays a subheader, which is smaller than a header.


st.subheader("I can’t stop laughing at that joke! 😆")





# st.caption    //  Displays smaller text, usually used for captions or notes.

st.caption("I’m dying of laughter from this video. 🤣")




# st.code   // Displays a block of code with optional syntax highlighting.

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')





# st.latex   // Displays mathematical expressions using LaTeX syntax

st.latex(r''' a^2 + b^2 = c^2 ''')




# st.text_input    //  Accepts text input from the user.


name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")




