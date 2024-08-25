import streamlit as st



# ### 1. **Basic Information Display**

# **Objective:** Create a simple Streamlit app to display user information.

# **Instructions:**
# 1. Use `st.title` to display the title of your app.
# 2. Use `st.header` to show a section header like "Personal Information."
# 3. Use `st.text` to display a fixed-width block of user information (e.g., name, age, and location).


st.title("My Portfolio")
st.header("Personal Information")
st.text('''Name: Ayesha Nudrat 
Age: 29
Location: Pakistan''')


# --------------------------------------------------------------------------------------------------------


# ### 2. **Markdown Formatting Practice**

# **Objective:** Create a Streamlit app that demonstrates various markdown features.

# **Instructions:**
# 1. Use `st.markdown` to display text with different formatting options like bold, italics, lists, and headers.
# 2. Include a block of code formatted with `st.code` to show how code looks in markdown.


# Bold
st.markdown("**I’m glad that presentation is over. 😅**")

# italic
st.markdown("_Your surprise party was amazing! 😃_")

# Bold and italic
st.markdown("**_I can’t wait to give you a big hug! 🤗_**")



# Headers

# Header 1
st.markdown(" # Your idea is fantastic! 👍")

# Header 2
st.markdown(" ## Congratulations on your achievement! 👏")

# Header 3
st.markdown(" ### We did it! Time to celebrate. 🙌 ")

# Header 4
st.markdown(" #### I’m open to new ideas. 🤲")


# lists

st.markdown("1. Do you like fruits? 🍒🍑🍍🥭")
st.markdown("2. Yummy fruits:")
st.markdown("   1. 🍏 Green Apple")
st.markdown("   2. 🍇 Grapes")

st.markdown("- Yes, here are my favorite fruits:")
st.markdown("- So tasty!")
st.markdown("  - 🥥 Coconut")
st.markdown("  - 🍅 Tomato")



# --------------------------------------------------------------------------------------------------------


# ### 3. **Interactive Text Display**

# **Objective:** Create a Streamlit app that updates text based on user input.

# **Instructions:**
# 1. Use `st.text_input` to get user input.
# 2. Display a greeting message with `st.write` or `st.markdown` that incorporates the user’s input.

name = st.text_input("Kindly Enter Your Beautiful Name")
st.write(f"Nice to meet you {name}!😍")



# --------------------------------------------------------------------------------------------------------


# ### 4. **Formatted Code Snippets**

# **Objective:** Display multiple code snippets with different programming languages.

# **Instructions:**
# 1. Use `st.code` to display code snippets in Python, JavaScript, and HTML.
# 2. Add headers and descriptions using `st.markdown`.



st.markdown("### Python Code")
st.markdown("This Python code prints the name of a country.")

# Python Code
code1 = '''
country = "Pakistan"
print(country)
'''
st.code(code1, language='python')

st.markdown("### JavaScript Code")
st.markdown("This JavaScript code logs the name of a country to the console.")

# JavaScript Code
code2 = '''
country = "Pakistan"
console.log(country)
'''
st.code(code2, language='javascript')

st.markdown("### HTML Code")
st.markdown("This HTML code displays a simple message.")

# HTML Code
code3 = '''
<div>
  <h4>I'm Muslim</h4>
</div>
'''
st.code(code3, language='html')


# --------------------------------------------------------------------------------------------------------


# ### 5. **Text Alignment and Spacing**

# **Objective:** Create an app that shows how text alignment and spacing can be managed.

# **Instructions:**
# 1. Use `st.text` to display lines of text with varying numbers of spaces.
# 2. Compare this with `st.markdown` to see how spacing and alignment are handled differently.

# jitni space do gyutni rahy gi

st.text("I could use a nap    right now. 😪")
st.text("I’m feeling a bit queasy after that meal. 🤢")
st.text("Here  we   go  again…   🙄")


# --------------------------------------------------------------------------------------------------------



# jin sahihai  bs  utni hi data hai

st.markdown("I’ll see   you at    the party, right? 😉")
st.markdown("That new job offer is too good to pass up! 🤑")
st.markdown("I’m nervous  about the big     exam.    😬")




# --------------------------------------------------------------------------------------------------------


# ### 6. **Mathematical Expressions with LaTeX**

# **Objective:** Use LaTeX to display mathematical expressions.

# **Instructions:**
# 1. Use `st.latex` to display simple mathematical formulas.
# 2. Include explanations in markdown before the LaTeX expressions.


st.markdown("### Expressions")

st.markdown("Quadratic Formula")

st.latex(r'''
    x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
''')

st.markdown("Summation")

st.latex(r'''
         
\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}

''')

st.markdown("Binomial Theorem")
st.latex(r'''
         
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k

         ''')




# --------------------------------------------------------------------------------------------------------


# ### 7. **Styled Text Display**

# **Objective:** Demonstrate different text styles and their applications.

# **Instructions:**
# 1. Use `st.markdown` to showcase various text styles like headers, bold, italics, and strikethrough.
# 2. Add descriptions or explanations for each style.

st.markdown("### Bold")
st.markdown("**I’m feeling a bit spooky today. 👻**")
st.markdown("### Bold")
st.markdown("_This pirate-themed party is a blast! ☠️_")
st.markdown("### strikethrough")
st.markdown("~~Giddy up, partner! 🤠~~")






