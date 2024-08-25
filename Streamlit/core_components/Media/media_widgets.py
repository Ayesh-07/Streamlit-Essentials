
# In Streamlit, media_widgets refers to widgets that allow you to display various types of media content, 
# such as images, audio, and video, directly in your Streamlit app.


#--------------------------------------------------------------------------------------------------------------

import streamlit as st


# st.image()
# Displays images in the app. You can use it to show static images from files, URLs, or even image data.

st.image("images.jfif", caption="This is an image", use_column_width=True)


# st.audio()
# Plays audio files. You can provide an audio file path, a URL, or audio data as input.


st.audio("rain.wav", format="audio/wav")


# st.video()
# Displays videos. You can use it to show video files from local paths, URLs, or video data.

st.video("https://www.youtube.com/watch?v=RjiqbTLW9_E&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW", format="video/mp4")