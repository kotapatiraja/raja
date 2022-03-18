import streamlit as st

st.title("""hello""")
x=st.slider("your selection")
st.write("you selected :", x*x)
select1=st.sidebar.selectbox("No of items",('1','2','many'))
st.write("you select:",select1)

from datetime import time
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

from datetime import datetime
appointment1=st.slider("schedule your appointment date:",
                       value=(datetime(2022,2,3,5,35 )))
st.write("your date:",appointment1)
x=st.date_input("pick a date:")
y=st.time_input("set a time:")
st.write('you selected date:',x)
y=st.write('your set time:',y)
