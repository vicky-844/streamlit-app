import streamlit as st

# no need to import the libs from different/called pages

from decode_qrcode_page import decode_qrcode_page
from generate_qrcode_page import generate_qrcode_page

# page config
st.set_page_config(
    page_title="MY QR CODE GENERATING APP",
    page_icon="😊"
)

# add a banner
# you can also add a google image link
st.image("https://i.pinimg.com/736x/70/0f/44/700f44fc91b474c0ad943882685b174e.jpg")


# add a sidebar
options = ['Generate QR Code', 'Decode QR Code', 'About Me']
page_selection = st.sidebar.selectbox("Menu", options)

#
if page_selection == "Generate QR Code":
    generate_qrcode_page()
elif page_selection == "Decode QR Code":
    decode_qrcode_page()
elif page_selection == "About Me":
    st.title("A few words about me")
    #st.write("")
    #st.image("")

##
st.markdown(
    "<br><hr><center>Made by Vickyy 💜", unsafe_allow_html=True)  #=> geht in die HMTL-Richtung
