

# ### 1. **Personalized Welcome App**
# Create an app that welcomes users by displaying their name, a custom message, and an image or audio file.

# #### Requirements:
# - Use `st.text_input()` to collect the user’s name.
# - Display a welcome message using `st.write()` or `st.markdown()`.
# - Display an image (e.g., a logo or welcome banner) using `st.image()`.
# - Optionally, play background music using `st.audio()`.

# #### Example:
# - The user enters their name as "John".
# - The app displays: "Welcome, John! Hope you have a great day!" and shows an image of a sunrise.
# - Optional: Play relaxing music in the background.

# ---


import streamlit as st
st.title("Personalized Welcome App")
st.image("Images/banner.png", use_column_width=True)

name = st.text_input("")
if name:
   st.write(f"Welcome, {name}! Hope you have a great day!")
else:
    st.write("Welcome! Please enter your name to get a personalized greeting.")

if st.checkbox("Play relaxing music"):
 st.audio("audio/rain.wav" ,  format="audio/wav" , autoplay=True)
 
 
 
 #-------------------------------------------------------------------------------------------------------------


st.markdown("<br><br>" , unsafe_allow_html=True)   # for  adding space 

st.empty()


 #-------------------------------------------------------------------------------------------------------------



# ### 2. **Motivational Quotes App**
# Create an app that displays a motivational quote along with an image. Allow users to click a button to refresh and see a new quote.

# #### Requirements:
# - Use `st.button()` to let users refresh the quote.
# - Display the quote using `st.write()` or `st.markdown()`.
# - Display a relevant image using `st.image()`.

# #### Example:
# - The app shows the quote: "Believe you can and you're halfway there" along with an image of a mountain.
# - User clicks a "New Quote" button, and the app refreshes with a different quote and image.

# ---

import random
st.title("Motivational Quotes App")

quotes = [
    {
        "quote": "Believe you can and you're halfway there.",
        "image": "Images/mountain.jfif"  # Image path for the quote
    },
    {
        "quote": "The only way to do great work is to love what you do.",
        "image": "Images/sunset.jfif"
    },
    {
        "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "image": "Images/forest.jfif"
    },
    {
        "quote": "You miss 100 percentage of the shots you don't take.",
        "image": "Images/waterfall.jfif"
    },
    {
        "quote": "Start where you are. Use what you have. Do what you can.",
        "image": "Images/river.jpg"
    }
]



def random_quote():
     return random.choice(quotes)
 
if st.button("New Quote"):
    Quote = random_quote()
    
    st.write(f"**Quote:** *{Quote['quote']}*")
    st.image(Quote["image"], use_column_width=True)
else:
    default_quote = quotes[0]
    st.write(f"**Quote:** *{default_quote['quote']}*")
    st.image(default_quote["image"], use_column_width=True)

    

#-------------------------------------------------------------------------------------------------------------

st.markdown("<br><br>" , unsafe_allow_html=True)   # for  adding space 

st.empty()


 #-------------------------------------------------------------------------------------------------------------




# ### 3. **Simple Audio Book App**
# Create an app where users can select a chapter from an audiobook and listen to it.

# #### Requirements:
# - Use `st.selectbox()` to let users choose from different chapters of an audiobook.
# - Use `st.audio()` to play the selected chapter.

# #### Example:
# - The user selects "Chapter 1" from the dropdown, and the app plays the corresponding audio file.
# - Show the title and description of the chapter with `st.write()`.

# ---



# Title of the app
st.title("Simple Audio Book App")

