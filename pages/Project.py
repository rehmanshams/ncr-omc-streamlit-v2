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
    h4{
        padding: 1.9rem 0px 1rem !important;
    }
</style>
""", unsafe_allow_html=True)
# Create two columns
col1, col2, col3 = st.columns(3)

# Place a selectbox in each column
col1.write("#### Projects Summary")
col2.selectbox('', ['All Projects Managers', 'Option 2', 'Option 3'])
col3.selectbox('', ['All Religions', 'Option 2', 'Option 3'])


# Main Content``
metrics_data = [
    {
        "header": "Projects",
        "values": [
            {"label": "Projects", "value": "654", "delta": "3%"},
        ]
    },
    {
        "header": "Project Status",
        "values": [
            {"label": "Complete", "value": "428", "delta": "4%"},
        ]
    },
    {
        "header": "Other Metrics",
        "values": [
            {"label": "Projects Pending Install", "value": "12", "delta": "-8%"}
        ]
    },
    {
        "header": "Other Metrics",
        "values": [
            {"label": "Projects Pending Install", "value": "12", "delta": "-8%"}
        ]
    },
]

# Flatten the metrics_data to get a list of all metrics
all_metrics = [
    metric for section in metrics_data for metric in section["values"]]

# Display all metrics in one row
columns = st.columns(len(all_metrics))
for idx, metric in enumerate(all_metrics):
    with columns[idx]:
        st.metric(label=metric["label"],
                  value=metric["value"], delta=metric["delta"])
        st.text("Since last week")

st.divider()
col1, col2, col3 = st.columns(3)
# Place a selectbox in each column
col1.write("#### Projects")
col2.text_input("", placeholder="Sreach for Projects")
# if search_term:
#     st.write(f"You searched for: {search_term}")
col3.selectbox('', ['Select: All', 'Option 2', 'Option 3'])

# Table Data
data = {
    "Site Name": ["COUNTRY WAFFLES-ANTIOCH", "COUNTRY WAFFLES - LIVERMORE", "COUNTRY WAFFLES - CLAYTON", "Mimosas Gourmet", "Lighthouse Bar And Grille"],
    "Project Type": ["System Refresh", "System Refresh", "System Refresh", "Installation - New System", "System Refresh"],
    "Status": ["In Progress", "In Progress", "In Progress", "In Progress", "In Progress"],
    "Progress": ["0%", "0%", "0%", "0%", "0%"]
}

# Display the table
st.table(data)
