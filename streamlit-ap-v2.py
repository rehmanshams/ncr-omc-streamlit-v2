import streamlit as st
import requests
from PIL import Image
from io import BytesIO
# Basic structure and layout
st.markdown("""
<style>
    .st-emotion-cache-12w0qpk{
        display: flex;
        flex-direction: column;
        align-items: start;
        border-radius: 0.5rem;
        padding: 1rem;
        border:1px solid #A4A4A4;
    }
    .st-emotion-cache-1n76uvr{
        width:1136px !important
    }
    .st-emotion-cache-1y4p8pa > div {
        width:100% !important;
        align-items:center
    }
</style>
""", unsafe_allow_html=True)
# Create two columns
col1, col2, col3 = st.columns(3)

# Place a selectbox in each column
col1.write("#### NCR Onboarding Management Console")
col2.selectbox('', ['All Projects Managers', 'Option 2', 'Option 3'])
col3.selectbox('', ['All Religions', 'Option 2', 'Option 3'])

# Dashboard Links on the LeftD
# Replace with the actual image link
image_link = "https://tuk-cdn.s3.amazonaws.com/can-uploader/adwdawd.png"

# Display the image using its link
html_string = f"""
<div style=" display: flex; justify-content: center; margin-bottom:50px">
<img src="{image_link}" width="90px" />
</div>
"""
# Display the centered image in the sidebar using markdown
st.sidebar.markdown(html_string, unsafe_allow_html=True)

# Sidebar Svg One
svg_icon_Dashboard = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
  <g clip-path="url(#clip0_307_1358)">
    <path d="M3 13H11V3H3V13ZM3 21H11V15H3V21ZM13 21H21V11H13V21ZM13 3V9H21V3H13Z" fill="currentColor"/>
  </g>
  <defs>
    <clipPath id="clip0_307_1358">
      <rect width="24" height="24" fill="white"/>
    </clipPath>
  </defs>
</svg>
"""
# Sidebar Svg two
svg_icon_Projects = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
  <g clip-path="url(#clip0_307_1361)">
    <path d="M20 22H4C3.73478 22 3.48043 21.8946 3.29289 21.7071C3.10536 21.5196 3 21.2652 3 21V3C3 2.73478 3.10536 2.48043 3.29289 2.29289C3.48043 2.10536 3.73478 2 4 2H20C20.2652 2 20.5196 2.10536 20.7071 2.29289C20.8946 2.48043 21 2.73478 21 3V21C21 21.2652 20.8946 21.5196 20.7071 21.7071C20.5196 21.8946 20.2652 22 20 22ZM8 7V9H16V7H8ZM8 11V13H16V11H8ZM8 15V17H13V15H8Z" fill="currentColor"/>
  </g>
  <defs>  
    <clipPath id="clip0_307_1361">
      <rect width="24" height="24" fill="white"/>
    </clipPath>
  </defs>
</svg>
"""
# Sidebar Svg Three
svg_icon = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
  <g clip-path="url(#clip0_0_257)">
    <path d="M12.5 9.99999C12.5 8.34999 11.15 6.99999 9.49999 6.99999C7.84999 6.99999 6.49999 8.34999 6.49999 9.99999C6.49999 11.65 7.84999 13 9.49999 13C11.15 13 12.5 11.65 12.5 9.99999ZM9.49999 11C8.94999 11 8.49999 10.55 8.49999 9.99999C8.49999 9.44999 8.94999 8.99999 9.49999 8.99999C10.05 8.99999 10.5 9.44999 10.5 9.99999C10.5 10.55 10.05 11 9.49999 11ZM16 13C17.11 13 18 12.11 18 11C18 9.88999 17.11 8.99999 16 8.99999C14.89 8.99999 13.99 9.88999 14 11C14 12.11 14.89 13 16 13ZM11.99 2.00999C6.46999 2.00999 1.98999 6.48999 1.98999 12.01C1.98999 17.53 6.46999 22.01 11.99 22.01C17.51 22.01 21.99 17.53 21.99 12.01C21.99 6.48999 17.51 2.00999 11.99 2.00999ZM5.83999 17.12C6.51999 16.58 8.10999 16.01 9.49999 16.01C9.56999 16.01 9.64999 16.02 9.72999 16.02C9.96999 15.38 10.4 14.73 11.03 14.16C10.47 14.06 9.93999 14 9.49999 14C8.19999 14 6.10999 14.45 4.76999 15.43C4.26999 14.39 3.98999 13.23 3.98999 12C3.98999 7.58999 7.57999 3.99999 11.99 3.99999C16.4 3.99999 19.99 7.58999 19.99 12C19.99 13.2 19.72 14.34 19.24 15.37C18.24 14.78 16.88 14.5 16 14.5C14.48 14.5 11.5 15.31 11.5 17.2V19.98C9.22999 19.85 7.20999 18.77 5.83999 17.12Z" fill="currentColor"/>
  </g>
  <defs>
    <clipPath id="clip0_0_257">
      <rect width="24" height="24" fill="white"/>
    </clipPath>
  </defs>
</svg>
"""
# Sidebar Svg Four
svg_icon_ProjectStatus = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
  <g clip-path="url(#clip0_2203_5878)">
    <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3ZM19 19H5V5H19V19ZM7 10H9V17H7V10ZM11 7H13V17H11V7ZM15 13H17V17H15V13Z" fill="currentColor"/>
  </g>
  <defs>
    <clipPath id="clip0_2203_5878">
      <rect width="24" height="24" fill="white"/>
    </clipPath>
  </defs>
</svg>
"""
# # Display the SVG next to the text in the sidebar
st.sidebar.markdown(f'{svg_icon_Dashboard} Dashboard', unsafe_allow_html=True)
st.sidebar.markdown(f'{svg_icon_Projects} Projects', unsafe_allow_html=True)
st.sidebar.markdown(f'{svg_icon} User', unsafe_allow_html=True)
st.sidebar.markdown(f'{svg_icon_ProjectStatus} Projects Status', unsafe_allow_html=True)

# Main Content``
st.subheader("Projects")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Projects", value="654", delta="3%")
    st.text("Since last week")
with col2:
    st.metric(label="New Install", value="312", delta="2%")
    st.text("Since last week")
with col3:
    st.metric(label="System Refresh", value="342", delta="3%")
    st.text("Since last week")
with col4:
    st.metric(label="Software Essentials Only", value="0", delta="0%")
    st.text("Since last week")

st.subheader("Project Status")
col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(label="Complete", value="428", delta="4%")
    st.text("Since last week")
with col6:
    st.metric(label="In Progress", value="66", delta="29%")
    st.text("Since last week")
with col7:
    st.metric(label="Overdue", value="140", delta="-3%")
    st.text("Since last week")
with col8:
    st.metric(label="Warning", value="12", delta="-48%")
    st.text("Since last week")

st.subheader("Other Metrics")
col9, col10, col11, col12 = st.columns(4)

with col9:
    st.metric(label="Actions Completed", value="2643", delta="2%")
    st.text("Since last week")
with col10:
    st.metric(label="Documents Submitted", value="1452", delta="2%")
    st.text("Since last week")
with col11:
    st.metric(label="Contacts Submitted", value="2233", delta="2%")
    st.text("Since last week")
with col12:
    st.metric(label="Projects Pending Install", value="12", delta="-8%")
    st.text("Since last week")