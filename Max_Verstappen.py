import streamlit as st
st.title("Đặt món ăn xem Australian Grand Prix 2026(6/3/2026-8/3/2026)")
list_banghe=["Bàn ghế 1","Bàn ghế 2","Bàn ghế 3","Bàn ghế 4","Bàn ghế 5","Không"]
list_doan=["Bánh mì","Bánh bao","Bánh mì kẹp thịt","Bánh mì chả cá","Bánh mì xúc xích","Không"]
list_douong=["Coca-cola","Pepsi","7up","Miranda","Fanta","Không"]
list_trangmieng=["Kem","Bánh ngọt","Bánh kem","Bánh quy","Bánh bông lan","Không"]
with st.form(key="str", clear_on_submit=True):
    option=st.multiselect("Chọn bàn ghế", list_banghe)
    option1=st.multiselect("Chọn đồ ăn", list_doan)
    option2=st.multiselect("Chọn đồ uống", list_douong)
    option3=st.multiselect("Chọn tráng miệng", list_trangmieng)
    submit_button=st.form_submit_button(label="Đặt")
    if submit_button:
        st.success("Đặt món thành công!")
        st.write("Bạn đã chọn:")
        st.write("Bàn ghế:", ", ".join(option))
        st.write("Đồ ăn:", ", ".join(option1))
        st.write("Đồ uống:", ", ".join(option2))
        st.write("Tráng miệng:", ", ".join(option3))
