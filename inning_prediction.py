import streamlit as st
import pandas as pd
import pickle,joblib
import streamlit as st
from streamlit_option_menu import option_menu

def inning_prediction():
    st.image("ipl_img.png", width=400)
    
    with st.sidebar:
        selected_inning = st.radio("Select Inning", ["First Inning Score", "Second Inning","IPL Score Prediction"])
        
    if selected_inning == "First Inning Score": 
        # model = joblib.load(r'IPL_Prediction\first_inning_score\random_forest.pkl')
        model = joblib.load('first_inning_models/random_forest.pkl')

        st.title('First Inning Score Prediction')


        def select_feature(label, options):
            selected_option = st.selectbox(label, list(options.values()))
            
            key = next(key for key, value in options.items() if value == selected_option)
            return {label: key}

        # map city numerical codes to more descriptive labels
        city_options = {
            0:'Abu Dhabi',1:'Ahmedabad', 2:'Bangalore', 3:'Bloemfontein', 4:'Cape Town',
            5:'Centurion', 6:'Chandigarh', 7:'Chennai', 8:'Cuttack', 9:'Delhi',
            10:'Dharamsala', 11:'Durban', 12:'East London', 13:'Hyderabad', 14:'Indore',
            15:'Jaipur',16:'Johannesburg', 17:'Kanpur', 18:'Kimberley', 19:'Kochi',
            20:'Kolkata', 21:'Mumbai', 22:'Nagpur', 23:'Port Elizabeth', 24:'Pune', 25:'Raipur',
            26:'Rajkot',27:'Ranchi',28:'Sharjah',29:'Visakhapatnam'
        }

        # map batting team numerical codes to more descriptive labels
        batting_team_options = {
            0:'CSK', 1:'DC', 2:'DD', 
            3:'GL',4:'KKR',4:'KTK', 
            5:'KXIP',6:'MI',7:'PW',
            8:'RCB',9:'RPS',10:'RR',11:'SRH'
        }

        # map bowling team numerical codes to more descriptive labels
        bowling_team_options = {
            0:'CSK', 1:'DC',2:'DD',
            3:'GL',4:'KKR',5:'KTK',
            6:'KXIP',7:'MI',8:'PW',
            9:'RCB',10:'RPS',11:'RR',12:'SRH'
        }


        # Selecting venue, city, batting team, and bowling team

        col1, col2 = st.columns(2)
        with col1:
            batting_team_data = select_feature('batting_team', batting_team_options)
        with col2:
            bowling_team_data = select_feature('bowling_team', bowling_team_options)
            
        col3,col4 = st.columns(2)
        with col3:   
            city_data = select_feature('city', city_options)
        with col4:
            overs = st.number_input("Overs", value=None,min_value=1,max_value=20,step=1)

        col5,col6 = st.columns(2)
        with col5:
            wickets_last_5 = st.number_input("Wickets in Last 5 overs", value=None,min_value=5,max_value=10,step=1)
        with col6:
            wickets = st.number_input("Wickets", value=None,min_value=1,max_value=10,step=1)
        

        col7,col8 = st.columns(2)
        with col7:
            runs_last_5 = st.number_input("Runs in Last 5 overs", value=None)
        with col8:
            runs =st.number_input("Runs", value=None)


        if 'batting_team' in batting_team_data and 'bowling_team' in bowling_team_data:
            if batting_team_data['batting_team'] == bowling_team_data['bowling_team']:
                st.warning("Batting team and Bowling team are the same. Please change teams.")

            # Create a DataFrame with user inputs
        input_data = {
            'runs_last_5': runs_last_5,
            'wickets_last_5': wickets_last_5,
            'wickets': wickets,
            'runs': runs,
            'overs': overs,
            **city_data,
            **batting_team_data,
            **bowling_team_data,  
            }


        input_df = pd.DataFrame([input_data])
        if st.button('Predict'):
            prediction = model.predict(input_df)
            st.subheader('Prediction Result')
            st.markdown('<div style="background-color:skyblue;padding:10px;border-radius:5px;margin-top:7px;color:black;font-weight:bold;border:2px solid blue;">' +
                            f'Predicted Runs: {prediction[0]}' +
                            '</div>', unsafe_allow_html=True)
    ######################################################################################################################################################
    # Second Inning Score
    ####################################################################################################################################################### 

    elif selected_inning == "Second Inning":
        model = joblib.load('second_inning_models/random_forest.pkl')
        # selected_inning == "Second Inning Score": 
        # model = joblib.load(r'IPL_Prediction\first_inning_score\random_forest.pkl')
        model = joblib.load('second_inning_models/random_forest.pkl')

        st.title('Second Inning Score Prediction')

        def select_feature(label, options):
            selected_option = st.selectbox(label, list(options.values()))
            
            key = next(key for key, value in options.items() if value == selected_option)
            return {label: key}
       

        # map city numerical codes to more descriptive labels
        city_options = {
            0:'Abu Dhabi',1:'Ahmedabad', 2:'Bangalore', 3:'Bloemfontein', 4:'Cape Town',
            5:'Centurion', 6:'Chandigarh', 7:'Chennai', 8:'Cuttack', 9:'Delhi',
            10:'Dharamsala', 11:'Durban', 12:'East London', 13:'Hyderabad', 14:'Indore',
            15:'Jaipur',16:'Johannesburg', 17:'Kanpur', 18:'Kimberley', 19:'Kochi',
            20:'Kolkata', 21:'Mumbai', 22:'Nagpur', 23:'Port Elizabeth', 24:'Pune', 25:'Raipur',
            26:'Rajkot',27:'Ranchi',28:'Sharjah',29:'Visakhapatnam'
        }

        # map batting team numerical codes to more descriptive labels
        batting_team_options = {
            0:'CSK', 1:'DC', 2:'DD', 
            3:'GL',4:'KKR',4:'KTK', 
            5:'KXIP',6:'MI',7:'PW',
            8:'RCB',9:'RPS',10:'RR',11:'SRH'

        }

        # map bowling team numerical codes to more descriptive labels
        bowling_team_options = {
            0:'CSK', 1:'DC',2:'DD',
            3:'GL',4:'KKR',5:'KTK',
            6:'KXIP',7:'MI',8:'PW',
            9:'RCB',10:'RPS',11:'RR',12:'SRH'
        }


        col1, col2 = st.columns(2)
        with col1:
            batting_team_data = select_feature('batting_team', batting_team_options)
        with col2:
            bowling_team_data = select_feature('bowling_team', bowling_team_options)
            
        col3,col4 = st.columns(2)
        with col3:   
            
            city_data = select_feature('city', city_options)
            
        with col4:
            overs = st.number_input("Overs", value=None,min_value=1,max_value=20,step=1)

        col5,col6 = st.columns(2)
        with col5:
            wickets_last_5 = st.number_input("Wickets in Last 5 overs", value=None,min_value=5,max_value=10,step=1)
        with col6:
            wickets = st.number_input("Wickets", value=None,min_value=1,max_value=10,step=1)
        

        col7,col8 = st.columns(2)
        with col7:
            runs_last_5 = st.number_input("Runs in Last 5 overs", value=None)
        with col8:
            runs =st.number_input("Runs", value=None)


        if 'batting_team' in batting_team_data and 'bowling_team' in bowling_team_data:
            if batting_team_data['batting_team'] == bowling_team_data['bowling_team']:
                st.warning("Batting team and Bowling team are the same. Please change teams.")

        
            # Create a DataFrame with user inputs
        input_data = {
            'runs_last_5': runs_last_5,
            'wickets_last_5': wickets_last_5,
            'wickets': wickets,
            'runs': runs,
            'overs': overs,
            **city_data,
            **batting_team_data,
            **bowling_team_data,  
            }


        input_df = pd.DataFrame([input_data])
        if st.button('Predict'):
            prediction = model.predict(input_df)
            st.subheader('Prediction Result')
            st.markdown('<div style="background-color:skyblue;padding:10px;border-radius:5px;margin-top:7px;color:black;font-weight:bold;border:2px solid blue;">' +
                            f'Predicted Runs: {prediction[0]}' +
                            '</div>', unsafe_allow_html=True)
            
            
    # Ipl Score Prediction
    ####################################################################################################################################################### 

    else:
        # selected_inning == "IPL Score Prediction": 
       
        model = joblib.load('Ipl_Prediction_models/random_forest.pkl')

        st.title('IPL Score Prediction')

        def select_feature(label, options):
            selected_option = st.selectbox(label, list(options.values()))
            
            key = next(key for key, value in options.items() if value == selected_option)
            return {label: key}
       

        # map city numerical codes to more descriptive labels
        city_options = {
            0:'Abu Dhabi',1:'Ahmedabad', 2:'Bangalore', 3:'Bloemfontein', 4:'Cape Town',
            5:'Centurion', 6:'Chandigarh', 7:'Chennai', 8:'Cuttack', 9:'Delhi',
            10:'Dharamsala', 11:'Durban', 12:'East London', 13:'Hyderabad', 14:'Indore',
            15:'Jaipur',16:'Johannesburg', 17:'Kanpur', 18:'Kimberley', 19:'Kochi',
            20:'Kolkata', 21:'Mumbai', 22:'Nagpur', 23:'Port Elizabeth', 24:'Pune', 25:'Raipur',
            26:'Rajkot',27:'Ranchi',28:'Sharjah',29:'Visakhapatnam'
        }

        # map batting team numerical codes to more descriptive labels
        batting_team_options = {
            0:'CSK', 1:'DC', 2:'DD', 
            3:'GL',4:'KKR',4:'KTK', 
            5:'KXIP',6:'MI',7:'PW',
            8:'RCB',9:'RPS',10:'RR',11:'SRH'

        }

        # map bowling team numerical codes to more descriptive labels
        bowling_team_options = {
            0:'CSK', 1:'DC',2:'DD',
            3:'GL',4:'KKR',5:'KTK',
            6:'KXIP',7:'MI',8:'PW',
            9:'RCB',10:'RPS',11:'RR',12:'SRH'
        }

	
        col1, col2 = st.columns(2)
        with col1:
            batting_team_data = select_feature('batting_team', batting_team_options)
        with col2:
            bowling_team_data = select_feature('bowling_team', bowling_team_options)
            
        col3,col4 = st.columns(2)
        with col3:   
            
            city_data = select_feature('city', city_options)
            
        with col4:
            overs = st.number_input("Overs", value=None,min_value=1,max_value=20,step=1)

        col5,col6 = st.columns(2)
        with col5:
            wickets = st.number_input("Wickets", value=None,min_value=1,max_value=10,step=1)
        
        with col6:
            runs =st.number_input("Runs", value=None)


        if 'batting_team' in batting_team_data and 'bowling_team' in bowling_team_data:
            if batting_team_data['batting_team'] == bowling_team_data['bowling_team']:
                st.warning("Batting team and Bowling team are the same. Please change teams.")

        
            # Create a DataFrame with user inputs
        input_data = {
            'wickets': wickets,
            'runs': runs,
            'overs': overs,
            **city_data,
            **batting_team_data,
            **bowling_team_data,  
            }


        input_df = pd.DataFrame([input_data])
        if st.button('Predict'):
            prediction = model.predict(input_df)
            st.subheader('Prediction Result')
            st.markdown('<div style="background-color:skyblue;padding:10px;border-radius:5px;margin-top:7px;color:black;font-weight:bold;border:2px solid blue;">' +
                            f'Predicted Runs: {prediction[0]}' +
                            '</div>', unsafe_allow_html=True)
            

            

    # Footer
    st.sidebar.markdown('---')
    st.sidebar.markdown("Created by Deepraj Vadhwane")

if __name__ == '__main__':
    inning_prediction()



