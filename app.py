import streamlit as st

# Title and description
st.title("Insurance Application Form")
st.write("Fill out the form below:")

# Address input
address_input = st.text_input("Address", "50 Laughton Ave M6N 2W9")

# First name input
first_name_input = st.text_input("First Name", "Kiel")

# Last name input
last_name_input = st.text_input("Last Name", "Dang")

# Date of birth inputs
st.write("Date of Birth:")
month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
date_input = st.number_input("Date", 1, 31, 23)
year_input = st.number_input("Year", 1900, 2023, 1994)

# Prevent auto closing the web after application finishes
st.button("Submit")

# Display the inputs
st.write("Address:", address_input)
st.write("First Name:", first_name_input)
st.write("Last Name:", last_name_input)
st.write("Date of Birth: {} {}, {}".format(month, date_input, year_input))