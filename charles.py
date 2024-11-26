import streamlit as st
from datetime import datetime

# Logo upload or path
logo = st.file_uploader("Upload your logo (jpg, jpeg, png):", type=["jpg", "jpeg", "png"], key="logo_uploader")

# Create columns for logo, title, and profile picture
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    # Display the logo if uploaded
    if logo is not None:
        st.image(logo, caption="Logo", use_column_width=True)

with col2:
    # Set the title of the application
    st.title("Welcome to My Blog")

with col3:
    # Profile picture upload
    st.header("Profile Picture")
    profile_picture = st.file_uploader("Upload your profile picture (jpg, jpeg, png):", type=["jpg", "jpeg", "png"])

# Create columns for user input
col1, col2 = st.columns([3, 1])

with col1:
    st.header("User  Information")
    name = st.text_input("Enter your name:", value="Charles Vincent B. Amposta")
    birthday = st.text_input("Enter your birthday (e.g., May 20, 2006):", value="May 20, 2006")
    age = st.text("Enter age:" , value="18")
    bio = st.text_area("Enter your bio:", value="I live in Barangay Cayawan Purok-4, Eldest son of Charlie and Virlyn Amposta, a BSCpE student in SNSU")

    # New fields for hobbies and interests
    hobbies = st.text_input("Enter your hobbies (comma-separated):")
    interests = st.text_input("Enter your interests (comma-separated):")

# Gender selection
gender = st.selectbox("Please select your gender:", ["Female", "Male", "Prefer not to say"])

# Submit button
if st.button("Submit"):
    if name and bio and birthday and hobbies and interests:
        # Display the submitted information
        st.write("### Submitted Information:")
        st.write(f"**Name:** {name}")
        st.write(f"**Bio:** {bio}")
        st.write(f"**Birthday:** {birthday}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Hobbies:** {', '.join(hobbies.split(','))}")
        st.write(f"**Interests:** {', '.join(interests.split(','))}")
        
        # Display profile picture if uploaded
        if profile_picture is not None:
            st.image(profile_picture, caption="Profile Picture", use_column_width=True)

        # Thank you message
        st.success("Thank you for submitting your information!")
    else:
        st.error("Please fill in all fields before submitting.")

# Reset functionality
if st.button("Reset"):
    st.experimental_rerun()
