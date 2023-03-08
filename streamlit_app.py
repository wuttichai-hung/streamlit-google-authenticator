import re
import pyotp
import qrcode
import streamlit as st

st.set_page_config(
    page_title="DataHungry - Google Authenticator",
    page_icon=":bee:",
    layout="centered"
)

if "secret" not in st.session_state:
    st.session_state.secret = pyotp.random_base32()

totp = pyotp.totp.TOTP(st.session_state.secret).provisioning_uri(
    name="Demo GA", issuer_name="DataHungry")
qr_byte_data = qrcode.make(totp).get_image()


st.markdown("# Google Authenticator")
st.image(qr_byte_data, caption="QR Code - Google Authenticator")


code = st.text_input("Enter the Code", placeholder="123456")
if st.button("Verify"):
    totp = pyotp.TOTP(st.session_state.secret)
    if totp.verify(re.sub(r"\s", "", code)):
        st.success("Code verified successfully!", icon="✅")
    else:
        st.error("Sorry, the code could not be verified. Please try again.", icon="🚨")
