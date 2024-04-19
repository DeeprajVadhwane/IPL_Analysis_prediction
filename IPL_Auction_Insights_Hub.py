import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




df_auction = pd.read_csv('datasets/auction.csv')
df_auction['Country'] = df_auction['Country'].str.strip()

def country_wise_analysis(df, country):
    # Perform analysis for the selected country
    country_data = df[df['Country'] == country]
    num_participants = len(country_data)

    # Group by Year and aggregate player names as a list
    players_by_year = country_data.groupby('Year')['Player'].apply(list).reset_index()

    # Display players played in each year
    st.write('## Players Played in Each Year')
    st.write(players_by_year)

    # Group by Year and aggregate team names as a list
    teams_by_year = country_data.groupby('Year')['Team'].apply(list).reset_index()

    # Display the DataFrame
    st.write('## Teams Played in Each Year')
    st.write(teams_by_year)

    # Create a bar plot for Base price
    st.subheader('Base Price by Year')
    fig, ax = plt.subplots()
    sns.barplot(data=country_data, x='Year', y='Base price', ax=ax)
    plt.xticks(rotation=90)  # Rotate x-axis labels
    plt.yticks(rotation=90)  # Rotate y-axis labels
    st.pyplot(fig)

    st.subheader('Team with the Highest Players per Year')
    high_players = country_data.groupby(['Year', 'Team'])['Player'].count().reset_index()
    st.bar_chart(high_players.pivot(index='Year', columns='Team', values='Player'))

    return num_participants

def team_analysis(df, team):
    st.write("Team Wise Analysis")
    team_data = df[df['Team'] == team]
    num_participants = len(team_data)

    players_by_year = team_data.groupby('Year')['Player'].apply(list).reset_index()

    st.write('## Players Played in Each Year')
    st.write(players_by_year)

    # Group by Year and aggregate country names as a list
    countries_by_year = team_data.groupby('Year')['Country'].apply(list).reset_index()

    st.write('## Countries Played Against in Each Year')
    st.write(countries_by_year)

    # Create a bar plot for Base price
    st.subheader('Base Price by Year')
    fig, ax = plt.subplots()
    sns.barplot(data=team_data, x='Year', y='Base price', ax=ax)
    plt.xticks(rotation=90)  # Rotate x-axis labels
    plt.yticks(rotation=90)  # Rotate y-axis labels
    st.pyplot(fig)

    st.subheader('Country with the Highest Players per Year')
    high_players = team_data.groupby(['Year', 'Country'])['Player'].count().reset_index()
    st.bar_chart(high_players.pivot(index='Year', columns='Country', values='Player'))

    return num_participants

def highest_player_representation(df):
    st.subheader("Country with the Highest Player Representation")
    country_counts = df['Country'].value_counts()
    highest_country = country_counts.idxmax()
    st.write(f"The country with the highest number of players represented is {highest_country} with {country_counts.max()} players.")

def player_distribution_by_season(df):
    st.subheader("Player Distribution by Country Across IPL Seasons")
    player_distribution = df.groupby(['Year', 'Country']).size().unstack(fill_value=0)
    sns.heatmap(player_distribution,  annot=True, fmt="d")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

def country_participation_trends(df):
    st.subheader("Participation Trends of Players from Specific Countries Over Years")
    participation_trends = df.groupby(['Year', 'Country']).size().unstack(fill_value=0)
    st.line_chart(participation_trends)

def top_20_countries(df):
    st.subheader('Top 20 Countries by Player Representation')
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Country', order=df['Country'].value_counts().head(20).index, ax=ax)
    plt.xticks(rotation=90)
    plt.xlabel('Country')
    plt.ylabel('Number of Players')
    st.pyplot(fig)

def top_10_teams(df):
    st.subheader('Top 10 Teams by Player Representation')
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Team', order=df['Team'].value_counts().head(10).index, ax=ax)
    plt.xticks(rotation=90)
    plt.xlabel('Team')
    plt.ylabel('Number of Players')
    st.pyplot(fig)


def main():
    st.subheader("IPL Auction Insights Hub: Unveiling Player Dynamics and Team Strategies")

    # Display the dataset
    st.write('### Dataset')
    st.write(df_auction)

    # Get unique countries from the dataset
    countries = df_auction['Country'].unique()
    # Dropdown menu to select a country
    selected_country = st.selectbox('Select a country:', countries)


    if st.button('Run Country-wise Analysis'):
        num_participants = country_wise_analysis(df_auction, selected_country)
        st.write(f'Number of participants from {selected_country}: {num_participants}')

    # Get unique teams from the dataset
    teams = df_auction['Team'].unique()
    # Dropdown menu to select a team
    selected_team = st.selectbox('Select a team:', teams)

    # Perform team-wise analysis when a team is selected
    if st.button('Run Team-wise Analysis'):
        num_participants = team_analysis(df_auction, selected_team)
        st.write(f'Number of participants from {selected_team}: {num_participants}')

    # Run analysis functions based on user selection
    analysis_options = {
        "Country with Highest Player Representation": highest_player_representation,
        "Player Distribution by Country Across IPL Seasons": player_distribution_by_season,
        "Participation Trends of Players from Specific Countries Over Years": country_participation_trends,
        "Top 20 Countries": top_20_countries,
        'Top 10 Teams': top_10_teams
    }
    
    selected_analysis = st.multiselect("Select an Analysis", list(analysis_options.keys()))

    if st.button("Run Analysis"):
        for analysis_name in selected_analysis:
            analysis_func = analysis_options.get(analysis_name)
            if analysis_func:
                analysis_func(df_auction)

    # Footer
    st.sidebar.markdown('---')
    st.sidebar.markdown("Created by Deepraj Vadhwane")

if __name__ == "__main__":
    main()