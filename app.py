import streamlit as st


st.title("Student Management System - LLM Agent")
def input_response(user_input):
    response = input_response(user_input)  
    return response
    
user_query = st.text_input("Ask a question about books or subjects:")

if st.button("Submit"):
    response = "W."
    st.write(response)
#Eg    
user_input = "What book to read?"  
response = input_response(user_input) 
print(response)  



