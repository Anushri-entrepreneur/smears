#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st

st.title("YOUR CM1 FRIEND ")
st.sidebar.header("TOPICS")
rad=st.sidebar.radio("TOPICS",["Time value of money","Interest rates","Discount rates nominal"])
print(rad)
if rad=="Time value of money":
   x=st.number_input("enter amount")
   y=st.number_input("enter interest in 0.00 form",min_value=0.05,max_value=0.20,step=1.0)
   z=st.number_input("enter no.of years",min_value=1,max_value=50,step=2)

   if st.button("Submit"):
      st.success("Submitted")
      a=x*(1+(y*z))
      st.write('The amount from simple intrest is',a)
      b=x*((1+y)**(z))
      st.write('The amount from compound intrest is',b)

if rad=="Interest rates":
   st.write("Finding Nominal interest rate")
   p1=st.number_input("Enter p1",min_value=0.5,max_value=20.00,step=0.5)
   i1=st.number_input("Enter i",min_value=0.05,max_value=0.20,step=1.0)
   ip1=p1*((1+i1)**(1/p1)-1)
   z1=st.button("Submit1")

   st.write("Nominal rate of interest ip is",ip1)

   st.write("Finding effective interest rate")
   p2=st.number_input("Enter p2",min_value=0.5,max_value=20.00,step=0.5)
   ip2=st.number_input("Enter ip value ",min_value=0.05,max_value=0.20,step=1.0)
   i2=((1+(ip2/p2))**p2)-1
   if st.button("Submit"):
      st.success("Submitted")
   st.write("effective rate of interest i is",i2)
if rad=="Discount rates nominal":
   a1=st.write("Nominal discount")

   p3=st.number_input("Enter p in number form",min_value=0.5,max_value=20.00,step=0.5 )
   d1=st.number_input("Enter d in(0.00) form",min_value=0.05,max_value=0.20,step=1.0)
   dp1=p3*(1-((1-d1)**(1/p3)))
   z2=st.write("Submitted")
   print(z2)
   st.write("Discount rate is ",dp1)























# In[ ]:





# In[ ]:
