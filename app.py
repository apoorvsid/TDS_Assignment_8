import streamlit as st 

st.header("App to add two numbers")

def user_inputs():
  a = st.number_input("Enter first number")
  b = st.number_input("Enter second number")

  return a+b 

result = user_inputs()
st.subheader("Answer")
st.write(result)