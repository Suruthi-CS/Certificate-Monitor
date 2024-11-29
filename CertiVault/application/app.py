import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64
import os

# Streamlit configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Helper function to load an image and encode it in base64
def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Define paths to assets
assets_dir = "C:/CertiVault/assets"
background_image_path = os.path.join(assets_dir, "college_image.png")
logo_image_path = os.path.join(assets_dir, "logo.png")

# Convert images to base64
background_image_base64 = load_image_as_base64(background_image_path)
logo_image_base64 = load_image_as_base64(logo_image_path)

# CSS styling for background and layout
st.markdown(
    f"""
    <style>
        body {{
            background: url(data:image/png;base64,{background_image_base64}) no-repeat center center fixed;
            background-size: cover;
        }}
        .stApp {{
            background: transparent;
        }}
        .top-bar {{
            background: white;
            height: 120px;  /* Increased height for the top bar */
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 100;
        }}
        .top-bar h1 {{
            font-size: 40px;  /* Increased font size for better visibility */
            font-weight: bold;
            color: #007bff;
        }}
        .container {{
            margin-top: 140px;  /* Adjusted for the taller top bar */
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            min-height: calc(100vh - 120px);
        }}
        .login-box {{
    background: white;
    padding: 30px;  /* Increased padding for a more spacious layout */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    text-align: center;
    max-width: 400px;  /* Maximum width */
    width: 100%;
    height: 350px;  /* Set a fixed height */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 20px;  /* Add spacing from other elements if needed */
}}
        .login-box img {{
            max-width: 100px;
            margin-bottom: 20px;
        }}
        .stButton {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .stButton > button {{
            width: 20%;  /* Make the buttons take full width */
            padding: 2px;
            background: #007bff;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
            margin: 5px 0;  /* Reduced margin between buttons */
        }}
        .stButton > button:hover {{
            background: #0056b3;
        }}
        .stButton > button span {{
            color: #007bff;  /* Set button text color to blue */
        }}
        .divider {{
            margin: 20px 0;
            font-size: 14px;
            color: #999;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Ensure the top bar is rendered correctly
st.markdown(
    """
    <div class="top-bar">
        <h1>Certificate Monitor</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Login box layout
st.markdown(
    f"""
    <div class="container">
        <div class="login-box">
            <img src="data:image/png;base64,{logo_image_base64}" alt="College Logo">
            <h2 style="color: #007bff;">Thiagarajar College of Engineering</h2>
            <h3 style="color: #007bff;">Login As</h3>
    """,
    unsafe_allow_html=True,
)

# Streamlit buttons rendered directly inside the login box
if st.button("College Admin"):
    st.session_state.profile = "Institute"
    switch_page("login")  # Redirect to the admin login page

if st.button("Verifier"):
    st.session_state.profile = "Verifier"
    switch_page("login")  # Redirect to the verifier login page

# End login box HTML
st.markdown(
    """
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
