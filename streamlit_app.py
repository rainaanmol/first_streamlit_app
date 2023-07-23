import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.dataframe(my_fruit_list)

#lets pick a fruit
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_show = my_fruit_list.loc[fruits_selected]

#display on the page
streamlit.dataframe(fruits_show)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")

streamlit.header("Fruityvice Fruit Advice!")
##streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? -- added the columns of the table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do? -- shows the result of the fruit selected
streamlit.dataframe(fruityvice_normalized)



