import streamlit as st
st.title("Price Calculator")
price = st.number_input("Enter Product Price",min_value = 0.0)
discount = st.slider("Select Discount (%)",0,50)

if st.button("Calculate"):
    final_price = price - (price*discount/100)
    st.success("Final Price : ₹" + str(final_price))