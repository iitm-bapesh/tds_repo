import streamlit as st
import pandas as pd
import numpy as np

st.title("Graded Assignment 8")
st.write("Use Case: Subtraction of 2 given numbers.")
st.write("Please enter 2 two numbers to be subtracted in the below text boxes")

st.text_input("First Number", key="num1")
st.text_input("Second Number", key="num2")

st.write(num1)
st.write(type(num1))

st.write(num2)
st.write(type(num2))