# List of chapters with corresponding audio files and descriptions
chapters = [
    {
        "Title": "Chapter 1: Introduction",
        "audio": "audio/breeze-through-the-trees.wav",  # Audio file path for chapter 1
        "description": "This chapter introduces the main concepts and gives an overview of the book."
    }, 
    { 
        "Title": "Chapter 2: Rain",
        "audio": "audio/heavy-rain-drops.wav",  # Audio file path for chapter 2
        "description": "This chapter features soothing rain sounds."
    },
    {
        "Title": "Chapter 3: Liquid",
        "audio": "audio/liquid-bubble.wav",  # Audio file path for chapter 3
        "description": "Listen to the sound of liquid bubbles for a calming effect."
    },
    {
        "Title": "Chapter 4: Storm",
        "audio": "audio/strong-wild-wind-in-a-storm.wav",  # Audio file path for chapter 4
        "description": "Experience the powerful sounds of a storm."
    },
    {
        "Title": "Chapter 5: Wind",
        "audio": "audio/wind-blowing-ambience.wav",  # Audio file path for chapter 5
        "description": "Feel the serenity of wind blowing through the trees."
    }
]

# Create a list of chapter titles for the selectbox
chapter_titles = [chapter["Title"] for chapter in chapters]

# Create a selectbox to choose a chapter
selected_chapter_title = st.selectbox("Choose a chapter to listen to", chapter_titles)

# Find the selected chapter details based on the title
selected_chapter = next(chapter for chapter in chapters if chapter["Title"] == selected_chapter_title)

# Display the selected chapter title and description
st.write(f"**Selected Chapter:** {selected_chapter['Title']}")
st.write(f"*Description:* {selected_chapter['description']}")

# Play the audio for the selected chapter
st.audio(selected_chapter["audio"], format="audio/wav")






#---------------------------------------------------------------------------------------------------------

st.markdown("<br><br>" , unsafe_allow_html=True)   # for  adding space 

st.empty()


 #-------------------------------------------------------------------------------------------------------------




# ### 4. **Image Captioning App**
# Create an app where users can upload an image and write a caption for it. 
# Display the image along with the caption below.

# #### Requirements:
# - Use `st.file_uploader()` to let users upload an image.
# - Use `st.text_input()` to let users write a caption.
# - Display the image using `st.image()` and the caption using `st.write()`.

# #### Example:
# - The user uploads an image of a beach and writes "A peaceful day by the ocean."
# - The app displays the image with the caption below.

# ---


st.title("Image Captioning App")
image = st.file_uploader("Please upload your Image..." , type=["jpg", "jpeg", "png"])
caption = st.text_input("Please write a caption")
if image:
 st.image(image, caption="Uploaded Image", use_column_width=True)
if caption:
 st.write(f"**Caption:** {caption}")
 
 
 
 
 

#---------------------------------------------------------------------------------------------------------

st.markdown("<br><br>" , unsafe_allow_html=True)   # for  adding space 

st.empty()


 #-------------------------------------------------------------------------------------------------------------
 
 
 
 
# ### 5. **Audio Player with Text Display**
# Create an app that lets users play an audio file and shows some related text
# (e.g., lyrics, podcast description) while playing.

# #### Requirements:
# - Use `st.file_uploader()` to allow users to upload an audio file.
# -Use `st.text_area()` to let users paste related text (lyrics, description).
# - Use `st.audio()` to play the audio.
# - Display the text using `st.write()`.

# #### Example:
# - The user uploads a song and pastes the lyrics.
# - The app plays the song while showing the lyrics in a text box.

# ---


import streamlit as st

# Set the title of the app
st.title("Audio Player with Text Display")

# File uploader for audio
audio_file = st.file_uploader("Please add your Audio File", type=["mp3", "wav"])

# Text area for the user to input the related text (e.g., lyrics, description)
description = st.text_area("")

# If an audio file is uploaded, play it
if audio_file is not None:
    # Pass the correct variable 'audio_file' to st.audio()
    st.audio(audio_file)

# If description is provided, display it
if description:
    st.write(description)






#---------------------------------------------------------------------------------------------------------

st.markdown("<br><br>" , unsafe_allow_html=True)   # for  adding space 

st.empty()


 #-------------------------------------------------------------------------------------------------------------
 
 
 
# ### 6. **Simple Newsletter Generator**
# Create a mini-newsletter generator where users can enter their name, write a headline, body text, and upload an image, 
# which is then displayed as a formatted newsletter.

