import streamlit as st
import pandas as pd
import numpy as np

st.title("Graded Assignment 8")
st.write("Use Case: Subtraction of 2 given numbers.")
st.write("Please enter 2 two numbers to be subtracted in the below text boxes")

st.text_input("First Number", key="num1")
st.text_input("Second Number", key="num2")

n1, n2 = None, None

if st.session_state.num1:
  n1 = float(st.session_state.num1)

if st.session_state.num2:
  n2 = float(st.session_state.num2)
  
if st.session_state.num1 and st.session_state.num2:
  st.write("The result of subtracting second number from the first is: "+str(n1-n2))
