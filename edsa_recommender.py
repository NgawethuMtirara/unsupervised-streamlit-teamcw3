"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

#import image and animation libraries
import requests
import streamlit_lottie
from streamlit_lottie import st_lottie
from PIL import Image

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

#load image resources 
vision_img = Image.open(r'resources/imgs/vision.jpg')
mission_img = Image.open(r'resources/imgs/mission.jpg')

#create a lottie loading algorithm
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#load  lottie urls
home_lottie = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_lnlbyoqx.json') 

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Our Team", "Data Overview", "Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)

    if page_selection == 'Home':
        st.title('Hi there :wave: we are CW-3')
        st.write('---')
        st.write('###')
        st.write("""\n We are a team of data scientists at [EXPLORE Data science academy](https://www.explore.ai/)  
        We deliver accurate solutions to real world problems using data """)
        #st_lottie(home_lottie)
        st.write('---')
        
        st.header('Mission')
        st.write('---')

        left_column, right_column = st.columns((3,2))
        st.write('---')

        with left_column:
            st.write("""To deliver accurate and applicable machine learning algorithms that solve 
            real world problems. """)
            st.write("""We aim to combine machine intelligence to human intelligence to come up with 
            cutting edge solutions to localised real-world problems  """)

        with right_column:
            st.image(mission_img, use_column_width=True)
        st.header('vision')
        st.write('---')
        st.write('###')

        left_column, right_column=st.columns((3,2))
        
        with left_column:

            st.write("""To become industry leaders in providing applicable solutions to problems using
            data """)
        
        with right_column:
            st.image(vision_img)

        st.header('Contact us')
        st.write('---')
        # generate a html script for a contact form
        contact_form = """
				<form action="https://formsubmit.co/andrewpharisihaki@gmail.com" method="POST">
     <input type="text" name="message" placeholder = "enter a message" required>
     <input type="email" name="email" placeholder = "enter your email" required>
     <button type="submit">Send</button>
     """
        st.markdown(contact_form, unsafe_allow_html=True)

        #styling the contract form using a css file
        def locall_css(filename):
            with open(filename) as f:
                st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

        locall_css(("style/style.css"))

    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
