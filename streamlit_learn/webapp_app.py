# streamlit is a pyhton library to create web apps for data projects  -- without needing HTML, CSS , JAVASCRIPT

# It turns your python scripts into interactive web apps just running a scripts

# to Run (python -m streamlit run streamlit_learn/webapp_app.py )

# what can you build ?
# ( Data Dashboard ,Ml model Tools ,Image/video tools ,chatbots , Resume analyzers , SQL explorers)
"""import streamlit as st
st.title(" $ My first streamlit App")
st.header("Wellcome To The streamlit App")
st.write("This is a simple app built with streamlit")

# interactive elements
name=st.text_input("What Is Your Name ? ")
if name:
    st.success(f'Hello ,{name} !')

#slider example
age=st.slider("select your age", 1, 50, 25)
st.write("Your Selected :",age)

"""

import streamlit as st

st.title(" $ Simple Calculator")

num1=st.number_input("Enter first number :")
num2=st.number_input("Enter Second number :")
operation=st.selectbox("Choose Your Operation",["Add","Subract","Multiply","Divide"])

if st.button("Calculate"):
    if operation =="Add":
        rsult= num1 +num2
    elif operation =="Subract":
        result=num1 - num2
    elif operation == "Multiply":
        result= num1 * num2
    elif operation == "Divide":
        result= num1 / num2 if num2 != 0 else "cannot divide by zero"
    st.success(f'Result : {result}')


