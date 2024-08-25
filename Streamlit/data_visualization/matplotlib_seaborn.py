import streamlit as st
import plotly.graph_objects as go

# Define your Plotly graph
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='markers'))

# Set title and labels
fig.update_layout(title='Simple Plotly Chart',
                  xaxis_title='X Axis Title',
                  yaxis_title='Y Axis Title')

# Use Streamlit to display the Plotly chart
st.plotly_chart(fig)
