import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Air Quality Index", layout="wide")
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 2.5rem; /* Adjust font size if needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Simulating a database for user credentials (use a real database in production)
if "valid_users" not in st.session_state:
    st.session_state.valid_users = {"user1": "password1", "user2": "password2", "admin": "1234"}

# Function for user authentication
def authenticate(username, password):
    return st.session_state.valid_users.get(username) == password

# Function for user registration
def register_user(username, password):
    if username in st.session_state.valid_users:
        return False  # Username already exists
    st.session_state.valid_users[username] = password
    return True

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None

# Login Page
if not st.session_state.authenticated:
    st.markdown('<h1 class="title">Login to Air Quality Index</h1>', unsafe_allow_html=True)
    
    # Tabs for login and registration
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        # Create columns for customized width
        col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column width ratios

        with col2:  # Center-align the inputs
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if authenticate(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.rerun()  # Refresh the app to show the dashboard
                else:
                    st.error("Invalid username or password.")

    with tab2:
        # Registration page
        st.subheader("Register a New Account")
        reg_username = st.text_input("New Username", key="reg_username")
        reg_password = st.text_input("New Password", type="password", key="reg_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
        if st.button("Register"):
            if reg_password != confirm_password:
                st.error("Passwords do not match.")
            elif reg_username in st.session_state.valid_users:
                st.error("Username already exists. Please choose another.")
            elif reg_username and reg_password:
                if register_user(reg_username, reg_password):
                    st.success("Registration successful! You can now log in.")
                else:
                    st.error("Failed to register. Please try again.")
            else:
                st.error("Please fill in all fields.")

# Dashboard Page
if st.session_state.authenticated:
    # Sidebar content
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()  # Refresh the app to show the login page

    # Main dashboard content
    st.title("📊 AIR QUALITY INDEX")

    # Power BI Dashboard URL
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYmQ3OTc1YTktYzE5YS00NDg3LTlkOWYtZmNjMWQyZDFmZGU3IiwidCI6ImFlM2Y0YzNjLTM5YWYtNGRlYi05OWExLTlkZGQxYzA2OWZhMCJ9"
    # Embed Power BI dashboard using an iframe
    st.markdown(
        f"""
        <iframe 
            src="{power_bi_url}" 
            width="100%" 
            height="800"
            frameborder="0" 
            allowfullscreen="true">
        </iframe>
        """,
        unsafe_allow_html=True,
    )
