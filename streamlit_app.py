import streamlit
import pandas as pd 
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents New Healthly Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blue Berry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Harold-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Importing pandas library to read txt file from AWS s3 location          
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#setting the index Fruit
my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Displaying the dataframe in the app
streamlit.dataframe(fruits_to_show)

#Create a repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        return fruityvice_normalized

# New section to display fruityice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
        fruit_choice1=streamlit.text_input('What fruit would you like information about?')
        if not fruit_choice1:
                streamlit.error("Please select a fruit to get information.")
        else:
                back_from_function=get_fruityvice_data(fruit_choice1)
                streamlit.dataframe(back_from_function)
except URLError as e:
        streamlit.error()
  
# streamlit.write('The user entered', fruit_choice1)
# streamlit.text(fruityvice_response.json()) -- write a separate line to point base URL
streamlit.header("The fruit load list contains:")
#Snowflake related functions
def get_fruit_load_list():
        with my_cnx.cursor() as my_cur
        my_cur.execute("select * from fruit_load_list")
        return my_data_rows = my_cur.fetchall()

#Add a button to load the list
if streamlit.button("Get Fruit Load List")
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
        my_data_rows=get_fruit_load_list()
        streamlit.dataframe(my_data_rows)

# Take the JSON version of the response and normalize it 
# Output it the screen as a table
# Don't tun anything past here while we troubleshoot
streamlit.stop()
 
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# streamlit.text("Hello from Snowflake:")

fruit_choice2=streamlit.text_input('What fruit would you like information about?', 'jackfruit')
streamlit.write('Thank you for adding', fruit_choice2)
# This will not work correctly, but just go it for now
my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
