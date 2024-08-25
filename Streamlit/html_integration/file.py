 # https://www.youtube.com/watch?v=sbv3yK5pMgU&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=44
 # watch video for understanding

import streamlit as st
import streamlit.components.v1 as com
with open("style.css") as source:
  design = source.read()
com.html(f"""
         
    <style>
    
    {design}
    
    </style>
     
    
     <div>
     <h1 class = "heading"> عبد الستار ایدھی </h1>
     <h5 class = "heading2">Over his lifetime, the Edhi Foundation expanded, backed entirely by private donations from Pakistani citizens across class, which included establishing a network of 1,800 ambulances. 
     By the time of his death, Edhi was registered as a parent or guardian of nearly 20,000 adopted children.</h5>
     </div>    
         
""" , width = 700 , height= 400 , scrolling= True)



# Html by using markdown

st.markdown("<button> Submit</button>" , unsafe_allow_html= True)


