import streamlit as st
from PIL import Image
from io import BytesIO
# Basic structure and layout
st.markdown("""
<style>
    .st-emotion-cache-12w0qpk{
        border-radius: 0.5rem;
        padding: 1rem;
        border:1px solid #A4A4A4;
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
st.sidebar.image('https://tuk-cdn.s3.amazonaws.com/can-uploader/image%20117.png',width=90)

# # Display the SVG next to the text in the sidebar
st.sidebar.write("Dashboard")
st.sidebar.write("Projects")
st.sidebar.write("User")
st.sidebar.write("Projects Status")

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