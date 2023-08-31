# Importing streamlit library, which is used to build apps
import streamlit
streamlit.title('My parents New Healthly Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blue Berry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Harold-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Importing pandas library to read txt file from AWS s3 location
import pandas as pd                
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Displaying the dataframe in the app
#streamlit.dataframe(my_fruit_list)
