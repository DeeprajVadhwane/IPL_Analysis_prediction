import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px



st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    df_matches = pd.read_csv('datasets/matches.csv')
    df_delivery = pd.read_csv('datasets/deliveries.csv')
    return df_matches, df_delivery

df_matches, df_delivery = load_data()

# Define data cleaning function
def data_cleaning(df_matches, df_delivery):
    # Drop 'umpire3' column from df_matches
    df_matches.drop(['umpire3'], axis=1, inplace=True)

    # Replace full team names with abbreviations
    df_matches.replace(['Mumbai Indians', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Deccan Chargers',
                        'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Daredevils', 'Gujarat Lions', 'Kings XI Punjab',
                        'Sunrisers Hyderabad', 'Rising Pune Supergiants', 'Kochi Tuskers Kerala', 'Pune Warriors',
                        'Rising Pune Supergiant', 'Delhi Capitals'],
                       ['MI', 'KKR', 'RCB', 'DC', 'CSK', 'RR', 'DD', 'GL', 'KXIP', 'SRH', 'RPS', 'KTK', 'PW', 'RPS', 'DD'], inplace=True)

    df_delivery.replace(['Mumbai Indians', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Deccan Chargers', 'Chennai Super Kings',
                         'Rajasthan Royals', 'Delhi Daredevils', 'Gujarat Lions', 'Kings XI Punjab',
                         'Sunrisers Hyderabad', 'Rising Pune Supergiants', 'Kochi Tuskers Kerala', 'Pune Warriors', 'Rising Pune Supergiant'],
                        ['MI', 'KKR', 'RCB', 'DC', 'CSK', 'RR', 'DD', 'GL', 'KXIP', 'SRH', 'RPS', 'KTK', 'PW', 'RPS'], inplace=True)

# Clean the data
data_cleaning(df_matches, df_delivery)

# Define functions for each visualization
def toss_decisions_across_seasons():
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_matches, x='Season', hue='toss_decision')
    plt.title('Toss Decisions Across Seasons')
    plt.xlabel('Season')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Toss Decision')
    plt.tight_layout()
    st.pyplot()

# Function to check Maximum no of match winner
def maximum_toss_winners():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.countplot(data=df_matches, x='toss_winner', order=df_matches['toss_winner'].value_counts().head(20).index)
    for a in ax.patches:
        ax.annotate(format(a.get_height()), (a.get_x(), a.get_height() + 2))
    ax.set_title('Maximum Toss Winners')
    ax.set_xlabel('Team')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot()
    
# Function to check what probability will be winning the toss will win match?
def toss_winner_match_winner():
    df = df_matches[df_matches['toss_winner'] == df_matches['winner']]
    slices = [len(df), (len(df_matches) - len(df))]
    label = ['yes', 'no']
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(slices, labels=label, autopct='%1.1f%%', colors=sns.color_palette('pastel'), explode=(0, 0.05), startangle=90)
    ax.set_title('Toss Winners Who Also Won the Match')
    ax.axis('equal')
    st.pyplot()

# Function to check total runs score by batsman across season
def total_runs_scored_by_batsmen_across_seasons(selected_team):
    df_batsmen = df_matches[['id', 'Season']].merge(df_delivery, left_on='id', right_on='match_id').drop('id', axis=1)
    if selected_team:
        df_batsmen = df_batsmen[df_batsmen['batting_team'] == selected_team]
    batsmen = df_batsmen.groupby('Season')['total_runs'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=batsmen, x='Season', y='total_runs', ax=ax)

    ax.set_title('Total Runs Scored by Batsmen Across Seasons')
    ax.set_xlabel('Season') 
    ax.set_ylabel('Total Runs')
    ax.set_xticks(ax.get_xticks())  
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  
    plt.grid()
    st.pyplot()

#Function to check six and four in the season
def six_and_fours_across_seasons(selected_team):
    six_runs = df_delivery[(df_delivery['batsman_runs'] == 6) & (df_delivery['batting_team'] == selected_team)].groupby('Season')['batsman_runs'].count().reset_index()
    four_runs = df_delivery[(df_delivery['batsman_runs'] == 4) & (df_delivery['batting_team'] == selected_team)].groupby('Season')['batsman_runs'].count().reset_index()

    six_four = six_runs.merge(four_runs, on='Season', how='outer')
    six_four.rename(columns={'batsman_runs_x': '6s', 'batsman_runs_y': '4s'}, inplace=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=six_four, x='Season', y='6s', label='6s', marker='o', color='blue')
    sns.lineplot(data=six_four, x='Season', y='4s', label='4s', marker='o', color='red')

    ax.set_title('Sixes and Fours Across Seasons')
    ax.set_xlabel('Season') 
    ax.set_ylabel('Count')
    ax.set_xticks(ax.get_xticks())  
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  
    plt.grid()
    st.pyplot()
    
#Function to check which ground is best ?
def favorite_ground_for_toss_winners():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.countplot(data=df_matches, y='venue', order=df_matches['venue'].value_counts().head(20).index, palette=sns.color_palette("pastel"))
    for p in ax.patches:
        ax.annotate(format(p.get_width()), (p.get_width(), p.get_y() + p.get_height()/2), xytext=(5, 0), textcoords='offset points')
    ax.set_title('Favorite Ground for Toss Winners')
    ax.set_ylabel('Ground')
    ax.set_xlabel('Count')
    ax.tick_params(axis='y', rotation=0)
    st.pyplot()

#Function to check Man of the match 
def max_man_of_the_match():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.countplot(data=df_matches, x='player_of_match', order=df_matches['player_of_match'].value_counts().head(20).index, palette=sns.color_palette("pastel"))
    for a in ax.patches:
        ax.annotate(format(a.get_height()), (a.get_x(), a.get_height()))
    ax.set_title('Max Man of the Match')
    ax.set_xlabel('Player of the Match')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot()

# Function to check win by wickets across the season
def win_by_wickets():
    win_by_wicket_pt = pd.pivot_table(df_matches,index='Season',
                                      columns='winner',
                                      values='win_by_wickets',
                                      aggfunc=sum)

    # Plotting
    sns.heatmap(win_by_wicket_pt, annot=True, cmap='YlGnBu')
    plt.title('Heatmap of Win by Wickets for Each Season and Winner')
    st.pyplot()


# Function to check inning effect on score/runs
def inning():
    # Grouping by match_id, inning, and batting_team, and calculating total runs
    delivery_group = df_delivery.groupby(['match_id', 'inning', 'batting_team']).sum().reset_index()
    delivery_group.drop('match_id', axis=1, inplace=True)
    delivery_group = delivery_group.sort_values(by=['batting_team', 'total_runs'], ascending=True)
    inning_1 = delivery_group[delivery_group['inning'] == 1]
    inning_2 = delivery_group[delivery_group['inning'] == 2]

    fig, axs = plt.subplots(2, 1, figsize=(10, 12))

    fig1 = px.box(inning_1, x='batting_team', y='total_runs', title='1st Inning')
    fig1.update_xaxes(tickangle=45)

    # Create boxplot for 2nd inning
    fig2 = px.box(inning_2, x='batting_team', y='total_runs', title='2nd Inning')
    fig2.update_xaxes(tickangle=45)

    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    
# Function to check year wise batsman
def year_wise_batsman_score(df_players_runs,season, batsman):
    season_data =df_players_runs[df_players_runs['Season'] == season]
    batsman_data = season_data[season_data['batsman'] == batsman]
    # batsman_data['']
    return batsman_data
# Function to select batting team and over based on season and Find Total runs scored against each bowler
def over_wise_runs(df_players_runs, season, batting_team, over):

    season_data = df_players_runs[df_players_runs['Season'] == season]

    over_runs = season_data[(season_data['batting_team'] == batting_team) & (season_data['over'] == over)]
    
    over_runs_info = over_runs.groupby(['batsman', 'bowler'])['total_runs'].sum().reset_index()

    fig = px.bar(over_runs_info, x='bowler', y='total_runs', title=f'Total runs scored against each bowler in over {over} by {batting_team} in {season}')
    fig.update_xaxes(title='Bowler')
    fig.update_yaxes(title='Total Runs')
    st.plotly_chart(fig)
    
    st.subheader('Top 5 Run Scorers in the Over:')
    top_scorers = over_runs.groupby('batsman')['total_runs'].sum().sort_values(ascending=False).head(5)
    st.write(top_scorers)
    
# Function to compare the teams  if we select same team it will give error
def team1_vs_team2(team1, team2):
    if team1 == team2:
        st.error("Please select different teams.")
        return
    
    match1 = df_matches[((df_matches['team1'] == team1) & (df_matches['team2'] == team2)) | 
                        ((df_matches['team1'] == team2) & (df_matches['team2'] == team1))]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Season', hue='winner', data=match1, palette='Set3', ax=ax)
    plt.title(f"Matches between {team1} and {team2}")
    plt.xlabel('Season')
    plt.ylabel('Number of Matches')
    plt.xticks(rotation=45)
    st.pyplot(fig)
   
# function is to compare the team against other team
def comparator(team_1):
    teams = ['MI', 'KKR', 'RCB', 'DC', 'CSK', 'RR', 'DD', 'GL', 'KXIP', 'SRH', 'RPS', 'KTK', 'PW']
    teams.remove(team_1)
    opponents = teams.copy()
    mt1 = df_matches[((df_matches['team1'] == team_1) | (df_matches['team2'] == team_1))]
    comparison_data = {}
    for i in opponents:
        mask = (((mt1['team1'] == i) | (mt1['team2'] == i))) & ((mt1['team1'] == team_1) | (mt1['team2'] == team_1))
        mt2 = mt1.loc[mask, 'winner'].value_counts().to_dict()
        comparison_data[i] = mt2.get(i, 0)
    return comparison_data


