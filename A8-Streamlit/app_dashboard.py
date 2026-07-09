import streamlit as st
st.title("Simple Sales Dashboard")
st.write("Monthly Sales Report")
months = ["January", "February", "March", "April"]
sales = {"January": 1200,"February": 1500,"March": 900,"April": 2000}
month = st.selectbox("Select Month", months)

st.metric("Sales", sales[month])
st.bar_chart(list(sales.values()))  