
import streamlit as st
import random
import string

# App Configuration
st.set_page_config(page_title="Password Generator", layout="centered")

# Styling
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🔒 Simple Password Generator</div>', unsafe_allow_html=True)
st.write("")

# Input Options
st.sidebar.header("Password Settings")
length = st.sidebar.slider("Select Password Length", min_value=6, max_value=50, value=12)
include_uppercase = st.sidebar.checkbox("Include Uppercase Letters", value=True)
include_numbers = st.sidebar.checkbox("Include Numbers", value=True)
include_special = st.sidebar.checkbox("Include Special Characters", value=True)

# Generate Password
def generate_password(length, uppercase, numbers, special):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation
    
    password = ''.join(random.choices(characters, k=length))
    return password

# Password Output
if st.button("Generate Password"):
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    st.success("Your Generated Password:")
    st.code(password, language="text")

    # Copy to clipboard
    st.button("Copy to Clipboard", on_click=lambda: st.session_state.update(clipboard=password))

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