# Define the Streamlit app
def main():
 
  
    st.header('Total Runs Scored by Batsmen Across Seasons')
    visualization_option = st.selectbox('Select Visualization', 
                                        ('Total Runs Scored by team 1',))

    if visualization_option == 'Total Runs Scored by team 1':
        selected_team = st.selectbox('Select Team', df_matches['team1'].unique())
        total_runs_scored_by_batsmen_across_seasons(selected_team)
        
    
            
    # elif visualization_option == 'Total Runs Scored by team 2':
    #     selected_team = st.selectbox('Select Team', df_matches['team2'].unique())
    #     total_runs_scored_by_batsmen_across_seasons(selected_team)

    df1 = df_players_runs = df_matches[['id','Season','city','date','team1','team2',]]
    df2 = df_delivery[['match_id','batting_team','batsman','batsman_runs','bowler','bye_runs','legbye_runs','noball_runs','total_runs',]]
    df_players_runs = pd.merge(df1,df2,left_on="id",right_on='match_id')

    st.title('Batsman Year-wise Score')
    selected_season = st.selectbox('Select Season:', df_players_runs['Season'].unique())
    selected_batsman = st.selectbox('Select Batsman:', df_players_runs['batsman'].unique())
    if st.button('Show Batsman Score'):
        batsman_score = year_wise_batsman_score(df_players_runs,selected_season, selected_batsman)
        st.write(batsman_score)

    
    st.subheader('Compart Two Teams')
    teams = df_matches['team1'].unique()
    seasons = df_matches['Season'].unique()
    
    # Select team1 and team2
    team1 = st.selectbox("Select Team 1:", teams)
    team2 = st.selectbox("Select Team 2:", teams)
    
    # Run analysis when button is clicked
    if st.button("Run Analysis", key="run_analysis_button"):
        team1_vs_team2(team1, team2)

     # Select team
     
    st.subheader('Compare your team with other teams')
    team_1 = st.selectbox("Select Team:", ['MI', 'KKR', 'RCB', 'DC', 'CSK', 'RR', 'DD', 'GL', 'KXIP', 'SRH', 'RPS', 'KTK', 'PW'])
    # Run analysis when button is clicked
    if st.button("Compare"):
        comparison_data = comparator(team_1)
        fig = go.Figure(go.Bar(
            x=list(comparison_data.keys()),
            y=list(comparison_data.values()),
            marker_color='indianred'
        ))
        fig.update_layout(title=f'Comparison of Wins for {team_1}',
                          xaxis_title='Opponent Teams',
                          yaxis_title='Number of Wins')
        st.plotly_chart(fig)
        
    ###################################################################################################
        
    df1 = df_players_runs = df_matches[['id','Season','city','date','team1','team2','player_of_match']]
    df2 = df_delivery[['match_id','batting_team','batsman','batsman_runs','bowler','bye_runs',
                       'legbye_runs','noball_runs','penalty_runs','total_runs','over']]
    df_players_runs = pd.merge(df1,df2,left_on="id",right_on='match_id')
        
    st.header('Total Runs Scored Against Each Bowler in a Specific Over')
    season = st.selectbox('Select Season', df_players_runs['Season'].unique())

    # Filter DataFrame based on selected season
    season_data = df_players_runs[df_players_runs['Season'] == season]

    batting_teams = season_data['batting_team'].unique()
    overs = season_data['over'].unique()
    batting_team = st.selectbox('Select Batting Team', batting_teams)
    over = st.selectbox('Select Over', overs)


    if st.button('Over runs analysis'):
        over_wise_runs(df_players_runs, season, batting_team, over)


    # #Total Runs Scored Each Over in IPL Seasons
    # seasons_list = df_matches['Season'].unique().tolist()

    # # Streamlit app
    # st.title('Total Runs Scored Each Over in IPL Seasons')
    # selected_season = st.selectbox('Select Season', seasons_list)

    # if selected_season:
    #     display_runs_each_over(df_matches, selected_season)
        
    
  
    st.header('Data Analysis')
    visualization_option = {
        'Toss Decisions Across Seasons': toss_decisions_across_seasons,
        'Maximum Toss Winners': maximum_toss_winners,
        'Toss Winners Who Also Won the Match': toss_winner_match_winner,
        'Favorite Ground for Toss Winners': favorite_ground_for_toss_winners,
        'Max Man of the Match': max_man_of_the_match,
        'Total Runs by Batting Team': inning,
        
    }
 
    # Multiselect for selecting visualization options
    selected_options = st.multiselect('Select Visualization', list(visualization_option.keys()))

    # Execute selected analyses when button is clicked
    if st.button("Run Analysis"):
        for option in selected_options:
            analysis_func = visualization_option.get(option)
            if analysis_func:
                analysis_func()
    

if __name__ == '__main__':
    main()
