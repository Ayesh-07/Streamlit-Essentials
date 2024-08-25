import streamlit as st
import streamlit.components.v1 as com
import json
from streamlit_lottie import st_lottie

com.iframe( src="https://lottie.host/embed/4ffbc6cf-2473-451c-8a5a-f0de11771753/hvrTUFTQkf.json")
with open("Ani.json") as source:
    animation = json.load(source)
st_lottie(animation , width=400)
