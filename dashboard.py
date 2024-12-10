import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Air Quality Index", layout="wide")

# Title
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