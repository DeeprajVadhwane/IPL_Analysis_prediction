# home_page.py
import streamlit as st

def show_home_page():
    st.image('ipl_img.png', caption='Indian Premier League', use_column_width=False)
    st.title('Welcome to IPL Home Page 🏏')
 

    # Information about the IPL
    st.write('The Indian Premier League (IPL) is a professional Twenty20 cricket league in India. It was founded by the Board of Control for Cricket in India (BCCI) in 2008, with the inaugural season held in 2008.')
    st.write('The IPL features franchise teams representing various cities and states of India. It has emerged as one of the most popular and lucrative cricket leagues in the world.')

    # Explain how IPL helps people
    st.write('The IPL provides a platform for young and talented cricketers to showcase their skills on a global stage. It entertains millions of cricket enthusiasts with high-quality cricketing action and thrilling matches.')
    st.write("The Indian Premier League (IPL), also known as the TATA IPL for sponsorship reasons, is a men's Twenty20 (T20) cricket league held annually in India. Founded by the BCCI in 2007, the league features ten city-based franchise teams. The IPL usually takes place during the summer, between March and May each year. It has an exclusive window in the ICC Future Tours Programme, resulting in fewer international cricket tours occurring during the IPL seasons.")
    st.write("The IPL is the most popular cricket league in the world; in 2014, it ranked sixth in average attendance among all sports leagues. In 2010, the IPL became the first sporting event to be broadcast live on YouTube. Inspired by the success of the IPL, other Indian sports leagues have been established.")

    # Key Information
    st.markdown("## Key Information")
    st.write("- **Starting Year**: 2008")
    st.write("- **Format**: Twenty20 (T20) cricket")
    st.write("- **Broadcast**: Telecasted globally, attracting millions of viewers")

    
      # Footer
    st.sidebar.markdown('---')
    st.sidebar.markdown("Created by Your Deepraj Vadhwane")

# Call the function to display the home page
show_home_page()
