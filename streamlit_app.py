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
#setting the index Fruit
my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

#Displaying the dataframe in the app
streamlit.dataframe(fruits_to_show)
# New section to display fruityice api response
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
