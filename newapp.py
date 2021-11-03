import streamlit as st


st.title("KARANE KE LIE SOOCHEE APP")

rad=st.sidebar.radio("Navigation",["Soochee mein jodane","Adyatan soochee"])

if rad=="Soochee mein jodane":
   
   a = st.checkbox("JAROORE")
   b=st.text_area("Enter list item")
   d= st.checkbox("MAHATVAPOORN NAHIN")
   e=st.text_area("Enter list ")
   
   if st.button("DONE"):
       st.success("SUCCESS")

if rad=="Adyatan soochee":
    c=st.text_area("ADD UPDATES IF ANY")
    if st.button("DONE"):
       st.success("LIST UPDATED")
