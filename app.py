import streamlit as st
import pandas as pd
from dashboard.queries import get_key_metrics, get_time_series

st.set_page_config(page_title="Creator Analytics Dashboard", layout="wide")
st.title("📊 Creator Analytics Dashboard")

# Key Metrics
st.subheader("Key Performance Indicators (KPIs)")
metrics = get_key_metrics()
cols = st.columns(5)
cols[0].metric("Total Creators", metrics["total_creators"][0])
cols[1].metric("Total Views", f'{metrics["total_views"][0]:,}')
cols[2].metric("Total Likes", f'{metrics["total_likes"][0]:,}')
cols[3].metric("Total Comments", f'{metrics["total_comments"][0]:,}')
cols[4].metric("Total Revenue", f'${metrics["total_revenue"][0]:,.2f}')

# Time Series Chart
st.subheader("📈 Performance Over Time")
df_ts = get_time_series()
selected_metrics = st.multiselect(
    "Choose metrics to visualize:",
    options=["views", "likes", "comments", "revenue"],
    default=["views", "revenue"]
)

if selected_metrics:
    st.line_chart(df_ts.set_index("date")[selected_metrics])
else:
    st.warning("Select at least one metric to display the chart.")

# Optional: Data Table
with st.expander("🔍 Raw Data Table"):
    st.dataframe(df_ts)
