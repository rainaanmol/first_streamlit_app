import streamlit
import snowflake.connector
import pandas 
import requests
from urllib.error import URLError

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.dataframe(my_fruit_list)

#lets pick a fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_show = my_fruit_list.loc[fruits_selected]
#display on the page
streamlit.dataframe(fruits_show)

def get_fruityvice_data(this_fruit_choice):
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("please select a fruit to get information")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()

##streamlit.stop()

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()

if streamlit.button("Get Fruit Load List"):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   ##my_cnx.close()
   streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
         return "thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button("Add a fruit to the List"):  
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
   





