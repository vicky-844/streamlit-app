import streamlit as st
import segno
import time


def generate_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10,
                  dark="#672eb4").save("qrcode_gen.png")

#definition (CREATE QR-CODE)
def generate_qrcode_page():

    url = st.text_input("Please enter the URL you want to encode   ⬇")

    #DISPLAY QR-CODE (-> overwrites qr-codes; otherwise add time-stamp)

    if url:
        with st.spinner("Generate QR Code:"):
            time.sleep(3)
        generate_qrcode(url)

        st.image("qrcode_gen.png",
            caption="Here you go :) ")