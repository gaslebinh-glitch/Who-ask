import streamlit as st
st.set_page_config(page_title="Hãy chọn 1 con vật yêu thích", page_icon=":racing_car:", layout="centered")

st.title("Hãy chọn con vật yêu thích!")
st1,st2,st3,st4,st5 = st.columns(5)
with st1:
    st1=st1.button("Con Mèo")
with st2:
    st2=st2.button("Con Chó")
with st3:
    st3=st3.button("Con Sư Tử")
with st4:
    st4=st4.button("Con Ngựa")
with st5:
    st5=st5.button("Thiên Nga")

with st1.button("Con Mèo"):
    st1.write("Mèo là một loài động vật nhỏ, thường được nuôi làm thú cưng. Chúng rất thông minh và có khả năng săn mồi tốt.")
with st2.button("Con Chó"):
    st2.write("Chó là loài động vật trung thành và thân thiện, thường được nuôi làm bạn đồng hành. Chúng có khả năng bảo vệ và giúp đỡ con người.")
with st3.button("Con Sư Tử"):
   st3.write("Sư tử là loài động vật hoang dã, được biết đến với sức mạnh và sự dũng mãnh. Chúng sống thành bầy và săn mồi theo nhóm.")
with st4.button("Con Ngựa"):
    st4.write("Ngựa là loài động vật có bốn chân, thường được sử dụng để cưỡi và kéo xe. Chúng rất nhanh nhẹn và có sức bền cao.")
with st5.button("Thiên Nga"):
    st5.write("Thiên nga là loài chim nước lớn, nổi tiếng với vẻ đẹp thanh lịch và lông trắng tinh khiết. Chúng thường sống gần các hồ và sông.")