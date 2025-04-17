
# import streamlit as st   
# import random
# import string

# def generate_password(length, use_digits, use_special):
#     characters = string.ascii_letters 

#     if use_digits:
#         characters += string.digits  

#     if use_special:
#         characters += string.punctuation  

#     return ''.join(random.choice(characters) for _ in range(length))

# st.title("Password Generator")
# length = st.slider("Select password Length", min_value=6, max_value=32, value=12)
# use_digits = st.checkbox("Use digits")
# use_special = st.checkbox("Use special characters")

# if st.button("Generate Password"):
#     password = generate_password(length, use_digits, use_special)
#     st.write(f"Generated Password: `{password}`")

# import streamlit as st
# import random
# import string

# # Custom Styling
# st.markdown(
#     """
#     <style>
#         body {background-color: #1e1e1e; color: white;}
#         .password-box {background: #333; padding: 10px; border-radius: 10px; text-align: center;}
#         .copy-btn {background: #ff7f50; border: none; padding: 10px; border-radius: 5px; cursor: pointer;}
#     </style>
#     """, 
#     unsafe_allow_html=True
# )

# # Function to generate password
# def generate_password(length, use_digits, use_special, exclude_similar):
#     characters = string.ascii_letters 

#     if use_digits:
#         characters += string.digits  

#     if use_special:
#         characters += string.punctuation  

#     if exclude_similar:
#         characters = characters.replace('O', '').replace('0', '').replace('l', '').replace('1', '')

#     return ''.join(random.choice(characters) for _ in range(length))

# # Streamlit UI
# st.title("🔐 Strong Password Generator")
# st.markdown("Generate a strong password with custom settings!")

# length = st.slider("📏 Select Password Length", min_value=6, max_value=32, value=12)
# use_digits = st.checkbox("🔢 Include Digits")
# use_special = st.checkbox("🔣 Include Special Characters")
# exclude_similar = st.checkbox("🚫 Exclude Similar Characters (O, 0, l, 1)")

# if st.button("✨ Generate Password"):
#     password = generate_password(length, use_digits, use_special, exclude_similar)
#     st.markdown(f"<div class='password-box'><h3>{password}</h3></div>", unsafe_allow_html=True)
#     st.code(password, language="plaintext")

#     # Copy Button
#     st.button("📋 Copy Password", on_click=lambda: st.write(f"`{password}` copied to clipboard!"))

# st.markdown("🔒 **Tip:** Use a mix of letters, digits, and special characters for a strong password!")

import streamlit as st
import random
import string

# Custom Styling to fix visibility
st.markdown(
    """
    <style>
        body {background-color: #1e1e1e; color: white;}
        .password-box {
            background: #444; 
            padding: 15px; 
            border-radius: 10px; 
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #ff7f50;  /* Coral color for better visibility */
        }
        .copy-btn {
            background: #ff7f50; 
            border: none; 
            padding: 10px; 
            border-radius: 5px; 
            cursor: pointer;
            color: white;
            font-weight: bold;
        }
    </style>
    """, 
    unsafe_allow_html=True
)


# Function to generate password
def generate_password(length, use_digits, use_special, exclude_similar):
    characters = string.ascii_letters 

    if use_digits:
        characters += string.digits  

    if use_special:
        characters += string.punctuation  

    if exclude_similar:
        characters = characters.replace('O', '').replace('0', '').replace('l', '').replace('1', '')

    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Strong Password Generator")
st.markdown("Generate a strong password with custom settings!")

length = st.slider("📏 Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("🔢 Include Digits")
use_special = st.checkbox("🔣 Include Special Characters")
exclude_similar = st.checkbox("🚫 Exclude Similar Characters (O, 0, l, 1)")

if st.button("✨ Generate Password"):
    password = generate_password(length, use_digits, use_special, exclude_similar)
    
    # Password Display Fix
    st.markdown(f"<div class='password-box'>{password}</div>", unsafe_allow_html=True)

    # Corrected Code Display (with white background)
    st.code(password, language="plaintext")

    # Copy Button (This needs clipboard API to fully work)
    st.button("📋 Copy Password", on_click=lambda: st.write(f"`{password}` copied to clipboard!"))

st.markdown("🔒 **Tip:** Use a mix of letters, digits, and special characters for a strong password!")

# Built with ❤️ by Madiha Ali Khan
st.markdown(
    """
    <div class='footer'>
        Built with ❤️ by <a href="https://portfolio-tailwind-css-plum.vercel.app/" target="_blank" style="color:#ff7f50; text-decoration: none;"><b>Madiha Ali Khan</b></a>
    </div>
    """, 
    unsafe_allow_html=True
)