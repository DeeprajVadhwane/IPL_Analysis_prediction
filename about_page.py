
import streamlit as st

def show_about_page():
    st.title("About IPL Project")

    st.subheader("IPL Cricket Insights Dashboard")
    st.write("This project aims to provide insights and analysis on Indian Premier League (IPL) cricket matches.")
    st.write("Key features of the dashboard include:")

    st.markdown("- **Year-wise Total Runs Score and Line Plot**: Select a team to visualize the year-wise total runs scored and identify peak scoring years.")
    st.markdown("- **Batsman Year-wise Score**: Select a batsman to view their year-wise scores.")
    st.markdown("- **Compare Two Teams**: Compare performance of two teams across different years.")
    st.markdown("- **Compare One Team with All Teams**: Compare one team with all other teams to gauge its performance.")

    st.subheader("IPL Auction Insights Hub")
    st.write("Explore insights from IPL auctions, including:")
    st.markdown("- **Players Played in Each Year**: Select a country to view insights on players who participated each year.")
    st.markdown("- **Teams Played in Each Year**: Select a country to view insights on teams that played each year.")
    st.markdown("- **Winning Bid Distribution**: Analyze the distribution of winning bids across players.")
    st.markdown("- **Team with the Highest Players per Year**: View insights on teams with the highest number of players each year.")

    st.subheader("First and Second Inning Prediction")
    st.write("Predict the outcome of first and second innings based on historical data and match conditions.")
    st.write("Features include:")
    st.markdown("- **Individual Player Analysis and Visualization**")
    st.markdown("- **Team Past Records Analysis and Visualization**")
    st.markdown("- **Neck to Neck Analysis Between Two Teams**")
    st.markdown("- **Batsman vs Bowler Analysis**")
    st.markdown("- **In-Depth EDA on IPL Data**")
    st.markdown("- **Bar Charts for Matches Per Season, Player of the Match, Toss Winners, etc.**")
    st.markdown("- **IPL Auction Analysis from 2013 to 2023**")
    st.markdown("- **Representing Team Wins and Lucky Venue**")
    st.markdown("- Click on the 'Predict Probability' button to see the predicted first and second inning score.")
    
    
      # Footer
    st.sidebar.markdown('---')
    st.sidebar.markdown("Created by Your Deepraj Vadhwane")