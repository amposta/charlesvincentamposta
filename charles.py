import streamlit as st
from datetime import datetime, date
import markdown

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
    st.header("User Information")
    name = st.text_input("Enter your name:", value="Charles Vincent B. Amposta")
    
    # Date input for birthday
    birthday = st.date_input("Enter your birthday:", value=date(2006, 5, 20))

    # Calculate age automatically based on the birthday
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    bio = st.text_area("Enter your bio:", value="I live in Barangay Cayawan Purok-4, Eldest son of Charlie and Virlyn Amposta, a BSCpE student in SNSU")

    # Gender selection
    gender = st.selectbox("Please select your gender:", ["Female", "Male", "Prefer not to say"])

# New fields for blog posts
st.header("Create a New Blog Post")

# Blog post title and content input
post_title = st.text_input("Enter the title of your blog post:")
post_content = st.text_area("Enter the content of your blog post:")

# Create a list to store blog posts in session state if it doesn't exist
if 'posts' not in st.session_state:
    st.session_state.posts = []

# Submit button for creating a blog post
if st.button("Submit Blog Post"):
    if post_title and post_content:
        # Convert the blog post content to Markdown format for better styling
        post_content_html = markdown.markdown(post_content)
        
        # Add the post to session state
        st.session_state.posts.append({
            "title": post_title,
            "content": post_content_html,
            "author": name,
            "date": datetime.now().strftime("%B %d, %Y")
        })

        # Display the submitted blog post
        st.success(f"Your blog post '{post_title}' has been published!")
    else:
        st.error("Please fill in all fields before submitting your blog post.")

# Display the profile and submitted blog posts
with col2:
    st.subheader("User Profile")
    st.write(f"**Name:** {name}")
    st.write(f"**Bio:** {bio}")
    st.write(f"**Birthday:** {birthday.strftime('%B %d, %Y')}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    if profile_picture is not None:
        st.image(profile_picture, caption="Profile Picture", use_column_width=True)

# Display all submitted blog posts
if st.session_state.posts:
    st.subheader("Your Blog Posts")
    for post in st.session_state.posts:
        st.markdown(f"### {post['title']}")
        st.markdown(f"**By {post['author']} on {post['date']}**")
        st.markdown(post['content'])
        st.write("---")  # Separator line
else:
    st.write("No blog posts yet. Create one above!")
