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

# Displaying the dataframe in the app
streamlit.dataframe(fruits_to_show)
# New section to display fruityice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice1=streamlit.text_input('What fruit would you like information about?', 'kiwi')
streamlit.write('The user entered', fruit_choice1)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice1)
# streamlit.text(fruityvice_response.json()) -- write a separate line to point base URL

# Take the JSON version of the response and normalize it 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
#snowflake connector
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

fruit_choice2=streamlit.text_input('What fruit would you like information about?', 'jackfruit')
streamlit.write('Thank you for adding', fruit_choice2)
#This will not work correctly, but just go it for now
my_cur.execute("insert into fruit_load_list_values('from streamlit')")

