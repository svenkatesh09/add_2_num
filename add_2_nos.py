import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app




# Header
st.header("Welcome to addition app")
# Subheader
st.subheader("Enter 2 numbers to be added")
num1 = st.text_input("Enter first number to be added", "Type Here ...")
num2 = st.text_input("Enter second number to be added", "Type Here ...")

 
# display the result when the submit button is clicked

if(st.button('Submit')):
    if  num1.isnumeric() and num2.isnumeric():
        ans=int(num1)+int(num2)
        result = ans
        st.success(result)
    else:
        result = "please enter numeric value"
        st.error(result)
        
    
