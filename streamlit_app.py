import streamlit

streamlit.title ('Estoy haciendo un curso')
streamlit.title ('Probando 1, 2, 3')

streamlit.header('🥣 Breakfast Menu')
streamlit.text(' 🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.dataframe(my_fruit_list)
streamlit.multiselect ("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#display the table on the page
streamlit.dataframe(my_fruit_list)
