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
    st.image('resources/imgs/logo.png', width=100)

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Our Team", "Data Overview","Solution Overview", "Recommender System", "News"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)

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
    if page_selection == 'Home':


        st.title('Hi there 👋 we are CW-3')
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
            st.image('resources/imgs/mission.jpg', use_column_width=True)
        st.header('vision')
        st.write('---')
        st.write('###')

        left_column, right_column=st.columns((3,2))
        
        with left_column:

            st.write("""To become industry leaders in providing applicable solutions to problems using
            data """)
        
        with right_column:
            st.image('resources/imgs/vision.jpg')
        
        
       
        st.header('Contact us')
        st.write('---')
        # generate a html script for a contact form
        left_column, right_column = st.columns((3,2))
        with left_column:
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
        
        with right_column:
            st.image('resources/imgs/logo.png', use_column_width=True)

    if page_selection == 'Our Team':
        st.title('Meet our amazing team of Data Scientists')
        st.write('---')
        with st.container():
            st.markdown(""" **We are a diverse team of data scientists spread across Africa.**
            \nWe are solutions oriented and pride ourselves in our wealth of experience in 
        data science. 
        We pride ourselves in our teamwork and mutual understanding ensuring prompt
        delivery of products
        """)
        st.image('resources/imgs/Team.jpg', use_column_width=True)

        st.write('---')
        st.header('The Team')
        st.write('---')
        with st.container():

            left_column, center_column, right_column = st.columns((2,2,2))
            with left_column:
                st.write('#')
                st.write('#')
                st.write('''**Ngalwethu Mtirara**
                \n our team lead. 
                \n Data scientist''')
        
            with center_column:
                st.image('resources/imgs/Ngalwetu.png', caption="Ngalwetu Mtirara. \n Team lead")
            st.write('---')
            left_column, center_column, right_column = st.columns((2,2,2))

            with left_column:
                st.image('resources/imgs/Idongesit.jpg', width=150, caption='Idongesit Bokeime. Data analyst')
                st.write('#')
                st.write('''Idongesit is a Data analyst with us. 
                she mainly deals with presentations''')
                st.write('---')

                st.image('resources/imgs/Collins.jpg', width=150, caption ='Collins Tlou. Data scientist')
                st.write('''Collins is a Data scientist with us. 
                He mainly deals with modelling''')
            
            with center_column:

                st.image('resources/imgs/demo.jpg', width=150, caption='Pharis Ihaki. Data scientist')
                st.write('''Ihaki is a Data scientist with us. 
                He mainly deals with model deployment''')
                st.write('')
                st.write('---')

                st.image('resources/imgs/demo.jpg', width=150, caption='Sibusiso Sibiya. Data Analyst')
                st.write('''Sibusiso is a Data scientist with us. 
                He mainly deals with data visualisation''')

            with right_column:

                st.image('resources/imgs/demo.jpg', width=150, caption = 'Daniel Uwaoma. Data scientist')
                st.write('''Daniel is a Data scientist with us. 
                He mainly deals with Web app development ''')
                st.write('')
                st.write('---')

                st.image('resources/imgs/demo.jpg', width=150, caption = 'Mbuyiselo Mkwanazi. Data scientist')
                st.write('''Mbuyiselo is a Data scientist with us. 
                He mainly deals with modelling''')
            st.write('---')

        left_column, right_column = st.columns((3,2))    
        with left_column:
            st.write('📞 Contact us: +2869868392')
            st.write('✉   Email us: info@showstack.inc')
            st.write('Visit our website: www.showstack.org')
        with right_column:
            st.image('resources/imgs/logo.png')

    if page_selection == "News":

	    st.title("Get The Latest movie and entertainment News")
	    st.write('---')
		
	    st.write("""Get the latest releases and movie ratings all on one platform.
        Get to know about expected release dates, trailer releases and future releases of your
        favourite movies. No spoilers allowed 🚫. If you are stuck in the old movie trap, this is the easiest way 
        to get ahead in matters movies
		"""
		)
	    st.write('##')
	    st.image('resources/imgs/news.jpg', width=600, caption="https://www.pexels.com/photo/turned-on-phone-displaying-collections-book-242492/")
	    st.write('---')
	    st.write("""
		With a single click, get the latest articles in the film industry and save yourself two hours of watching a boring
        screenpiece. We are sure you will not need this (our models are that good) but why not 
        give you a chance to see the latest trends in movies from reputable news outlets. 
		""")
	    btn = st.button("Click to get latest on movies and series")

	    if btn:
		    url ="https://newsapi.org/v2/everything?"
		    request_params = {
				"q": 'Movies OR film OR oscars OR holywood OR netflix OR HBO',
				"sort by": "latest",
				"language": 'en',
				"apikey": "950fae5906d4465cb25932f4c5e1202c"
			}
		    r = requests.get(url, request_params)
		    r = r.json()
		    articles = r['articles']

		    for article in articles:
			    st.header(article['title'])
			    if article['author']:
				    st.write(f"Author: {article['author']}")
			    st.write(f"Source: {article['source']['name']}")
			    st.write(article['description'])
			    st.write(f"link to article: {article['url']}")
			    st.image(article['urlToImage'])
    if page_selection == 'Data Overview':
        st.title('Get a glimpse of our dataset 👀')
        st.write('---')
        st.write('###')
        st.write(
            '''The dataset contains features that are both cartegorical and numeric. All the features played a 
            big role in our model development and feature engineering sections of our solution development.
            We shall look at some of the features grouped into either cartegorical or numeric
        '''
        )
        st.write('---')
        st.write('###')

        left_column, right_column = st.columns((1,1))

        with left_column:
            st.header('Cartegorical features')
            st.markdown("""
            * Movie id - unique identifier for each movie
            * User id - unique identifier for each user
            * title -movie title
            * genre - movie genre
            * tag -
            """)

        with right_column:
            st.header('Numeric features')
            st.markdown("""
            * Ratings - movie rating for each movie
            * runtime - movie run time from start to finish
            * relevance - movie relevance
            * Timestamp - 
            * budget - movie budget
            """)
        
        st.write('---')
        st.header('Explore some of the feature distributions of the data')
        btn = st.radio("Select relevant visuals to view",
        ('Rating distribution', 'top actors', 'genre distribution' ))
        

        if btn == 'Rating distribution':
            st.write('---')
            st.write('rating distribution for all movies. The average rating lies at 4')
            ratings_img = Image.open(r'resources/imgs/rating_distribution.PNG')
            st.image('resources/imgs/rating_distribution.PNG')

        if btn == 'top actors':
            st.write('---')
            st.write('Top twenty actors in the dataset')
            actors_img = Image.open(r'resources/imgs/actors_distribution.PNG')
            st.image('resources/imgs/actors_distribution.PNG')

        if btn =='genre distribution':
            st.write('---')
            genres_img = Image.open(r'resources/imgs/genres.PNG')
            st.write('Top twenty genres on the dataset')
            st.image('resources/imgs/genres.PNG')
    if page_selection == 'Solution Overview':
        st.header('Our solution')
        st.markdown("""
        Our solution is a fine balance between accuracy and efficiency.
        We used an SVDpp model to make predictions of movie ratings, the model was 
        utilised to perform two types of filtering
        * content base filtering
        * collaborative based filtering
        """)
        st.write('---')
        st.header('content based filtering')
        st.write("""
        The Content-Based Recommender relies on the similarity of the items being recommended.
        The basic idea is that if you like an item, then you will also like a “similar” item. It generally works well when it's easy to determine the context/properties of each item.
        A content-based recommender works with data that the user provides, either explicitly movie ratings for the MovieLens dataset. Based on that data, a user profile is generated,
        which is then used to make suggestions to the user. As the user provides more inputs or takes actions on the recommendations, the engine becomes more and more accurate.
        """)

        st.write('---')

        st.header('Collaborative filtering')
        st.write('''
        The content based engine suffers from some severe limitations. It is only capable of suggesting movies which are *close* to a certain movie. 
        That is, it is not capable of capturing tastes and providing recommendations across genres.

        Collaborative Filtering is based on the idea that users can be used to predict how much a user will like a particular product or service those users have used/experienced.
        ''')

        st.write('---')

        st.header('Model performance')
        st.markdown('''
        We built and tested seven different collaborative filtering models and compared their performance using a 
        statistical measure known as the root mean squared error (**RMSE**), which determines the average squared difference 
        between the estimated values and the actual value. A low RMSE value indicates high model accuracy.
        ''')

        st.write('**Visual represenation of the performance of our model**')
        evaluation_img = Image.open(r'resources/imgs/model_evaluation.PNG')
        st.image('resources/imgs/model_evaluation.PNG')
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
