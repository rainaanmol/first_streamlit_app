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
##streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))
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
       streamlit.datatframe(back_from_function)
      
    
    
    ##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       ##fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       ##streamlit.dataframe(fruityvice_normalized)

except URLError as e:
    streamlit.error()

##streamlit.text(fruityvice_response.json())
##streamlit.write('The user entered ', fruit_choice)
# write your own comment -what does the next line do? -- added the columns of the table

# write your own comment - what does this do? -- shows the result of the fruit selected


streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
##my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
##my_data_row = my_cur.fetchone()
##streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding ', add_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")