# #### Requirements:
# - Use `st.text_input()` for the user's name and the headline.
# - Use `st.text_area()` for the body text of the newsletter.
# - Use `st.file_uploader()` to let the user upload an image.
# - Display the complete newsletter using `st.markdown()` or `st.write()`.

# #### Example:
# - The user writes a headline: "Breaking News: Streamlit is Awesome!"
# - Adds a body text: "Today we explore how to build interactive apps with Streamlit..."
# - Uploads an image, and the app shows the formatted newsletter with the image included.

# ---


#Title of the App
st.title("Simple Newsletter Generator")

# User Enter his name
name = st.text_input("Enter your name")

# User Enter Headline 
headline = st.text_input("Enter the headline")


# User Enter news description 
news = st.text_area('''Enter the body text''')

# User Upload Image
file = st.file_uploader("Kindly Add Image" , type = ["jpg" , "png", "jfif"])


# Display the complete newsletter when headline or news is provided
if name:
        st.write(f"**From:** {name}")
        
if headline:
    st.write(f"### {headline}")


    
if news:
    st.write(news)


if file:
    st.image(file , caption="Newsletter Image", use_column_width=True)
    
    
    


#---------------------------------------------------------------------------------------------------------

st.markdown("<br><br>" , unsafe_allow_html=True)   # for  adding space 

st.empty()


 #-------------------------------------------------------------------------------------------------------------




# ### 7. **Media Showcase App**
# Create an app where users can upload an image, audio, or video, and display/play the uploaded media accordingly.
# The user should also be able to add a description for the media.

# #### Requirements:
# - Use `st.file_uploader()` to allow users to upload an image, audio, or video.
# - Use `st.text_area()` to let users write a description of the media.
# - Display or play the media using `st.image()`, `st.audio()`, or `st.video()`, depending on the file type.
# - Display the description using `st.write()`.

# #### Example:
# - The user uploads a video file and writes, "This is a video from my last trip."
# - The app plays the video and shows the description below.

# ---


st.title("Media Showcase App")

image = st.file_uploader("Enter Your Image" , type = ["jpg" , "png", "jfif"] )

audio = st.file_uploader("Enter Your Audio" , type = ["mp3", "wav"])

video = st.file_uploader("Enter Your Video" , type = ["mp4" , "wmv"])

text = st.text_area("Enter Your Text")


if image: 
    st.image(image , caption="Uploaded Image" , use_column_width = True)
    

if audio: 
    st.audio(audio , format="audio/wav")
    
if text: 
    st.write(text)
    
if video:
    st.video(video  ,  format="video/mp4")



#---------------------------------------------------------------------------------------------------------

st.markdown("<br><br>" , unsafe_allow_html=True)   # for  adding space 

st.empty()


 #-------------------------------------------------------------------------------------------------------------
 
 
 

# ### 8. **Daily Journal App**
# Create an app where users can write a daily journal entry and upload a related image. 
# Each day, users can write a new entry and view the last entry they wrote.

# #### Requirements:
# - Use `st.text_area()` to let users write a journal entry.
# - Use `st.file_uploader()` to let users upload an image for the day.
# - Display the current day's journal entry and image.
# - Optionally, save the entries locally (using a file or database for more advanced functionality).

# #### Example:
# - The user writes: "Today I worked on my Streamlit project" and uploads an image of their desk.
# - The app displays the journal entry and image.

# ---


from datetime import date

# Title of the app
st.title("Daily Journal App")

# Current date
current_date = date.today().strftime("%B %d, %Y")

# Display current date
st.subheader(f"Journal Entry for {current_date}")

# Text area for journal entry
journal_entry = st.text_area(f"Write your journal entry for {current_date}")

# File uploader for journal image
journal_image = st.file_uploader(f"Upload an image for {current_date}", type=["jpg", "png", "jfif"])

# Display current day's entry and image if they exist
if journal_entry:
    st.write("### Today's Journal Entry:")
    st.write(journal_entry)

if journal_image:
    st.image(journal_image, caption="Today's Image", use_column_width=True)



