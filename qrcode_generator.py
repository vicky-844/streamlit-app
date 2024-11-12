import segno
import streamlit as st
import time


#page configuration
st.set_page_config(
    page_title="Test",
    page_icon="💚"
)


#add a banner
st.image("https://i.pinimg.com/736x/70/0f/44/700f44fc91b474c0ad943882685b174e.jpg")

#add a title
st.title("QR Code Generator")

#add a text box (GET URL & STORE IT)
url = st.text_input("Please enter the URL you want to encode   ⬇")
#st.write(url)

#definition (CREATE QR-CODE)
def generate_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10,
                  dark="#672eb4").save("qrcode_gen.png")

#DISPLAY QR-CODE (-> overwrites qr-codes; otherwise add time-stamp)
if url: #not literally url, just text input
    with st.spinner("Generate QR Code:"):
        time.sleep(1.5)
    generate_qrcode(url)
    st.image("qrcode_gen.png",
             caption="Here you go :) ")

st.markdown(
    "<br><hr><center>Made by Vickyy 💜", unsafe_allow_html=True)  #=> geht in die HMTL-Richtung

