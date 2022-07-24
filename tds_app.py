import streamlit as st
import pandas as pd
import numpy as np

st.title("Graded Assignment 8")
st.header("Use Case: Subtraction of 2 given numbers.")
st.write("Please enter 2 two numbers to be subtracted in the below text boxes")

st.text_input("First Number", key="num1")
st.text_input("Second Number", key="num2")

n1, n2 = None, None
valid1 = False
valid2 = False

if st.session_state.num1:
  try:
    n1 = float(st.session_state.num1)
    valid1 = True
  except ValueError:
    st.error('Please enter a number for first number')

if st.session_state.num2:
  try:
    n2 = float(st.session_state.num2)
    valid2 = True
  except ValueError:
    st.error('Please enter a number for second number') 

if st.session_state.num1 and st.session_state.num2 and valid1 and valid2:
  st.write("The result of subtracting second number from the first is: ",str(n1-n2))
