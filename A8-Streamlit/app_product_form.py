import streamlit as st
st.title("Product Form")
name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox("Category",["Electronics","Accessories","Furniture","Clothing"])

price = st.sidebar.number_input("Price", min_value = 0)
if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully")
    st.write("Product Name :",name)
    st.write("Category :",category)
    st.write("Price :",price)