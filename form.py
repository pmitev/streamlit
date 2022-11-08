import streamlit as st       
     
if 'count' not in st.session_state:
   st.session_state.count = 0
else:                                                                                                                                                                             
   st.session_state.count = st.session_state.count + 1
     
st.write("Count",st.session_state.count)
     
with st.form("my_form"):     
   st.write("Inside the form")         
   slider_val = st.slider("Form slider")             
   checkbox_val = st.checkbox("Form checkbox")       
     
   # Every form must have a submit button.           
   submitted = st.form_submit_button("Submit")       
   if submitted:             
       st.write("slider", slider_val, "checkbox", checkbox_val)
     
st.write("Outside the form") 
st.write("slider", slider_val, "checkbox", checkbox_val)
