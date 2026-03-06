import streamlit as st
st.title("Đăng kí vào Long's App")
list_sex=["Nam","Nữ","Khác"]
list_hobbies=["Đá bóng","Bóng rổ","Bơi lội","Chạy bộ","Đạp xe","Khác"]
data_tai=''
with st.form(key="str", clear_on_submit=False):
    name=st.text_input("Họ và tên")
    age=st.slider("Tuổi", min_value=1, max_value=99, step=1)
    dia_chi=st.text_input("Địa chỉ")
    email=st.text_input("Email")
    sdt=st.text_input("Số điện thoại")
    sex=st.selectbox("Giới tính", list_sex)
    hobbies=st.multiselect("Sở thích", list_hobbies)
    chap_thuan=st.checkbox("Tôi đồng ý với các điều khoản và điều kiện")
    submit_button=st.form_submit_button(label="Đăng kí")
    if submit_button:
        if not name:
            st.error("Vui lòng nhập họ và tên.")
        elif not dia_chi:
            st.error("Vui lòng nhập địa chỉ.")
        elif not email:
            st.error("Vui lòng nhập email.")
        elif not sdt:
            st.error("Vui lòng nhập số điện thoại.")    
        elif not hobbies:
            st.error("Vui lòng chọn ít nhất một sở thích.")
        elif not sex:
            st.error("Vui lòng chọn giới tính.")
        elif not chap_thuan:
            st.error("Vui lòng đồng ý với các điều khoản và điều kiện.")
        else:
            st.success("Đăng kí thành công!")
            st.write("Thông tin của bạn:")
            st.write("Họ và tên:", name)
            st.write("Tuổi:", age)
            st.write("Địa chỉ:", dia_chi)
            st.write("Email:", email)
            st.write("Số điện thoại:", sdt)
            st.write("Giới tính:", sex)
        data_tai=f"""
            Họ và tên: {name}
            Tuổi: {age} 
            Địa chỉ: {dia_chi}
            Email: {email}  
            Số điện thoại: {sdt}
            Giới tính: {sex}
            Sở thích: {', '.join(hobbies)}  
        """
st.download_button(label="Tải thông tin của bạn", data=data_tai, file_name="")