import streamlit as  st 
# st.title("MyAPP")
# st.write("Hello world")

# st.header("Main Title")

# st.title("Main Title")
# st.header("Header")
# st.subheader("Sub Header")
# st.text("Simple Text")
# st.markdown("**Bold Text**")
# st.success("Success Message")
# st.error("Error Message")
# st.warning("Warning Message")
# st.info("Info Message")

# user input

#text input
name = st.text_input("Enter Name:")
if name:
    st.write("Hello",name)

#number input
age = st.number_input("Enter Age:")
st.write(age)

#button
if st.button("Click me"):
    st.write("Button clicked")

#select box
city = st.selectbox(
    "Select city",
    ["Nagpur","Pune","Maharashtra"]
)
st.write(city)

#radio button
gender = st.radio(
    "Gender",
    ["Male","Female"]
)
st.write(gender)

#check box
if st.checkbox("show data"):
    st.write("Data visible")

#slider
salary = st.slider(
    "Salary",
    10000,
    100000,
    25000
)

st.write(salary)

#DataFrame

import pandas as pd
df = pd.DataFrame({
    "Name":["A","B","C"],
    "Marks":[80,90,70]
})

st.dataframe(df)

#File upload
file = st.file_uploader("Upload CSV")

if file:
    import pandas as pd
    df = pd.read_csv(file)
    st.dataframe(df)

#image
from PIL import Image
img = Image.open("download.jpg")
st.image(img)

#graph
import pandas as pd

data = {
    "Year":[2021,2022,2023],
    "Sales":[100,150,200]
}

df = pd.DataFrame(data)

st.line_chart(df.set_index("Year"))

