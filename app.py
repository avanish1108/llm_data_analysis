# Streamlit frontend
import streamlit as st
import pandas as pd
from agent import get_agent
import os

st.set_page_config(page_title="LLM Data Analyst", layout="wide")

st.title("📊 LLM-Powered Data Analyst")
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1]
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Preview of your dataset:")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about your data:")

    if question:
        with st.spinner("Analyzing..."):
            agent = get_agent(df)
            response = agent.run(question)
            st.markdown("### Response")
            st.write(response)
