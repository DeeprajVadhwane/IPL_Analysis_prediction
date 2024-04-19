
# main.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

import home_page

import about_page
import IPL_Cricket_Insights_Dashboard
import IPL_Auction_Insights_Hub
import inning_prediction

# Define navigation options
nav_options = ["Home", "About",'IPL Cricket Insights Dashboard','IPL Auction Insights Hub','Inning Prediction']

# Sidebar navigation
nav_selection = st.sidebar.radio("Navigation", nav_options)

# Display content based on user selection
if nav_selection == "Home":
    home_page.show_home_page()
elif nav_selection == "About":
    about_page.show_about_page()
elif nav_selection == 'IPL Cricket Insights Dashboard':
    IPL_Cricket_Insights_Dashboard.main()
elif nav_selection == 'IPL Auction Insights Hub':
    IPL_Auction_Insights_Hub.main()
elif nav_selection == 'Inning Prediction':
    inning_prediction.inning_prediction()