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

#lets pick a fruit
###streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))
fruits_show = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)['Avacado','Strawberries'])

#display on the page
streamlit.dataframe(fruits_show)
