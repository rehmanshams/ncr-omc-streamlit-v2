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



# Main Content``
metrics_data = [
    {
        "header": "Projects",
        "values": [
            {"label": "Projects", "value": "654", "delta": "3%"},
            {"label": "New Install", "value": "312", "delta": "2%"},
            {"label": "System Refresh", "value": "342", "delta": "3%"},
            {"label": "Software Essentials Only", "value": "0", "delta": "0%"}
        ]
    },
    {
        "header": "Project Status",
        "values": [
            {"label": "Complete", "value": "428", "delta": "4%"},
            {"label": "In Progress", "value": "66", "delta": "29%"},
            {"label": "Overdue", "value": "140", "delta": "-3%"},
            {"label": "Warning", "value": "12", "delta": "-48%"}
        ]
    },
    {
        "header": "Other Metrics",
        "values": [
            {"label": "Actions Completed", "value": "2643", "delta": "2%"},
            {"label": "Documents Submitted", "value": "1452", "delta": "2%"},
            {"label": "Contacts Submitted", "value": "2233", "delta": "2%"},
            {"label": "Projects Pending Install", "value": "12", "delta": "-8%"}
        ]
    }
]
# Display metrics data
for section in metrics_data:
    st.subheader(section["header"])
    columns = st.columns(4)

    for idx, metric in enumerate(section["values"]):
        with columns[idx]:
         with st.container():
                st.metric(label=metric["label"], value=metric["value"], delta=metric["delta"])
                st.text("Since last week")